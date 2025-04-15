// api/index.js

const express = require('express');
const { MongoClient } = require('mongodb');
const app = express();
const port = 3000; // Changed to a different port from Flask

// MongoDB URI from your Docker compose environment variable
const uri = process.env.MONGO_URI || 'mongodb://mongo:27017';

async function main() {
  const client = new MongoClient(uri, { useNewUrlParser: true, useUnifiedTopology: true });

  try {
    await client.connect();
    console.log('Connected to MongoDB');

    // Endpoint for data processing
    app.get('/processed-data', async (req, res) => {
      try {
        const database = client.db('taxonDB');
        const collection = database.collection('taxonData');
        
        // Retrieve only the dateDiscovered field from the collection
        const data = await collection.find({}, { projection: { _id: 0, dateDiscovered: 1 } }).limit(100).toArray();
        
        // Process the data to form a histogram
        const validDates = data
          .map(entry => entry.dateDiscovered)
          .filter(date => date !== null && !isNaN(date));

        const histogram = createHistogram(validDates);
        
        // Sending the histogram data as JSON
        res.json(histogram);
      } catch (err) {
        console.error('Error processing data:', err);
        res.status(500).json({ error: 'Internal server error' });
      }
    });

    // Function to create a histogram from the date data
    function createHistogram(data) {
      const frequency = {};

      data.forEach(date => {
        if (frequency[date]) {
          frequency[date]++;
        } else {
          frequency[date] = 1;
        }
      });

      return frequency;
    }

  } catch (err) {
    console.error('Failed to connect to MongoDB', err);
    process.exit(1);
  }
}

main().catch(console.error);

app.listen(port, () => {
  console.log(`Node.js API is running on http://localhost:${port}`);
});