FROM ubuntu:16.04
USER root

#ENV
ENV HADOOP_HOME=/opt/hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-arm64
ENV PATH=$PATH:$HADOOP_HOME/bin:$HADOOP_HOME/sbin:$JAVA_HOME/bin
ENV java_path /usr/lib/jvm/java-8-openjdk-arm64

ENV HDFS_NAMENODE_USER=root
ENV HDFS_DATANODE_USER=root
ENV HDFS_SECONDARYNAMENODE_USER=root
ENV YARN_RESOURCEMANAGER_USER=root
ENV YARN_NODEMANAGER_USER=root

#RUN
RUN apt-get update && apt-get install -y \
    ssh \
    rsync \
    vim \
    wget \
    sudo \
    openjdk-8-jdk


#hadoop stuff
RUN wget https://dlcdn.apache.org/hadoop/common/hadoop-3.4.0/hadoop-3.4.0.tar.gz && \
    tar -xzf hadoop-3.4.0.tar.gz && \
    mv hadoop-3.4.0 $HADOOP_HOME && \
    rm hadoop-3.4.0.tar.gz


RUN echo "export JAVA_HOME=$java_path" >> $HADOOP_HOME/etc/hadoop/hadoop-env.sh


# Set SSH for passwordless access
RUN ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
    cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
    chmod 0600 ~/.ssh/authorized_keys

#ADD
ADD hdfs-site.xml $HADOOP_HOME/etc/hadoop/hdfs-site.xml
ADD core-site.xml $HADOOP_HOME/etc/hadoop/core-site.xml
ADD yarn-site.xml $HADOOP_HOME/etc/hadoop/yarn-site.xml
ADD mapred-site.xml $HADOOP_HOME/etc/hadoop/mapred-site.xml
ADD bootstrap.sh /bootstrap.sh
RUN chmod +x /bootstrap.sh

#Expose
EXPOSE 9870 8088 9864 19888

#add path
RUN echo 'export PATH=$PATH:/opt/hadoop/bin:/opt/hadoop/sbin' >> ~/.bashrc

#CMD
CMD ["/bootstrap.sh"]

#Build the image
#docker build -t hadoop-docker .

#Run the container. Rememeber to cd to current directory before running the command
#otherwise the volume will not be mounted correctly.

#docker run -it -p 9870:9870 -p 8088:8088 --name hadoop-container -v "$PWD":/project hadoop

#Check the hadoop processes
#docker exec -it hadoop-container jps

#Enter into the container
#docker exec -it hadoop-container bash
