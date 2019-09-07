# Elastic Search

## setup & install

### setup python

1. create virtual environment(not necessary if you don't want this)
   1. > virtualenv venv-ml8
   2. > `source venv-ml8/bin/activate` (under mac) `. venv-ml8/bin/activate` (under powershell)
   3. > pip install jieba
   4. > pip install elasticsearch
   5. > pip install flask
   6. > pip install flask_restful
   7. > pip install gensim
   8. > pip install tensorflow
   9. > pip install keras


### setup docker

#### preparation

   1. change all coding to UTF-8 including stop_words.txt, need coding in seq2seq.py
   2. change flask address from ip to docker service name in es_plugins/config/IKAnalyzer.cfg.xml
   3. change es address from ip to docker service name in config.py's ES_HOST,

#### build images

   1. if es version changed, then modify docker-build-es/dockerfile to update the version of es and ik there, and run `docker build -t="<account prefix>/elasticsearch-with-ik:<version>" ./docker-build-es` under project root folder
   2. if you want the image to be used universally, **push** the local tagged image to docker hub with your own account as image prefix before upload

### run containers

#### for network
   > `docker network create flask-es-ml8-nlp` for linux/mac/win 10 \
   > `docker network create -d nat flask-es-ml8-nlp` for win server

#### for elastic search container
   1. > `docker run -d --name elasticsearch-with-ik --net flask-es-ml8-nlp -p 9200:9200 -p 9300:9300 -v ${pwd}/es_plugins/config/IKAnalyzer.cfg.xml:/usr/share/elasticsearch/config/analysis-ik/IKAnalyzer.cfg.xml -v ${pwd}/es_plugins/config/user_defineword.dic:/usr/share/elasticsearch/config/analysis-ik/user_defineword.dic -v ${pwd}/es_plugins/config/user_stopword.dic:/usr/share/elasticsearch/config/analysis-ik/user_stopword.dic -e "discovery.type=single-node" leolin16/elasticsearch-with-ik:7.3.0` under powershell in win or linux, or following if already copied over via dockerfile： `docker run -d --name elasticsearch-with-ik --memory 2048m --net flask-es-ml8-nlp -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" leolin16/elasticsearch-with-ik:1.0`, memory option is needed when on win server
   2. install yk plugin if not already embeded in the es image: `/usr/share/elasticsearch/bin/elasticsearch-plugin install https://github.com/medcl/elasticsearch-analysis-ik/releases/download/v7.3.0/elasticsearch-analysis-ik-7.3.0.zip`

### setup local

#### Linux - Ubuntu

1. > wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
2. > sudo apt-get install apt-transport-https
3. > echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee -a /etc/apt/sources.list.d/elastic-7.x.list
4. > sudo pat-get update && sudo apt-get install elasticsearch
5. > sudo vi /etc/elasticsearch/elasticsearch.yml -> change node.name, network.host(from 192.168.0.1 to 0.0.0.0 if running within a virtual env to bind the service to all network interface inside venv), discovery.seed_hosts(from host1/host2 to 127.0.0.1), cluster.initial_master_nodes(from node-1/node-2 to real node name)
6. > sudo /bin/systemctl daemon-reload
7. > sudo /bin/systemctl enable elasticsearch.service
8. > sudo /bin/systemctl start elasticsearch.service
9. > test by `curl -XGET 127.0.0.1:9200

### download material

1. > download mapping: `wget http://media.sundog-soft.com/es7/shakes-mapping.json`
2. > submit mapping to es: `curl -H "Content-Type: application/json" -XPUT 127.0.0.1:9200/shakespeare --data-binary @shakes-mapping.json`
3. > download actual work: `wget http://media.sundog-soft.com/es7/shakespeare_7.0.json`
4. > submit work to es index: `curl -H "Content-Type: application/json" -XPOST '127.0.0.1:9200/shakespeare/_bulk' --data-binary @shakespeare_7.0.json`
5. > search in es: `curl -H  "Content-Type: application/json" -XGET '127.0.0.1:9200/shakespeare/_search?pretty' -d '{"query" : {"match_phrase" : {"text_entry" : "to be or not to be"}}}'`

## Building

## Search

## Analysis