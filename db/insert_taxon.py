import os
import re
import pandas as pd
from pymongo import MongoClient
from dotenv import load_dotenv

def load_taxon_data_to_dataframe(file_path):
    """Loads taxon data from a file and returns it as a Pandas DataFrame."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist. Make sure you are in the correct directory.")
        return None

    try:
        dataframe = pd.read_csv(file_path, sep='\t')
        return dataframe
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def preprocess_dataframe(df):
    """Adds a 'dateDiscovered' column by extracting the date from 'scientificNameAuthorship'."""
    if 'scientificNameAuthorship' in df:
        # Use a regex pattern to find the first sequence of four digits in 'scientificNameAuthorship'
        df['dateDiscovered'] = df['scientificNameAuthorship'].apply(
            lambda x: re.search(r'\b(\d{4})\b', x).group(1) if pd.notnull(x) and re.search(r'\b(\d{4})\b', x) else None
        )
    else:
        df['dateDiscovered'] = None
        print("'scientificNameAuthorship' column not found in the DataFrame.")

    return df

def insert_dataframe_to_mongo(df, db_name, collection_name, mongo_uri="mongodb://localhost:27018/"):
    """Insert a DataFrame into a MongoDB collection."""
    if df is None:
        print("No data to insert.")
        return

    try:
        # Connect to the MongoDB server
        client = MongoClient(mongo_uri)

        # Access the database
        db = client[db_name]

        # Access the collection
        collection = db[collection_name]

        # Clear existing data in the collection
        collection.delete_many({})
        print(f"Cleared existing records in the '{collection_name}' collection of the '{db_name}' database.")

        # Convert DataFrame to a list of dictionaries
        data_dict = df.to_dict("records")

        # Insert data into the collection
        collection.insert_many(data_dict)

        print(f"Inserted {len(data_dict)} records into the '{collection_name}' collection of the '{db_name}' database.")
    except Exception as e:
        print(f"An error occurred while inserting data into MongoDB: {e}")

def main():
    # Load environment variables
    load_dotenv()

    # Get the main directory from environment variable
    main_dir = os.getenv('MAIN_DIR')
    if not main_dir:
        print("Environment variable MAIN_DIR not set.")
        return

    # Change to the main directory
    try:
        os.chdir(main_dir)
        print(f"Changed working directory to {main_dir}.")
    except Exception as e:
        print(f"Unable to change directory to {main_dir}: {e}")
        return

    # Define paths for the taxon files
    taxon_part1_path = 'data/taxon_part1.tab'
    taxon_part2_path = 'data/taxon_part2.tab'
    
    # Load the taxon data into Pandas DataFrames
    taxon_part1_df = load_taxon_data_to_dataframe(taxon_part1_path)
    taxon_part2_df = load_taxon_data_to_dataframe(taxon_part2_path)

    # Check if dataframes were loaded successfully
    if taxon_part1_df is not None and taxon_part2_df is not None:
        # Concatenate both DataFrames
        combined_df = pd.concat([taxon_part1_df, taxon_part2_df], ignore_index=True)
        
        # Preprocess the DataFrame to add 'dateDiscovered'
        processed_df = preprocess_dataframe(combined_df)

        print("Processed Taxon DataFrame:")
        print(processed_df)

        # Insert the processed DataFrame into MongoDB
        insert_dataframe_to_mongo(processed_df, db_name="taxonDB", collection_name="taxonData")
    else:
        print("Failed to load one or more DataFrames.")

if __name__ == '__main__':
    main()