FROM python:3.12-slim
WORKDIR /app
COPY requirements.ini .
RUN pip install --no-cache-dir -r requirements.ini
COPY . .
CMD ["python", "app.py"]
