FROM python:3.11-slim

# WORKDIR /workspace

# Optional: system tools for scientific libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy external requirements file
COPY requirements.txt .

# Install all Python dependencies (JupyterLab included)
RUN pip install --no-cache-dir -r requirements.txt

# Create symlinks in /root so JupyterLab shows your volumes in the main view
RUN ln -s /workspace /root/workspace \
    && ln -s /workspace_repoML /root/repoML \
    && ln -s /workspace-temps /root/temps

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--no-browser", "--allow-root"]
