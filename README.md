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
    * sleep for 30 seconds while the database starts up.
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

## 2Q-Cloud_App_Architecture

![Image_of_Q2](https://github.com/tianyang98/Assignment_Tian_Yang/blob/master/image_of_Q2.png)

### 1.Explain the Architecture model of this and the Benefit

This architecture model is a combination of __Content Deliver Networks(CDN)__ and __Load Balancing__. 

CDN is simply a network of servers used to deliver content. Servers are distributed throughout various global locations. When a user requests a resource or content,  it call the contents from the server that is closest to the requesting user. This increases the speed at which the content is delivered to end users by __decreasing the distance__ the information must travel and thus __reducing latency__.

Load balancing is the automatic process of distributing workloads across multiple servers. It ensures that requests for an application or data are spread evenly across the network of servers that hosts the application or data, and ensures uptime by redirecting traffic to another server in the event that one server goes down. It can improve service availability and __prevent any single server from getting overloaded and possibly breaking down__.

A load balancer will let you distribute your application across a cluster of servers while CDN will help you optimize the experience of end-users in disparate geographic regions. In other words, CDN provides a platform for delivering large amounts of content __closer__ to the end user, while load balancing allows for easily __scaling resources__ for applications. Using both two strategies together creates a more resilient and reliable delivery strategy for your applications and content than either could do alone. They eliminate single points of failure in delivering applications and the content that power them, while making smart, efficient use of resources.

### 2.How do you roll out an update to the service without any downtime impact to the app foo.com

Generally, for availability, users of your web service will hit it via a load balancer which then routes requests to a pool of instances of the application. This means __if one instance falls over__, you have availability because __the load balancer will just send the traffic to the instances that are working__. For that reason, when you deploy, you can take down one instance, upgrade, then another, etc, until they are all updated. During this you will always have at least one running.

### 3.If you have to deploy this App to the Cloud what services would you use and explain the Architecture. You can mention for Cloud of your choice (Google Cloud Platform).

Google Cloud provides hybrid networking portfolio with Cloud CDN and Load Balancing.

![Image_GCP](https://github.com/tianyang98/Assignment_Tian_Yang/blob/master/GCP_model.png)

It is based on new internet network endpoint groups (NEG), which allows you to configure a publicly addressable endpoint. From there, you can serve content via Cloud CDN, or serve API traffic via an external HTTP(S) Load Balancer.

With this configuration, requests are proxied by the HTTP(S) load-balancer to services running on Google Cloud or other clouds to the services running in your on-prem locations that are configured as an internet NEG backend to your load-balancer. 


## 3Q-Data_Pipeline_with_Python



### Reference: 
 1. https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash
 2. https://www.softwaredeveloper.blog/initialize-mssql-in-docker-container
 3. https://jelecos.com/cloud-resources/important-apply-load-balancing-cloud-environment/
 4. https://www.inap.com/blog/cdn-versus-cloud-computing-whats-difference-do-i-need-both/
 5. https://victorops.com/blog/cdns-vs-load-balancers-for-uptime-and-user-experience
 6. https://dev.to/nektro/how-do-you-update-backend-web-services-without-downtime-2k7f
 7. https://cloud.google.com/blog/products/networking/enabling-hybrid-deployments-with-cloud-cdn-and-load-balancing
 

