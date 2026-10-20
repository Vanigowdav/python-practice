def reverse_palindrome(my_string):
    your_string = my_string[::-1].upper()
    if my_string.upper() == your_string:
        return "Its palindrome"
    else:
        return "Not a palindrome"

my_string = input("Enter the string name: ")
print(reverse_palindrome(my_string))