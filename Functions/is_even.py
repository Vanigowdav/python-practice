def is_even(n):
    if n % 2 == 0:
        return True
    else: 
        return False

user = int(input("Enter the number: "))
result = is_even(user)

if result:
    print("The given number is even")
else:
    print("The given number is odd")

