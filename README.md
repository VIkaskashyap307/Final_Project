# Final_Project-Checkpint 1

Docker Images
1. Terminal : https://hub.docker.com/r/vikaskashyap307/terminal
2. Apache Spark: https://hub.docker.com/r/bitnami/spark
3. Jupyter Notebook: https://hub.docker.com/r/jupyter/scipy-notebook
4. Sonarqube: https://hub.docker.com/_/sonarqube

Commands for Docker image creation for terminal
1. docker buildx build -t vikaskashyap307/terminal . --platform linux/amd64
2. docker push vikaskashyap307/terminal

Docker and Kubernetes commands on Google Cloud

1. 'gcloud config set project august-charter-327616' - Setting project directory
2. 'docker pull bitnami/spark' - pulling docker image onto GCP
3. 'docker tag spark us.gcr.io/august-charter-327616/spark - Tag Docker Image
4. 'docker push us.gcr.io/august-charter-327616/spark' - Pushing tagged Docker image to GCP
5. 'gcloud config set compute/zone us-central1-a' - set the zone for the kubernetes cluster
6. 'gcloud container clusters create kube-cluster --num-nodes=3' - Create the Kubernetes Cluster
7. 'gcloud container clusters get-credentials kube-cluster' - Enable kubectl to use the cluster 
8. 'kubectl create deployment spark --image=us.gcr.io/august-charter-327616/spark' - Create the Kubernetes deployment
9. 'kubectl expose deployment spark --type LoadBalancer --port 8080 target-port 6004' - Expose the deployment with an IP

Terminal Application 
1. 'kubectl run -i --tty terminal-app --image=vikaskashyap307/terminal' - Runs the terminal application
