# JupyterLab + Python + NumPy + Pandas (Docker Environment)
This project provides a fully containerized Python environment using Docker. It includes:

- Python 3.11
- JupyterLab
- NumPy
- Pandas

Automatic mounting of a Windows directory for persistent notebooks

Custom external port (8887)

No Python installation required on the host machine

The environment is designed for local development on Windows while keeping all dependencies isolated inside Docker.

## Project Structure
```Code
project-root/
│
├── JupiterLab
├─── Dockerfile
├─── requirements.txt
└── docker-compose.yml
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
docker compose up --build
```