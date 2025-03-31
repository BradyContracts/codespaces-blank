import os
import json
import csv
import random
import pandas as pd
from sklearn.model_selection import train_test_split

# Set random seed for reproducibility
random.seed(42)

# Configuration: Change these paths as needed
INPUT_PATH = "/workspaces/codespaces-blank/"  # Directory containing raw JSON or CSV files
OUTPUT_PATH = "/workspaces/codespaces-blank/processed"  # Directory to save processed files

# Ensure output directory exists
os.makedirs(OUTPUT_PATH, exist_ok=True)


def load_json(file_path):
    """Loads a JSON file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def load_csv(file_path):
    """Loads a CSV file and returns data as a list."""
    with open(file_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        return [row for row in reader]


def preprocess_snippets(snippets):
    """Optional: Cleans up code snippets (remove empty lines, strip spaces)."""
    cleaned = []
    for snippet in snippets:
        if isinstance(snippet, str):  # Ensure it's a string
            snippet = snippet.strip()
            if snippet:  # Ignore empty snippets
                cleaned.append(snippet)
    return cleaned


def split_and_save(data, base_filename):
    """Splits data into train, test, and validation sets, then saves them."""
    train, test = train_test_split(data, test_size=0.2, random_state=42)
    test, val = train_test_split(test, test_size=0.5, random_state=42)  # 10% test, 10% val

    # Save as JSON
    json.dump(train, open(f"{OUTPUT_PATH}/{base_filename}_train.json", "w", encoding="utf-8"), indent=4)
    json.dump(test, open(f"{OUTPUT_PATH}/{base_filename}_test.json", "w", encoding="utf-8"), indent=4)
    json.dump(val, open(f"{OUTPUT_PATH}/{base_filename}_val.json", "w", encoding="utf-8"), indent=4)

    # Save as CSV
    pd.DataFrame(train, columns=["code"]).to_csv(f"{OUTPUT_PATH}/{base_filename}_train.csv", index=False)
    pd.DataFrame(test, columns=["code"]).to_csv(f"{OUTPUT_PATH}/{base_filename}_test.csv", index=False)
    pd.DataFrame(val, columns=["code"]).to_csv(f"{OUTPUT_PATH}/{base_filename}_val.csv", index=False)

    print(f"Saved: {base_filename}_train, _test, _val")


def process_files():
    """Processes all JSON and CSV files in the input directory."""
    for file_name in os.listdir(INPUT_PATH):
        file_path = os.path.join(INPUT_PATH, file_name)

        if file_name.endswith(".json"):
            print(f"Processing JSON: {file_name}")
            data = load_json(file_path)
        elif file_name.endswith(".csv"):
            print(f"Processing CSV: {file_name}")
            df = pd.read_csv(file_path)
            data = df.iloc[:, 0].tolist()  # Assume first column is code snippets
        else:
            continue  # Skip non-JSON/CSV files

        # Preprocess and split the data
        clean_data = preprocess_snippets(data)
        if not clean_data:  # Skip if the dataset is empty
            print(f"Skipping {file_name}: No valid data after preprocessing.")
            continue

        base_name = os.path.splitext(file_name)[0]
        split_and_save(clean_data, base_name)


if __name__ == "__main__":
    process_files()
