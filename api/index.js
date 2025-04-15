// api/index.js

const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();
const port = 5000;

// MongoDB URI from your Docker compose environment variable
const uri = process.env.MONGO_URI;

async function main() {
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    console.log('Connected to MongoDB');

    // Define a route to get data
    app.get('/data', async (req, res) => {
      try {
        const database = client.db('your_database_name');
        const collection = database.collection('your_collection_name');
        
        // Querying the database
        const data = await collection.find({}).toArray();
        
        // Sending the data to the UI as JSON
        res.json(data);
      } catch (err) {
        console.error(err);
        res.status(500).json({ error: 'Internal server error' });
      }
    });

  } catch (err) {
    console.error(err);
    process.exit(1);
  }
}

main().catch(console.error);

app.listen(port, () => {
  console.log(`API is running on http://localhost:${port}`);
});