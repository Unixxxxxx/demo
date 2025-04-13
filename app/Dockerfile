# Use the official Python image
FROM python:3.11-slim

# Set the working directory
WORKDIR /app

# Copy project files
COPY requirements.txt requirements.txt
COPY app.py app.py

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 5000

# Run the app
CMD ["python", "app.pygit 