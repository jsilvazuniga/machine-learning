FROM python:3.11-slim

WORKDIR /workspace

# Optional: system tools for scientific libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy external requirements file
COPY requirements.txt .

# Install all Python dependencies (JupyterLab included)
RUN pip install --no-cache-dir -r requirements.txt

COPY ./src ./src

EXPOSE 5678

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]


# docker build -t fastapi-image .

# docker run --name fastapi-container -p 8885:80 fastapi-image

# linux env
# docker run --name fastapi-container -p 8885:80 -d -v $(pwd):/workspace fastapi-image

# windows env
# docker run --name fastapi-container -p 8885:80 -d -v "%cd%":/workspace fastapi-image

