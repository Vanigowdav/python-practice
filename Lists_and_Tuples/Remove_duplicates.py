def duplicates(my_list):
    new_list = []
    for item in my_list[:]:
        if item not in new_list:
            new_list.append(item)
    return new_list
my_list = [1, 2, 2, 3, 4, 4, 5]
print(duplicates(my_list))