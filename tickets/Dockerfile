# Use an Alpine-based Python image
FROM python:3.10-alpine

# Set working directory inside the container
WORKDIR /app

# Install system dependencies
RUN apk update \
    && apk add --no-cache \
        gcc \
        musl-dev \
        libffi-dev \
        openssl-dev \
        python3-dev \
    && rm -rf /var/cache/apk/*

# Install pipenv for managing dependencies
RUN pip install --no-cache-dir pipenv

# Copy the Pipfile and Pipfile.lock into the container
COPY Pipfile* ./

# Install FastAPI and other dependencies using pipenv
RUN pipenv install --system --deploy

# Copy your FastAPI app code into the container
COPY . .

# Expose the port on which FastAPI will run (change it to your desired port)
EXPOSE 8000

# Command to run the FastAPI server using uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
