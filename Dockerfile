FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/mcdonalds_scraper

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

COPY commands/ commands/

RUN chmod +x commands/entrypoint.sh
