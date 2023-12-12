# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Create and set the working directory
WORKDIR /app

# Copy frontend files into the container
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port on which the Flask application will run
EXPOSE 8083

# Command to run the Flask application
CMD ["python", "app.py"]
