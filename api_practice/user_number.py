import requests

user_id = input("Enter the number (1-10): ").strip()

if not user_id.isdigit():
    print("The value should be a number")
elif not 1<= int(user_id) <= 10:
    print("The number should be between 1 and 10.")
else: 
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data["name"])
        else:
            print("Something went wrong:", response.status_code)
    except requests.exceptions.RequestException:
        print("Could not connect. Check your internet.")

