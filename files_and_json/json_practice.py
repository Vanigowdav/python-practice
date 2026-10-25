import json
person = {
    "name": "Aishu",
    "age": 22,
    "city": "Mysore"
}

with open("test.json", "w") as f:
    json.dump(person, f)

print("Data saved successfully")