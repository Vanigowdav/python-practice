import json 

with open("test.json", "r")as f:
    person = json.load(f)

print(person)
print(type(person))
print(person["name"])
print(person["city"])