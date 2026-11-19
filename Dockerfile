FROM python:3.11-slim

# System deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    portaudio19-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Install Python deps first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

EXPOSE 8000

CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "8000"]
