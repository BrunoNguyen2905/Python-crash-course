# JSON = JavaScript Object Notation
import json

json_string = '''{
    "name": "Bulbasaur",
    "type": ["Grass", "Poison"],
    "stats": {
        "hp": 45,
        "attack": 49,
        "defense": 49,
        "speed": 45
    },
    "abilities": ["Overgrow", "Chlorophyll"]
}'''

data = json.loads(json_string)
print("data:", data['abilities'][0])  # Accessing first ability
data['stats']['hasHiddenSkills'] = True  # Adding new key-value pair
# Pretty-print with indentation
new_json_string = json.dumps(data, indent=2, sort_keys=True)
print("new_json_string:", new_json_string)
