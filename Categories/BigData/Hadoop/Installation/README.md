#  Installation Modes

* Standalone
* Pseudo-Distributed
* Fully Distributed

## Standalone

* single node - one JVM process
* using local file storage rather than HDFS
* Yarn doesn't run either

### install jdk

> java --version

### open following link

#### download

> [hadoop](www.apache.org/dyn/closer.cgi/hadoop/common/) -> 
> download *.tar.gz file

#### unpack

> unpack with `tar xvfz something.tar.gz`

#### cd

> `cd ~/hadoop-install/hadoop-?.?.?/`

#### create folder

> `mkdir input`

#### copy local files into input folder

> `cp etc/hadoop/* input/`

#### list files under the folder

> `ls -ls input/`

#### run hadoop for map & reduce jobs

> `bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-2.7.3.jar grep input output 'dfs[a-z.]+'`

***please notice that the output directory should be a non-existance folder***

#### check output

> `cat output/*`

#### list output structure

> `ls -ls output/`

## Pseudo-Distributed

* single node - 2 JVM processes to simulate 2 nodes(master & slave)
* using HDFS for storage
* Yarn installed

### pre-reqs

1) greater than 50GB free disk spaces
2) Install ssh(both client & server). SSH is required for master slave communication and should not prompt you password authentication (instead using public certificate)
   ***if no .ssh folder, execute ssh localhost first***
   1. generate rsa
        > cd ~/.ssh/

        > ssh-keygen -t rsa

        > cat ./id_rsa.pub >> ./authorized_keys
   2. or generate dpa
        > ssh-keygen -t dsa -P '' -f ~/.ssh/id_dsa

        > cat ~/.ssh/id_dsa.pub >> ~/.ssh/authorized_keys

   3. SSH client is installed by default for ubuntu
      1) ubuntu: need install ssh server by `sudo apt-get install openssh-server`
      2) (mac: enable ssh via system preferences -> Sharing -> Remote Login)
   4. test ssh
        > ssh localhost
3) Install Java
   1) mac:
        > /usr/libexec/java_home
   2) ubuntu: somewhere in /usr/lib/jvm
        > sudo apt install default-jdk

        ***to change java  version
        > sudo update-alternatives --config java
4) setup java env
    > cd <hadoop folder>/etc/hadoop
    
    ***add following to hadoop-env.sh:***
    > `export JAVA_HOME=/Library/Java/JavaVirtualMachines/jdk1.?.jdk/Contents/Home`

    > `export HADOOP_PREFIX=/Users/<some one>/<hadoop folder>/hadoop-2.?.?`

    > if edit with nano, ctrl+x to save and exit

    > execute `hadoop-env.sh` to setup

5) setup configuration for hadoop in distributed mode under hadoop folder
   1) ***edit common config***
        > nano etc/hadoop/core-site.xml

        ```xml
            <configuration>
                <property>
                    <name>fs.defaultFS</name>
                    <value>hdfs://localhost:9000</value>
                </property>
            </configuration>
        ```

   2) ***edit hdfs config*** Pseudo mode only has single node, thus replcation should be set to 1
        > nano etc/hadoop/hdfs-site.xml

        ```xml
            <configuration>
                <property>
                    <name>fs.replication</name>
                    <value>1</value>
                </property>
            </configuration>
        ```

   3) ***edit mapreduce config*** setup resource manager (local[run mapreduce locally]/classic[mapreduce version 1]/yarn[mapreduce version 2])
        > nano etc/hadoop/mapred-site.xml

        ```xml
            <configuration>
                <property>
                    <name>mapreduce.framework.name</name>
                    <value>yarn</value>
                </property>
            </configuration>
        ```

   4) ***edit mapreduce config*** setup yarn capabilities
        > nano etc/hadoop/yarn-site.xml

        ```xml
            <configuration>
                <property>
                    <name>yarn.nodemanager.aux-services</name>
                    <value>mapreduce_shuffle</value>
                </property>
            </configuration>
        ```

6) format the name node:
   ***under hadoop folder***
   > bin/hdfs namenode -format

7) start the master and slave nodes:
   ***under hadoop folder***
   > sbin/start-dfs.sh
   
## Fully Distributed

* a cluster of machines - 2 JVM processes to simulate 2 nodes(master & slave)
* too complicated, usually using commercial types like Cloudera/MapR/Hortonworks


