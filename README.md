![CI](https://github.com/YARAGANIDURGADHANUSH/cloud-devsecops-pipeline/actions/workflows/ci.yml/badge.svg)

# Cloud-Based Secure DevOps Pipeline for Software Development

## Architecture Diagram
![DevSecOps Architecture](https://raw.githubusercontent.com/YARAGANIDURGADHANUSH/cloud-devsecops-pipeline/main/DevSecOps_Architecture_Diagram.png)

## Project Highlights
- ✅ CI/CD automation using GitHub Actions
- ✅ Dockerized Python (Flask) application for consistent deployments
- ✅ Security scanning using Trivy (HIGH/CRITICAL)
- ✅ Trivy JSON report generated and uploaded as an artifact
- ✅ Job Summary prints vulnerability counts and fails build on CRITICAL issues

![Docker PS](screenshots/docker-ps.jpg)
![EC2 Instance](screenshots/ec2-instance.jpg)
![GitHub Actions](screenshots/github-actions.jpg)


## CI Workflow (GitHub Actions)
On every push/PR to `main`, the pipeline:
1. Installs dependencies
2. Runs a basic Flask import test
3. Builds the Docker image
4. Scans the image using Trivy
5. Uploads Trivy JSON report as an artifact
6. Shows HIGH/CRITICAL summary and fails if CRITICAL > 0

## Resume Bullet Points
- Built a cloud-ready DevSecOps CI pipeline using GitHub Actions to automate testing, Docker builds, and vulnerability scanning.
- Integrated Trivy scanning with JSON artifact reports and automated security gate to fail builds on CRITICAL vulnerabilities.
- Documented architecture and workflow to support reproducible deployments and audit-ready security validation.


This project demonstrates a secure CI/CD pipeline using GitHub Actions, Docker, and vulnerability scanning.

## Tech Stack
- Python (Flask)
- Docker
- Git & GitHub
- GitHub Actions (CI)
- Trivy (Image vulnerability scanning)

## Pipeline Flow
1. Code push / PR triggers GitHub Actions
2. Dependencies are installed
3. Basic test runs
4. Docker image is built
5. Trivy scan checks HIGH/CRITICAL vulnerabilities

## Run Locally
```bash
docker build -t devsecops-pipeline .
docker run -p 5000:5000 devsecops-pipeline

## Deployment (AWS Ready)
This project is designed to be cloud-ready and can be deployed on:
- AWS EC2 (Docker container)
- AWS ECS Fargate (recommended)
- Kubernetes (EKS)

### Example: Run on any Linux server (EC2)
```bash
docker pull <your-image>
docker run -d -p 80:5000 <your-image>

