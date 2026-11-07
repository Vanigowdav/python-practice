import requests

response = requests.get("https://jsonplaceholder.typicode.com/users")
if response.status_code == 200:
    data = response.json()
    for user in data:
        print(f'{user["name"]} and {user["email"]}')
else:
    print("Something went wrong")