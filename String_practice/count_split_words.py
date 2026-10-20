def count_split_words(my_string):
    count = 0
    new_string = my_string.strip()
    split_string = new_string.split()
    for item in split_string:
        count += 1
    return count
my_string = input("Enter the string name: ")
print(count_split_words(my_string))