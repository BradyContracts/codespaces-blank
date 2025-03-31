import random
import string
import json
import csv


# Predefined list of function templates
function_templates = [
    "def {function_name}({args}):\n    {body}",
    "def {function_name}({args}):\n    return {return_value}",
]

# Predefined list of class templates
class_templates = [
    "class {class_name}:\n    def __init__(self, {init_args}):\n        {init_body}",
    "class {class_name}:\n    pass",
]

# Predefined list of loops and conditionals
loop_templates = [
    "for {var} in {iterable}:\n    {body}",
    "while {condition}:\n    {body}",
]






# Predefined list of random Python variables
variables = ["x", "y", "z", "num", "total", "counter", "result", "temp", "value"]

# Predefined list of random functions and operations
operations = [
    "{var} + {var}",
    "{var} - {var}",
    "{var} * {var}",
    "{var} / {var}",
    "len({var})",
    "{var} == {var}",
    "{var} > {var}",
    "{var} < {var}",
    "print({var})",
    "return {var}",
    "if {var}:\n    # do something\nelse:\n    # do something else",
    "try:\n    {var}\nexcept Exception as e:\n    print(e)",
    "with open('file.txt', 'w') as f:\n    f.write({var})",
    "import {var}",
    "from {var} import {var}",
    "import {var} as {var}",
    "def {var}():\n    pass",
    "lambda {var}: {var}",
    "append({var})",
    "class {var}:\n    pass",
]

# Predefined list of return values
return_values = ["None", "True", "False", "0", "1", "[]", "{}", "len({var})", "sum({var})"]

# Helper function to generate a random string (e.g., variable names, function names)
def generate_random_string(length=10):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

# Helper function to generate random arguments
def generate_random_args():
    return ", ".join(random.sample(variables, random.randint(1, 5)))

# Helper function to generate random iterable (e.g., list, range)
def generate_random_iterable():
    return random.choice([f"range=10)", f"[{', '.join(random.sample(variables, random.randint(1, 5)))}]", f"list({generate_random_string()})"])

# Helper function to generate random condition
def generate_random_condition():
    return random.choice([f"{random.choice(variables)} > 5", f"{random.choice(variables)} < 5", f"{random.choice(variables)} == {random.choice(variables)}"])

# Function to generate a random function snippet
def generate_function_snippet():
    function_name = generate_random_string()
    args = generate_random_args()
    body = random.choice(operations).format(var=random.choice(variables))
    return random.choice(function_templates).format(function_name=function_name, args=args, body=body, return_value=random.choice(return_values))

# Function to generate a random class snippet
def generate_class_snippet():
    class_name = generate_random_string()
    init_args = generate_random_args()
    init_body = random.choice(operations).format(var=random.choice(variables))
    return random.choice(class_templates).format(class_name=class_name, init_args=init_args, init_body=init_body)

# Function to generate a random loop or conditional snippet
def generate_loop_snippet():
    loop_type = random.choice(loop_templates)
    var = random.choice(variables)
    iterable = generate_random_iterable()
    body = random.choice(operations).format(var=random.choice(variables))
    
    if "{condition}" in loop_type:
        condition = generate_random_condition()
        return loop_type.format(condition=condition, body=body)
    else:
        return loop_type.format(var=var, iterable=iterable, body=body)

# Main function to generate a random code snippet
def generate_code_snippet():
    snippet_type = random.choice(["function", "class", "loop"])
    
    if snippet_type == "function":
        return generate_function_snippet()
    elif snippet_type == "class":
        return generate_class_snippet()
    elif snippet_type == "loop":
        return generate_loop_snippet()

# Example: Generate and save random code snippets to a CSV file
def save_snippets_to_csv(num_snippets=10, filename='snippets.csv'):
    snippets = [generate_code_snippet() for _ in range(num_snippets)]
    
    # Save to CSV
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Snippet'])
        for snippet in snippets:
            writer.writerow([snippet])
    
    print(f"Snippets saved to {filename}")

# Example: Generate and save random code snippets to a JSON file
def save_snippets_to_json(num_snippets=10, filename='snippets.json'):
    snippets = [generate_code_snippet() for _ in range(num_snippets)]
    
    # Save to JSON
    with open(filename, mode='w') as file:
        json.dump(snippets, file, indent=4)
    
    print(f"Snippets saved to {filename}")

if __name__ == "__main__":
    for _ in range(5):
        print(generate_code_snippet())
        print("\n" + "-"*40 + "\n")
    
    # Save snippets to files
    save_snippets_to_csv(50, 'snippets.csv')
    save_snippets_to_json(50, 'snippets.json')
