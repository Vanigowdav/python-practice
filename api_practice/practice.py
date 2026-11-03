import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
data = response.json()
print(type(data))
print(data[0])
for user in data:
    print(f'{user["name"]} and {user["email"]}')