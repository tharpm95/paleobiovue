# load_taxons.py

import os

def load_taxon_data(file_path):
    """Loads taxon data from a file and returns it as a list of dictionaries."""
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return None

    taxons = []
    with open(file_path, 'r') as file:
        headers = file.readline().strip().split('\t')
        for line in file:
            fields = line.strip().split('\t')
            taxon = {headers[i]: fields[i] for i in range(len(fields))}
            taxons.append(taxon)
    
    return taxons

def save_taxon_data(file_path, headers, taxons):
    """Saves taxon data to a file from a list of dictionaries."""
    with open(file_path, 'w') as file:
        file.write('\t'.join(headers) + '\n')
        for taxon in taxons:
            line = '\t'.join(str(taxon[header]) for header in headers)
            file.write(line + '\n')

def split_and_save_taxon_data(taxons, original_file_path):
    """Splits the taxons list in half and saves each half to new files."""
    total_taxons = len(taxons)
    half_index = total_taxons // 2
    first_half = taxons[:half_index]
    second_half = taxons[half_index:]

    # Determine the directory of the original file
    directory, original_file_name = os.path.split(original_file_path)
    base_name, ext = os.path.splitext(original_file_name)

    # Create new file paths for the two halves
    first_half_path = os.path.join(directory, f"{base_name}_part1{ext}")
    second_half_path = os.path.join(directory, f"{base_name}_part2{ext}")

    # Assuming taxons are not empty, using the headers from the first taxon
    headers = list(taxons[0].keys())

    # Save both halves to separate files
    save_taxon_data(first_half_path, headers, first_half)
    save_taxon_data(second_half_path, headers, second_half)

    print(f"Saved first half to {first_half_path}")
    print(f"Saved second half to {second_half_path}")

def main():
    # Assuming the current script's location is within `db` folder
    file_path = os.path.join('data', 'taxon.tab')
    taxons = load_taxon_data(file_path)
    
    if taxons is not None:
        print("Loaded Taxon Data:")
        
        split_and_save_taxon_data(taxons, file_path)

if __name__ == '__main__':
    main()