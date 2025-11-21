# JSON = JavaScript Object Notation
import json

with open('example.json', mode='r') as json_file:
    data = json.load(json_file)

with open('output.json', mode='w') as output_file:
    # Modify data (for example, add a new key-value pair)
    data['new_key'] = 'new_value'
    # Write modified data to new JSON file with pretty-printing
    json.dump(data, output_file, indent=4, sort_keys=True)

# print(data.items())  # Print all key-value pairs
