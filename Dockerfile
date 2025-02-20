FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

# Copy the dependencies file
COPY requirements/ requirements/

# Install Python dependencies
RUN pip install -r requirements/base.txt

# Copy the source code
COPY . .

EXPOSE 8000

CMD uvicorn mcdonalds_scraper.api.main:app --reload --host 0.0.0.0
