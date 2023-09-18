# Use an official Python runtime as the base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY ./app /app

COPY .env /app

EXPOSE 8000

# Run the application
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers=2"]