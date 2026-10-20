def split_and_join(my_string):
    new_string = my_string.title()
    split_string = new_string.split()
    print(split_string)
    join_string = " ".join(split_string)
    print(join_string)
    return new_string

my_string = input("Enter your First name and Last name: ")
print(split_and_join(my_string))
