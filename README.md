# Machine Learning Pipeline

This repository contains a robust, modular, and scalable machine learning pipeline built using best practices. The project is designed for production use, ensuring flexibility, reusability, and maintainability.

## Table of Contents
- [Project Structure](#project-structure)
- [Key Features](#key-features)
- [Setup Instructions](#setup-instructions)
  - [1. Clone the Repository](#1-clone-the-repository)
  - [2. Create Virtual Environment](#2-create-virtual-environment)
  - [3. Install Dependencies](#3-install-dependencies)
  - [4. Environment Variables](#4-environment-variables)
  - [5. Run the Pipeline](#5-run-the-pipeline)
  - [6. Run the API Server](#6-run-the-api-server)
  - [7. Run Tests](#7-run-tests)
- [Usage](#usage)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```

api/
├── model/
│   ├── __init__.py
│   └── model.py
├── routes/
│   ├── health.py
│   └── predict.py
├── __init__.py
├── main.py
└── utils.py
data/
docs/
models/
notebooks/
src/
├── __init__.py
├── config.py
├── data_ingestion.py
├── evaluation.py
├── logging.py
├── predict.py
├── preprocessing.py
├── training.py
└── utils.py
tests/
├── integration/
│   └── test_pipeline.py
├── unit/
│   ├── __init__.py
│   └── test_data_ingestion.py
├── __init__.py
.env.dev
.env.prod
.gitignore
docker-compose.yml
Dockerfile
dvc.yml
main.py
README.md
```

## Key Features

✅ Modular code design following best practices
✅ Comprehensive unit and integration tests
✅ Supports environment configurations for development and production
✅ Dockerized for seamless deployment
✅ DVC (Data Version Control) for efficient data management
✅ FastAPI for fast and scalable API development

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <repository_url>
cd ml_pipeline
```

### 2. Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate   # For Linux/Mac
.venv\Scripts\activate      # For Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Variables

Copy `.env.dev` or `.env.prod` to `.env` depending on your environment:

```bash
cp .env.dev .env
```

### 5. Run the Pipeline

```bash
python main.py
```

### 6. Run the API Server

```bash
uvicorn api.main:app --reload
```

### 7. Run Tests

```bash
pytest tests/
```

## Usage

* **Training:** Execute `main.py` to run the full pipeline (data ingestion, preprocessing, training, and evaluation).
* **API Endpoints:**
   * `GET /health` - Health check endpoint
   * `POST /predict/` - Make predictions by passing input data in JSON format

## Deployment

To deploy with Docker:

```bash
docker-compose up --build
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License.
