# thumbnail_maker_multiprocessing_async.py - based on queue edition
# still needs improvement, like make async mixed with threading for io-bound operationw
import time
import os
import logging
from urllib.parse import urlparse
from urllib.request import urlretrieve
from queue import Queue
import threading
from threading import Thread, Lock
import multiprocessing
import asyncio
import aiohttp
import aiofiles

import PIL
from PIL import Image

FORMAT = "[%(threadName)s, %(asctime)s, %(levelname)s] %(message)s"
logging.basicConfig(filename='logfile_async.log', level=logging.DEBUG, format=FORMAT)

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

    async def download_image_coroutine(self, session, url):
        # download each image and save to the input dir
                logging.info("downloading image at URL " + url)
                img_filename = urlparse(url).path.split('/')[-1]
                img_filepath = self.input_dir + os.path.sep + img_filename

                # urlretrieve(url, img_filepath)
                async with session.get(url) as response:
                    async with aiofiles.open(img_filepath, 'wb') as f:
                        content = await response.content.read()
                        await f.write(content)

                img_size = os.path.getsize(img_filepath)
                # self.downloaded_bytes += img_size
                self.dl_size += img_size
                logging.info("image [{} bytes] saved to {}".format(img_size, img_filepath))

                self.img_queue.put(img_filename)


    async def download_images_coroutine(self, img_url_list):

        async with aiohttp.ClientSession() as session:
            for url in img_url_list:
                # download each image and save to the input dir
                await self.download_image_coroutine(session, url)


    def download_images(self, img_url_list):

        # validate inputs
        if not img_url_list:
            return
        os.makedirs(self.input_dir, exist_ok=True)

        logging.info("beginning image downloads")

        start = time.perf_counter()
        loop = asyncio.get_event_loop()
        try:
            loop.run_until_complete(self.download_images_coroutine(img_url_list))
        finally:
            loop.close()
        end = time.perf_counter()

        # self.img_queue.put(None) # since None s have been added in main routine
        logging.info("downloaded {} images in {} seconds".format(len(img_url_list), end - start))
    
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


        num_processes = multiprocessing.cpu_count()
        for _ in range(num_processes):
            p = multiprocessing.Process(target=self.perform_resizing)
            p.start()

        self.download_images(img_url_list) # since no queue for download anymore, call should be put after resizing multiprocessing part
        # run_until_complete will take the responsibility for waiting until download_images completes
        # dl_queue.join()  # block the main thread until all downloads complete -> all downloading files have been added to img_queue

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