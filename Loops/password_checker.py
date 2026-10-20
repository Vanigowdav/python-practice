password = "test123"
attempts = 0
while attempts < 3:
    user = input("Enter the password ")
    if user == password:
        print("Acess granted")
        break
    attempts += 1
    print("Wrong password: ")
else:
    print("Access locked")