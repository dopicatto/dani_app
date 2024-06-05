# Dani App

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Development](#development)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Introduction
Dani App is a web application built with Flask and deployed using Docker and Terraform. It uses a PostgreSQL database and is designed to run in an Azure cloud environment.

## Features
- Web application using Flask
- PostgreSQL database integration
- Dockerized application for containerized deployment
- Infrastructure management using Terraform

## Installation
### Prerequisites
- Docker
- Docker Compose
- Terraform
- Python 3.x
- pip

### Steps
1. Clone the repository:
   ```
   bash
   git clone https://github.com/yourusername/dani-app.git
   cd dani-app
   ```

2. Create a virtual environment and activate it:
   ```
   bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required Python packages:
   ```
   bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `.env` file in the root directory and add your environment variables:
   ```
   bash
   cp .env.example .env
   ```

2. Modify the `.env` file with your configuration details.

## Usage
1. To run the application locally:
   ```
   bash
   flask run
   ```

2. Access the application at `http://localhost:5000`.

## Development
### File Structure
- `app.py`: Main application file
- `requirements.txt`: Python dependencies
- `import_resources.sh`: Shell script for importing resources into Terraform
- `docker-compose.yml`: Docker Compose configuration
- `Dockerfile`: Docker image configuration
- `main.tf`: Terraform configuration for infrastructure
- `variables.tf`: Terraform variables

### Running with Docker
1. Build the Docker image:
   ```
   bash
   docker build -t dani-app .
   ```

2. Run the Docker container:
   ```
   bash
   docker-compose up
   ```

### Infrastructure Management with Terraform
1. Initialize Terraform:
   ```
   bash
   terraform init
   ```

2. Apply the Terraform configuration:
   ```
   bash
   terraform apply
   ```

## Deployment
1. Ensure all configurations in `main.tf` and `variables.tf` are set correctly.
2. Use the `import_resources.sh` script to import existing resources into Terraform state:
   ```
   bash
   ./import_resources.sh
   ```
3. Apply Terraform configuration:
   ```
   bash
   terraform apply
   ```

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License
This project is licensed under the MIT License.

---

This README file provides a comprehensive overview of your project, including installation, configuration, usage, and development instructions.