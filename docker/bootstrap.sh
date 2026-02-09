# start ssh server
service ssh start

# format namenode

if [ ! -d /tmp/hadoop-root/dfs/name/current ]; then
    echo "Formatting NameNode..."
    $HADOOP_HOME/bin/hdfs namenode -format -force
fi


#start hadoop
echo "Starting HDFS..."
$HADOOP_HOME/sbin/start-dfs.sh

#yarn
echo "Starting YARN..."
$HADOOP_HOME/sbin/start-yarn.sh

# Start JobHistory Server
echo "Starting JobHistory Server..."
$HADOOP_HOME/bin/mapred --daemon start historyserver

echo "Hadoop services started successfully!"

#keep the container running
tail -f /dev/null
