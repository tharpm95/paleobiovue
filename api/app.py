from flask import Flask, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def load_initial_data():
    """Function to run insert_taxon logic at server start."""
    from db.insert_taxon import main
    main()

@app.route('/')
def home():
    return "API is running!"

@app.route('/data')
def get_data():
    try:
        mongo_uri = os.getenv("MONGO_URI", "mongodb://mongo:27017/")
        client = MongoClient(mongo_uri)
        db = client['taxonDB']
        collection = db['taxonData']

        # Fetch data from MongoDB
        data = list(collection.find({}, {'_id': 0}))  # Project out MongoDB IDs, return all other fields

        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    load_initial_data()  # Run the data loading script before starting the server
    app.run(host='0.0.0.0', port=5000)