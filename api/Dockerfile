# Use an official Python runtime as a parent image
FROM python:3.9

# Install Node.js
RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs

# Set the working directory in the container
WORKDIR /app

# Copy and install Python dependencies
COPY db/requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python app code
COPY db/ /app/
COPY app.py /app/

# Copy the Node.js app code
COPY index.js /app/

# Expose the necessary ports
EXPOSE 5000

# Command to run Flask
CMD ["python", "app.py"]