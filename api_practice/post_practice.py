import requests 

response = requests.get("https://jsonplaceholder.typicode.com/posts?userId=1")
if response.status_code == 200:
    data = response.json()
    for post in data:
        print(post["title"])
else:
    print("Something went wrong")