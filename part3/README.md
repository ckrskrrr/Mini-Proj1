# Build the image
docker build -t hadoop-docker .

# Rememeber to cd to the project directory before running the ccontainer.
# Otherwise the volume will not be mounted correctly.
docker run -it -p 9870:9870 -p 8088:8088 --name hadoop-container -v "$PWD":/project hadoop-docker

# Check the hadoop processes
docker exec -it hadoop-container jps

# Enter into the container
docker exec -it hadoop-container bash

# Cd to part3 folder
cd /project/part3

# Add the execute permission to run.sh
chmod +x run.sh

# Execute the script to get the result for q1 to q5 :)
./run.sh
