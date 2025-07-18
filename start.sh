#!/usr/bin/env bash

echo "Running Alembic migrations..."
alembic upgrade head

echo "Starting FastAPI app..."
uvicorn app.main:app --host=0.0.0.0 --port=10000

