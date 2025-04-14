# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy the necessary files for the API
COPY db/requirements.txt ./

# Install API dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the working directory
COPY /db/ .

# Expose the API's port
EXPOSE 5000

# Command to run your API app
CMD ["python", "db/insert_taxon.py"]