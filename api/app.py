from flask import Flask, jsonify
from flask_cors import CORS
import subprocess
import sys

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Append the full path to the `db` directory inside the container
sys.path.append('/app/db')

def load_initial_data():
    """Function to directly access the file inside `/app/db`."""
    try:
        from insert_taxon import main
        main()
    except ModuleNotFoundError as e:
        print("Error loading the `insert_taxon` module:", e)

@app.route('/')
def home():
    return "API is running!"

@app.route('/data', methods=['GET'])
def get_data():
    print('hello')
    try:
        # Call the Node.js script
        result = subprocess.run(['node', 'index.js'], capture_output=True, text=True)
        if result.returncode != 0:
            return jsonify({"error": result.stderr}), 500

        # Parse and return the output from the Node.js script
        data = result.stdout.strip()  # Strip any extraneous newlines or spaces
        return jsonify({"data": data})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    load_initial_data()  # Run the data loading script before starting the server
    with app.app_context():
        # Call get_data within application context
        response_from_endpoint, status_code = get_data()
        # Extract JSON data from response
        response_data = response_from_endpoint.get_json()
        print(response_data)
    app.run(host='0.0.0.0', port=5000)