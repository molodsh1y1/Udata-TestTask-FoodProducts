FROM python:3.11-slim AS base

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app/mcdonalds_scraper

# Create a non-root user and set the home directory to /app
RUN adduser --disabled-password --gecos "" --home "/app" --shell "/sbin/nologin" --no-create-home appuser

# Set the user to 'appuser'
USER appuser

WORKDIR /app

# Install system dependencies as root
USER root
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

# Ensure the copied entrypoint script is executable
COPY commands/ commands/
RUN chmod +x commands/entrypoint.sh

# Set the user back to 'appuser' for running the application
USER appuser
