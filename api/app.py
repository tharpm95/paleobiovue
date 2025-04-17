from flask import Flask, jsonify
from flask_cors import CORS
import os
from pymongo import MongoClient
from dotenv import load_dotenv
import sys
from collections import Counter

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load environment variables
load_dotenv()

# Append the full path to the `db` directory inside the container
sys.path.append('/app/db')

def load_initial_data():
    """Function to directly access the file inside `/app/db`."""
    try:
        from insert_taxon import main
        main()
    except ModuleNotFoundError as e:
        print("Error loading the `insert_taxon` module:", e)

def get_mongo_data():
    """Connects to MongoDB, retrieves and processes data counts for histogram."""
    try:
        # Retrieve the MongoDB URI from environment variables
        mongo_uri = os.getenv('MONGO_URI')
        
        # Create a MongoDB client and connect to the specified database
        client = MongoClient(mongo_uri)
        db = client['taxonDB']  # Use your database name
        collection = db['taxonData']  # Use your collection name

        # Fetch data from the collection
        data = collection.find({}, {"_id": 0, "dateDiscovered": 1})
        
        # Count occurrences of each `dateDiscovered`, ignoring null values
        year_counter = Counter(record["dateDiscovered"] for record in data if record["dateDiscovered"] is not None)
        
        # Convert Counter object to dictionary
        return dict(year_counter)

    except Exception as e:
        print(f"Error fetching data from MongoDB: {e}")
        return None

@app.route('/')
def home():
    return "API is running!"

@app.route('/data', methods=['GET'])
def get_data():
    try:
        # Fetch and process data from MongoDB for histogram
        data = get_mongo_data()
        if data is None:
            return jsonify({"error": "Failed to retrieve data"}), 500
        
        # Return the data as JSON
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    load_initial_data()  # Run the data loading script before starting the server
    app.run(host='0.0.0.0', port=5000)