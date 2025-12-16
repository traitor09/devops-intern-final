# DevOps Intern Final Assessment 🙌
**Name:** Divyanshi Pathak   
**Date:** 16-12-2025
## Description
This repository contains the final DevOps Intern assessment and presents a full DevOps workflow featuring:  
- Linux scripting
- Docker containerization 
- GitHub Actions–based CI/CD
- Nomad job deployment
- Grafana Loki monitoring
## Prerequisites
To run, install the following-  
### macOS Installation (via Homebrew)

**1. Docker**
```bash
brew install --cask docker
# Open Docker Desktop from Applications to start the daemon
open /Applications/Docker.app
```

**2. Nomad**
```bash
brew tap hashicorp/tap
brew install hashicorp/tap/nomad
# Verify installation
nomad --version
```

## Steps to Run

### 1. Python Script
Run sample python script:
```bash
python hello.py
```

### 2. Linux Script
Run the system info script:
```bash
./scripts/sysinfo.sh
```

### 3. Docker
Build and run the container:
```bash
docker build -t devops-intern-hello .
docker run devops-intern-hello
```

### 4. Nomad
Run the job [Ensure you have Nomad installed and running]:
```bash
nomad job run nomad/hello.nomad
```

### 5. Monitoring
See `monitoring/loki_setup.txt` for instructions on setting up & using Grafana Loki.

### 6. MLFlow
Run the MLFlow experiment inside the container:
```bash
# Rebuild image
docker build -t devops-intern-hello .

# Run experiment script
docker run devops-intern-hello python mlflow/experiment.py
```
