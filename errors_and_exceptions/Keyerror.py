def keyerror(student):
    try:
        key_name = input("enter key name you want to extract: ")
        print(student[key_name])
    except KeyError:
        print("Key is not found.")




try:
    student = {
        "name": input("enter your name: "),
        "age": int(input("enter your age: ")),
        "city": input("enter your city: ")
}

    keyerror(student)

except ValueError:
    print("Age must be a number.")

