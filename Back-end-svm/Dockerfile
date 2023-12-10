# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app
# Install the required packages
#RUN apt-get update && apt-get install -y libsndfile1

# Copy the necessary backend files to the container
COPY app.py modeltest.pkl requirements.txt scalertest.pkl /app/

# Install any needed packages specified in requirements.txt
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

# Expose the port used by your Flask application
EXPOSE 8081

# Define environment variable for Flask to run in production mode
ENV FLASK_ENV=production

# Command to start the application
CMD ["python", "app.py"]
