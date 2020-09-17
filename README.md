## Clone demo for the first time

First, create a folder on your host and then git clone this project into that folder:

```
git clone https://github.com/tianyang98/Assignment_Tian_Yang
```

## 1Q-Docker_Image_with_SQL

For the 1st question, we enter this directory and run `setup.bash` to do all the work automatically.

```
source ./setup.bash
```

To explain in detail, 
* We build the Docker Image by __Dockerfile__, tag it as db-demo
  * Download the Docker Image as `mcr.microsoft.com/mssql/server:2017-CU17-ubuntu`
  * Create DBScripits directory
  * Grant permissions for run-initialization script 
    * it runs a sqlcmd that calls scripts to create the DB and the schema in the DB: 
     ```
     01-create-database.sql
     02-create-table.sql
     03-insert-data.sql
     ```
  * Set environment variables
    * set SA_PASSWORD = CorrectPasswordForVisualBI$
    
  * entrypoint.sh — script ran at startup that simply runs irun-initialization.sh and starts the SQL Server.
  
* Run the container and set '-p 1433:1433' to ensure that __SQL Server is listening on TCP 1433 in the container and this is exposed to the port, 1433, on the host.__

* Then we can connect to the SQL Server with SQL Server Management Studio (SSMS). Provide localhost as Server name. Choose SQL Server Authentication and provide sa user with password from Dockerfile.

## 2Q-Cloud_App_Archetecture

## 3Q-Data_Pipeline_with_Python
