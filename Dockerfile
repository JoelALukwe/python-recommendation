FROM python:3.9-slim

WORKDIR /app
COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    && mkdir -p /app/models

CMD ["uvicorn", "app.api:app", "--host", "0.0.0.0", "--port", "8000"]
