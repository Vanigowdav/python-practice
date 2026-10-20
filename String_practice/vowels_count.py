def vowels(my_string):
    my_count = 0
    vowels = "a", "e", "i", "o", "u"
    for char in my_string.lower():
        if char in vowels:
            my_count += 1
           
    return my_count


my_string = input("Enter the string name: ")
print(vowels(my_string))