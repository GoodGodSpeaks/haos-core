# Base image with Python 3.12
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /haos

# Copy and install Python requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy all files from host into container
COPY . .

# Default test command to validate full agent flow
CMD ["pytest", "tests"]
