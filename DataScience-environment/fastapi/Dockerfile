FROM python:3.11-slim

WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn[standard] mlflow[extras] pandas scikit-learn

COPY . /app

CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]
