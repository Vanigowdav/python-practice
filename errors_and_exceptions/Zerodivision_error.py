def divide(a, b):
    try:
        a = float(a)
        b = float(b)
        print(a/b)
    except ZeroDivisionError:
        print("Value of b cannot be zero")
    except ValueError:
        print("Enter a valid number")

a = input("Enter a number: ")
b = input("Enter a number: ")
result = divide(a, b)