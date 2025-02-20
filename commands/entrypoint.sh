#!/bin/sh

# Run the McDonald's spider
echo "Running McDonald's spider..."
# shellcheck disable=SC2164
cd /app/mcdonalds_scraper
scrapy crawl mcdonald

# Run the web server
echo "Running web server..."
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload --reload-dir /app/mcdonalds_scraper
