# Use official Python slim image
FROM python:3.11-slim

# Set work directory
WORKDIR /app

# Prevent Python from writing pyc files and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy entire project
COPY . /app/

# Create media directory
RUN mkdir -p /app/media

# Expose port for Django
EXPOSE 8000

# Default command to run Django via Gunicorn
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
