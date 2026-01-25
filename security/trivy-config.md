# Trivy Scan Notes

This project uses Trivy inside GitHub Actions to scan Docker images.

Command used:
trivy image --severity HIGH,CRITICAL devsecops-pipeline:latest

Pipeline should fail if HIGH or CRITICAL vulnerabilities are found.
