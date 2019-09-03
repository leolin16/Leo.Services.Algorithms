# Intro

## install on docker swarm with postgre and all-spark-notebook

Please refer to Leo.Data.Science
'sha1:c2a73212ae07:068c44d9bc9275e917a9e2f8a7c70b6191f6fd21'

### online solution

[free online edtion of spark](https://databricks.com/)

### local installation
   1. Jupyter notebook + python3
      1. python3 installation via anaconda or standalone python installer
      2. start jupyter notebook via `jupyter notebook`
   2. Java, Py4j, Spark
      1. Java: jdk
      2. Py4j: pip install py4j
      3. Spark: [spark-2.4.3-bin-hadoop2.7.tgz](https://www.apache.org/dyn/closer.lua/spark/spark-2.4.3/spark-2.4.3-bin-hadoop2.7.tgz) (can download via wget)-> extract to c:\spark
   3. Set Winutils
      1. [Winutils](https://github.com/steveloughran/winutils/releases/download/tag_2017-08-29-hadoop-2.8.1-native/hadoop-2.8.1.zip)
      2. unzip and get the winutils.exe -> put it in c:\winutils\bin
   4. Set Path and start jupyter
      1. set below paths in USER variable for PC:
         1. SPARK_HOME C:\spark
         2. PYSPARK_DRIVER_PYTHON_OPTS notebook
         3. PYSPARK_DRIVER_PYTHON ipython
         4. PATH %SPARK_HOME%
         5. JAVA_HOME C:\Prigram Files\Java\jdk?.?.?_???
         6. HADOOP_HOME C:\winutils
      2. Verify from cmd
         1. > pip install findspark
         2. > python
         3. > import findspark
         4. > findspark.init()
         5. > import pyspark
      3. Verify from jupyter notebook
         1. > jupyter notebook
         2. > import findspark
         3. > findspark.init()
         4. > import pyspark