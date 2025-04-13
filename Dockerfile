FROM mongo:latest

WORKDIR /app

# Copy necessary files
COPY . /app/

# Expose the MongoDB port (27017)
EXPOSE 27018

# Start the MongoDB server
CMD ["mongod"]
