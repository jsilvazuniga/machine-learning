# Docker Labs: Datasience Machine Learning 

## 1. DataSciente environnement
This project creates a fully containerized Python environment using Docker, running **JupyterLab with NumPy and Pandas preinstalled**. It mounts your Windows notebook directory into the container so all your work stays on your PC. It provides a reproducible, isolated workspace accessible through your browser on port **8887**.

## 2. Machine Learning as a Service

This directory contains a collection of practical labs focused on building and deploying applications using Docker. The projects combine **Flask** as a lightweight web framework and **Machine Learning models** exposed as REST APIs. The goal is to provide a simple environment for experimenting with containerization, API deployment, and basic MLOps concepts.

### Objectives
- Build small web services using Flask.
- Expose Machine Learning models as API endpoints.
- Create reproducible Docker images for each lab.
- Run and test containers locally.
- Explore foundational MLOps practices.

### Repository Structure
- **Flask/** — Flask service exposing test.
- **Flask-ML-Scoring/** — Flask service exposing a scoring model.
- **Flask-ML-Sentimiento/** — Sentiment analysis API using logistic regression.
