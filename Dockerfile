FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src/

# Eğer host'taki uploads/ klasörü varsa:
COPY uploads/ ./uploads/
# Eğer yoksa oluştur:
RUN mkdir -p uploads

WORKDIR /app/src

CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:8080", "app:app"]