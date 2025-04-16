# Use an official Node.js runtime as a parent image
FROM node:16

# Install Python and necessary build tools
RUN apt-get update && apt-get install -y python3 python3-pip
RUN python3 -m pip install --upgrade pip setuptools wheel
RUN python3 -m pip install --no-cache-dir pandas

# Set the working directory in the container
WORKDIR /app

# Copy and install Node.js dependencies first
COPY package*.json /app/
RUN npm install

# Copy Python dependencies and install them
COPY db/requirements.txt /app/
RUN python3 -m pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY db/ /app/
COPY app.py /app/
COPY index.js /app/

# Expose the necessary ports
EXPOSE 5000

# Start the application
CMD ["sh", "-c", "echo 'Starting app...' && python3 app.py"]