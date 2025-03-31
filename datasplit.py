from sklearn.model_selection import train_test_split
import json

# Load a JSON file
with open('path/to/your/file.json', 'r') as file:
    data = json.load(file)

# Check data structure
print(data)

# Example: Load code dataset (Assuming it's in JSON format)
with open('cleaned_snippets.json' 'r') as file:
    data = json.load(file)

# Split into training and testing data
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Optionally split train data further for validation
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

print(f'Training Data: {len(train_data)}')
print(f'Validation Data: {len(val_data)}')
print(f'Test Data: {len(test_data)}')
