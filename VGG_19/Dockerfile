# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Install the required packages
RUN apt-get update && apt-get install -y libsndfile1

# Copy the necessary backend files to the container
COPY app.py  requirements.txt vgg19_model.h5 /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Expose the port for Flask application
EXPOSE 8082

# Command to start the Flask application
CMD ["python", "app.py"]
