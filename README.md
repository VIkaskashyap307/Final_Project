# Course_Project-Option 1

Docker Images
1. Terminal : https://hub.docker.com/r/vikaskashyap307/terminal_project
2. Apache Hadoop Namenode : https://hub.docker.com/r/bde2020/hadoop-namenode
3. Apache Hadooop Datanode : https://hub.docker.com/r/bde2020/hadoop-datanode
4. Apache Spark: https://hub.docker.com/r/bitnami/spark
5. Jupyter Notebook: https://hub.docker.com/r/jupyter/scipy-notebook
6. Sonarqube: https://hub.docker.com/_/sonarqube
7. GUI : https://hub.docker.com/r/vikaskashyap307/terminal_gui

Steps for Docker image creation for terminal
1. docker buildx build -t vikaskashyap307/terminal_project . --platform linux/amd64
2. docker push vikaskashyap307/terminal_project


Steps for Building Apache Hadoop

Namenode

1. 'docker pull bde2020/hadoop-namenode - pulling docker image onto GCP
2. 'docker tag bde2020/hadoop-namenode us.gcr.io/august-charter-327616/hadoop-namenode' - Tag Docker image
3. 'docker push us.gcr.io/august-charter-327616/hadoop-namenode' - Pushing taggged Docker image to GCP
4. Navigate to the docker image in container registry
5. Deploy to GKE, set environment variable as mentioned in https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml corresponding to namenode
6. Set the other 8 environment variables from https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env (first 8)
7. Deploy to the existing Kubernete cluster and set replication to 1 in the YAML file from 3
8. Expose the deployed cluster by giving port as 9870,9870 and 9000,9000 respectively, notedown the service name

Datanode

1. 'docker pull bde2020/hadoop-datanode - pulling docker image onto GCP
2. 'docker tag bde2020/hadoop-datanode us.gcr.io/august-charter-327616/hadoop-datanode' - Tag Docker image
3. 'docker push us.gcr.io/august-charter-327616/hadoop-datanode' - Pushing taggged Docker image to GCP
4. Navigate to the docker image in container registry
5. Deploy to GKE, set environment variable as mentioned in https://github.com/big-data-europe/docker-hadoop/blob/master/docker-compose.yml corresponding to datanode
6. Set the other 8 environment variables from https://github.com/big-data-europe/docker-hadoop/blob/master/hadoop.env (first 8)
7. Deploy to the existing Kubernete cluster (as load balancer) and set replication to 2 in the YAML file from 3
8. Change the value of SERVICE_Protection to namenode-service-name:9000 
9. Change the value of CORE_CONF_fs_defaultFS to hdfs://namenode-service-name:9000 
10. Wait for a couple of minutes for the datanodes to show up in the namenode service
 

Steps for Docker and Kubernetes Orchestration on Google Cloud

1. 'gcloud config set project august-charter-327616' - Setting project directory
2. 'docker pull bitnami/spark' - pulling docker image onto GCP
3. 'docker tag spark us.gcr.io/august-charter-327616/spark - Tag Docker Image
4. 'docker push us.gcr.io/august-charter-327616/spark' - Pushing tagged Docker image to GCP
5. 'gcloud config set compute/zone us-central1-a' - set the zone for the kubernetes cluster
6. 'gcloud container clusters create kube-cluster --num-nodes=3' - Create the Kubernetes Cluster
7. 'gcloud container clusters get-credentials kube-cluster' - Enable kubectl to use the cluster 
8. 'kubectl create deployment spark --image=us.gcr.io/august-charter-327616/spark' - Create the Kubernetes deployment
9. 'kubectl expose deployment spark --type LoadBalancer --port 8080 target-port 6004' - Expose the deployment with an IP

Repeat same steps except steps 5,6,7 for all other services.

Terminal Application 
1. 'kubectl run -i --tty terminal-app --image=vikaskashyap307/terminal_project' - Runs the terminal application
 
GUI

1. GUI Files are present in the GUI folder
 
   1.1 It contains the template folder having the template.html file
 
   1.2 It contains the Dockerfile, requirements.txt file and the app.py file

2. Need to specify port as 6007:9880 while exposing the GUI service
