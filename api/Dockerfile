# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY db/requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code to the working directory
COPY db/ /app/

# Copy the new app.py file
COPY app.py /app/

# Expose the API's port
EXPOSE 5000

# Command to run Flask
CMD ["python", "app.py"]