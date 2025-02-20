
# Udata-TestTask-FoodProducts

## Overview

This repository contains a solution for scraping McDonald's menu data and exposing it via a FastAPI backend. The backend allows users to interact with the data through various API endpoints. 

The task is to scrape product data, including nutritional information, and make it available for querying via an API.

## Features

- **Scraping**: Data is scraped from the McDonald's menu.
- **API**: FastAPI server exposes the scraped data via various endpoints.
- **Docker**: The project can be run both locally and in a Docker container.

## Getting Started

These instructions will help you run the project locally or using Docker Compose.

### Requirements

- **Python 3.12** or higher
- **Docker** and **Docker Compose**
- **Scrapy** for web scraping
- **FastAPI** for the backend API
- **Uvicorn** for serving FastAPI

### Running Locally

#### 1. Clone the repository:

```bash
git clone https://github.com/molodsh1y1/Udata-TestTask-FoodProducts.git
```

#### 2. Install dependencies:

Create a virtual environment and install the required dependencies.

```bash
python -m venv .venv
source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
pip install -r requirements/dev.txt
```

#### 3. Run the scraper:

The scraper can be run manually using Scrapy. To do this, navigate to the `mcdonalds_scraper` directory and execute:
```bash
cd mcdonalds_scraper
```

Then run the scraper using the following command:
```bash
scrapy crawl mcdonald
```

This will scrape the data from the McDonald's menu and store it in a predefined location.

#### 4. Start the API:

After scraping the data, run the FastAPI server:

```bash
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload
```

The API will now be accessible at `http://127.0.0.1:8000`.

### Running with Docker Compose

You can also run the entire application using Docker Compose, which will handle both the web server and the scraping process.

#### 1. Build and start the containers:

```bash
docker-compose up --build
```

#### 2. Access the application:

Once the containers are up and running, the API will be available at `http://localhost:8000`. You can check the Swagger UI at `http://localhost:8000/docs` to interact with the API.

### Available Endpoints

- **GET `/products/`**: Fetch a list of all products from the menu.
- **GET `/products/{product_name}/`**: Get details of a specific product by name.
- **GET `/products/{product_name}/{product_field}/`**: Get a specific field of a product by name (e.g., `calories`, `carbs`).
