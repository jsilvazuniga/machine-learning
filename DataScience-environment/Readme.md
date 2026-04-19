# JupyterLab + Python + NumPy + Pandas (Docker Environment)
This project provides a fully containerized Python environment using Docker. It includes:

- Python 3.11
- JupyterLab
- NumPy
- Pandas

# MLflow + JupyterLab + FastAPI stack

## 🇬🇧 Overview

This repository provides a reproducible environment for:

- Experiment tracking with **MLflow** (PostgreSQL backend, artifact store on volume)
- Interactive development with **JupyterLab**
- Model serving with **FastAPI** using MLflow models

The stack is orchestrated with **Docker Compose** and is suitable as a solid starting point for production-like workflows.

---

## 🇬🇧 Architecture

- **JupyterLab**  
  Interactive notebooks for experimentation, training, and logging runs to MLflow.

- **PostgreSQL**  
  MLflow backend store for runs, metrics, parameters, and model registry.

- **MLflow server**  
  Central tracking server and model registry, exposing the UI on port `5000`.

- **FastAPI**  
  Lightweight API layer to serve MLflow models in real time.

---

## 🇬🇧 Prerequisites

- Docker
- Docker Compose
- Environment variables (example):
  - `WORKSPACE_DIR`
  - `REPO_DIR`
  - `TEMP_DIR`

---

## 🇬🇧 How to run

```bash
docker compose up --build


Automatic mounting of a Windows directory for persistent notebooks

Custom external port (8887)

No Python installation required on the host machine

The environment is designed for local development on Windows while keeping all dependencies isolated inside Docker.

## Project Structure
```Code
project/
│
├── docker-compose.yml
├── .env
├── JupyterLab/
│   ├── Dockerfile
│   └── requirements.txt
│
├── workspace/          ← código activo
├── repoML/             ← repositorios o datasets
└── temps/              ← archivos temporales
```
### Your actual notebooks live in your Windows directory:

```Windows
D:\Users\<USER>\Documents\MyDocsPersonales\myJupyterFiles\

Your Windows folder is mounted into /workspace inside the container.
```
This folder is mounted into the container at /workspace.

> [!NOTE]
>- JupyterLab runs internally on port 8888, mapped to 8887 on Windows.
>- Your Windows folder is mounted into /workspace inside the container.
>- All notebooks and data remain on your PC.

---
## Running the Environment
### 1. Open PowerShell or CMD
Navigate to the project folder:

```powershell
cd path\to\project-root
```
### 2. Build and start the environment
```powershell
docker compose up --build
```
### 3. Open JupyterLab
Copy the URL shown in the terminal and open:

```Code
http://localhost:8887/lab
```
JupyterLab will open in your browser.

---

## Working With Your Files
Inside JupyterLab, your notebooks appear under:

```Code
/workspace
```
These files correspond directly to your Windows folder:

```Code
D:\Users\<USER>\Documents\MyDocsPersonales\myJupyterFiles
```
Any changes you make in JupyterLab are saved on your PC.
If you need to modify your workspace root path, you can do it from docker-compose.yml

---

## Stopping the Environment
Press CTRL + C in the terminal, then:

```powershell
docker compose down
```
## Updating Dependencies
To add new Python libraries:

Edit requirements.txt

Rebuild the container:

```powershell
docker compose build --no-cache
docker compose up -d

```