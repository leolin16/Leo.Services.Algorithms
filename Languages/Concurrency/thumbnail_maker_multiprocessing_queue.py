# thumbnail_maker_multiprocessing.py - based on queue edition
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
from queue import Queue
import threading
from threading import Thread, Lock
import multiprocessing

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile_queue.log', level=logging.DEBUG, format=FORMAT)

class ThumbnailMakerService(object):
    def __init__(self, home_dir='.'):
        self.home_dir = home_dir
        self.input_dir = self.home_dir + os.path.sep + 'incoming'
        self.output_dir = self.home_dir + os.path.sep + 'outgoing'
        self.img_queue = multiprocessing.JoinableQueue()
        # self.dl_queue = Queue()
        self.dl_size = 0
        # self.downloaded_bytes = 0
        self.resized_size = multiprocessing.Value('i', 0)
        self.img_count = multiprocessing.Value('i', 0)

    def download_image(self, dl_queue, dl_size_lock):
        # download each image and save to the input dir
        while not dl_queue.empty():
            try:
                url = dl_queue.get(block=False) # block=False makes that if the queue is empty, get() will not block and willl give an exception
                logging.info("downloading image at URL " + url)
                img_filename = urlparse(url).path.split('/')[-1]
                img_filepath = self.input_dir + os.path.sep + img_filename
                urlretrieve(url, img_filepath)
                img_size = os.path.getsize(img_filepath)
                # self.downloaded_bytes += img_size
                with dl_size_lock:
                    self.dl_size += img_size
                logging.info("image [{} bytes] saved to {}".format(img_size, img_filepath))

                self.img_queue.put(img_filename)
                # self.img_list.append(img_filename)
                dl_queue.task_done()
            except Queue.Empty:
                logging.info("Queue empty")

    # def download_images(self, img_url_list):
    #     # validate inputs
    #     if not img_url_list:
    #         return
    #     os.makedirs(self.input_dir, exist_ok=True)

    #     logging.info("beginning image downloads")

    #     start = time.perf_counter()
    #     for url in img_url_list:
    #         # download each image and save to the input dir
    #         img_filename = urlparse(url).path.split('/')[-1]
    #         urlretrieve(url, self.input_dir + os.path.sep + img_filename)
    #         self.img_queue.put(img_filename)
    #     end = time.perf_counter()
    #     self.img_queue.put(None)
    #     logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))

    def perform_resizing(self):
        # validate inputs
        os.makedirs(self.output_dir, exist_ok=True)

        logging.info("beginning image resizing")
        # num_images = len(os.listdir(self.input_dir))
        target_sizes = [32, 64, 200]

        start = time.perf_counter()
        while True:
            filename = self.img_queue.get()
            if filename:
                logging.info("resizing image {}".format(filename))
                orig_img = Image.open(self.input_dir + os.path.sep + filename)
                for basewidth in target_sizes:
                    img = orig_img
                    # calculate target height of the resized image to maintain the aspect ratio
                    wpercent = (basewidth / float(img.size[0]))
                    hsize = int((float(img.size[1]) * float(wpercent)))
                    # perform resizing
                    img = img.resize((basewidth, hsize), PIL.Image.LANCZOS)

                    # save the resized image to the output dir with a modified file name
                    new_filename = os.path.splitext(filename)[0] + \
                        '_' + str(basewidth) + os.path.splitext(filename)[1]
                    out_filepath = self.output_dir + os.path.sep + new_filename
                    img.save(out_filepath)

                    with self.resized_size.get_lock(): # return multiprocessing.Lock
                        self.resized_size.value += os.path.getsize(out_filepath)

                os.remove(self.input_dir + os.path.sep + filename)
                with self.img_count.get_lock():
                    self.img_count.value += 1
                logging.info("done resizing image {}".format(filename))
                self.img_queue.task_done()
            else:
                self.img_queue.task_done()
                break
        end = time.perf_counter()

        logging.info("created {} thumbnails in {} seconds".format(self.img_count, end - start))

    def make_thumbnails(self, img_url_list):
        logging.info("START make_thumbnails")
        # pool = multiprocessing.Pool()
        start = time.perf_counter()
        dl_queue = Queue()
        dl_size_lock = Lock()

        # download images
        for img_url in img_url_list:
            dl_queue.put(img_url)

        num_dl_threads = 4
        for _ in range(num_dl_threads):
            t = Thread(target=self.download_image, args=(dl_queue, dl_size_lock))
            t.start() # no need to join this, coz when t2 is done, then we're done. and t2 is always after this t
        # resize images
        # t2 = Thread(target=self.perform_resizing)
        # t1.start()
        # t2.start()
        # t1.join()

        num_processes = multiprocessing.cpu_count()
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.perform_resizing)
            p.start()

        dl_queue.join()  # block the main thread until all downloads complete -> all downloading files have been added to img_queue

        for _ in range(num_processes):
            self.img_queue.put(None)
        # start_resize = time.perf_counter()
        # pool.map(self.resize_image, self.img_list)
        # end_resize = time.perf_counter()
        # p.join ()

        end = time.perf_counter()
        # pool.close()
        # pool.join()
        # logging.info("created {} thumbnails in {} seconds".format(len(self.img_list), end_resize - start_resize))
        logging.info("END make_thumbnails in {} seconds".format(end - start))
        logging.info("Initial size of downloads: [{}]  Final size of images: [{}]".format(self.dl_size, self.resized_size.value))