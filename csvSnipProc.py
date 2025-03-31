import csv
import re
import json  # Importing the json module to fix the NameError

def clean_snippet(snippet):
    # Same cleaning logic as before
    snippet = re.sub(r'range\s*=\s*(\d+)', r'range(\1)', snippet)
    snippet = re.sub(r'for\s+(.*?)\s+in\s+range=\d+\):', r'for \1 in range(10):', snippet)
    snippet = re.sub(r'(def\s+.*?)(?=\n)', r'\1:', snippet)
    snippet = re.sub(r'(class\s+.*?)(?=\n)', r'\1:', snippet)
    snippet = re.sub(r'append\((.*?)\)', r'list.append(\1)', snippet)
    snippet = re.sub(r'for\s+\w+\s+in\s+range\(\d\):', r'for value in range(10):', snippet)
    snippet = re.sub(r'return\s+sum\({var}\)', r'return sum([var])', snippet)
    snippet = re.sub(r'while\s+\w+\s*>\s*7:', r'while x > 7:', snippet)
    
    snippet = snippet.strip()
    
    return snippet

def load_snippets_from_csv(file_path):
    # Load the raw snippets from a CSV file
    snippets = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            snippets.append(row[0])  # Assuming the code snippets are in the first column
    return snippets

def clean_and_save_snippets(snippets, file_name='cleaned_snippets.json'):
    cleaned_snippets = [clean_snippet(snippet) for snippet in snippets]
    
    # Save the cleaned snippets to a csv file
    with open(file_name, 'w') as f:
        json.dump(cleaned_snippets, f, indent=4)

    return cleaned_snippets

# Specify the path to your raw snippets CSV file
raw_file_path = '/workspaces/codespaces-blank/snippets.csv'

# Load snippets from the file
raw_snippets = load_snippets_from_csv(raw_file_path)

# Clean and save the snippets
cleaned_snippets = clean_and_save_snippets(raw_snippets)

# Print out cleaned snippets
for snippet in cleaned_snippets:
    print(snippet)
