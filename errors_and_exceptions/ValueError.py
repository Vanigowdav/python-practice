while True:
    try:
        number = int(input("Enter the number: "))
        squared_number = number * number
        print(squared_number)
        break
    except ValueError:
        print("Enter a valid number: ")
