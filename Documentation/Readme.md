Key Points:

Technologies Used:

Flask: For the web application framework.
PostgreSQL: For the relational database.
Docker: For containerization.
Terraform: For infrastructure as code.
GitHub Actions: For CI/CD pipeline.
Azure Container Instances: To run Docker containers in Azure.
Azure PostgreSQL: Managed PostgreSQL database in Azure.
Tools Needed:

Docker: To build and run containers locally.
Terraform: To manage infrastructure.
Azure CLI: To interact with Azure resources.
Git: For version control.
Python: To run the application.
How to Start This Service from Scratch:
Clone the Repository:


git clone https://github.com/dopicatto/dani_app.git
cd dani_app
Set Up Environment Variables:
Create a .env file with the necessary environment variables:

DB_NAME=exampledb
DB_USER=your_db_user
DB_PASSWORD=your_db_password
DB_HOST=daniapppsqlserver.postgres.database.azure.com
DB_PORT=5432


Build and Run Docker Containers:

docker-compose up --build


Deploy Infrastructure with Terraform:

cd terraform
terraform init
terraform apply -auto-approve -var="db_admin_user=your_db_user" -var="db_admin_password=your_db_password"
Push Changes and Trigger CI/CD Pipeline:
Push changes to the GitHub repository to trigger the CI/CD pipeline which will build and deploy the application.

Additional Documentation:
How to Scale Number of Servers to Take More Load:

To scale the number of servers, you can use Azure Container Instances (ACI) or Azure Kubernetes Service (AKS). AKS is preferable for larger-scale applications because it provides better orchestration capabilities.

Using ACI:
Adjust the terraform/main.tf to increase the number of container instances.

Using AKS:
Deploy the application to an AKS cluster and configure horizontal pod autoscaling based on metrics.