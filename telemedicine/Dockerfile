FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
# Disable progress bar and use simpler installation
RUN pip install --no-cache-dir --upgrade pip --progress-bar off && \
    pip install --no-cache-dir -r requirements.txt --progress-bar off
COPY app.py .
EXPOSE 5000
CMD ["python", "app.py"]