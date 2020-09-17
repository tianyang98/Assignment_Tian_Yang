#!/bin/bash
# This is a setup bash for docker containers!
# activate via: chmod 0755 setup_bash or chmod +x setup_bash
# navigate to wd docker_contents
# excute in terminal via source ./setup_bash

echo "===== Build the image. ====="

docker build -t db-demo .

echo "===== Run the container. ====="

docker run -p 1433:1433 -d db-demo --name sql1 -h sql1

#Then we can connect to the SQL Server with SQL Server Management Studio (SSMS).
#Provide localhost as Server name. Choose SQL Server Authentication and provide sa user with password from Dockerfile.

