import os
import pandas as pd

def load_taxon_data_to_dataframe(file_path):
    """Loads taxon data from a file and returns it as a Pandas DataFrame."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None

    try:
        dataframe = pd.read_csv(file_path, sep='\t')
        return dataframe
    except Exception as e:
        print(f"An error occurred while reading {file_path}: {e}")
        return None

def main():
    # Define paths for the taxon files
    taxon_part1_path = os.path.join('data', 'taxon_part1.tab')
    taxon_part2_path = os.path.join('data', 'taxon_part2.tab')
    
    # Load the taxon data into Pandas DataFrames
    taxon_part1_df = load_taxon_data_to_dataframe(taxon_part1_path)
    taxon_part2_df = load_taxon_data_to_dataframe(taxon_part2_path)

    # Check if dataframes were loaded successfully
    if taxon_part1_df is not None and taxon_part2_df is not None:
        # Concatenate both DataFrames
        combined_df = pd.concat([taxon_part1_df, taxon_part2_df], ignore_index=True)
        print("Combined Taxon DataFrame:")
        print(combined_df)

        # List all unique values in the taxonRank column
        unique_taxon_ranks = combined_df['taxonRank'].unique()
        print("\nUnique Values in taxonRank Column:")
        for rank in unique_taxon_ranks:
            print(rank)
    else:
        print("Failed to load one or more DataFrames.")

if __name__ == '__main__':
    main()