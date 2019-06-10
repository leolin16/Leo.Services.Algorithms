# Intro

## how much data

### facebook

* Current storage = `300 petabytes`
* Processed perday = `600 terabytes`
* Users per month = `1 billion`
* Likes per day = `2.7 billion`
* Photos uploaded per day = `300 million`

### NSA

* Current storage = `~5 exabytes`
* Processed perday = `30 petabytes`
* touches internet traffic per day = `1.6%`

### Google

* Current storage = `15 exabytes`
* Processed perday = `100 petabytes`
* Number of pages indexed = `60 trillion`
* Unique search users per month > `1 billion`

## revolution

* Storage: `GFS/HDFS(apache)` -> google file system
* to run the data processing task: `yarn`(cluster resource management)
* define a **data Processing** task: `MapReduce`(user defines map and reduce tasks using mapreduce api) -> Hive(from sql to mapreduce, sql interface to hadoop) -> `spark`
* Database/Search: `NoSql-BigTable/HBase`(no modification, just adding/deleting), Hue(for sql writting)
  
## new revolution

* Caffeine, Pregel, Dremel
* Cloudera: first commercial hadoop company
* pig: a way to convert unstructured data into structured form
* Oozie: workflow management system
* Flume/Sqoop: get data into/from hadoop
* spark: a way to perform cool transformations in a functional way on big data
* HBase: dbms on top of hadoop
* ELK: ES(elastic search) + Logstash(collect logs) + Kibana(analyze & report)

## hadoop versions

1) Apache - latest techs
2) Cloudera-CDH
3) Hortonworks-HDP