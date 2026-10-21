def mini(my_list):
    smallest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] < smallest:
            smallest = my_list[i]
    return smallest



def maxi(my_list):
    largest = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > largest:
            largest = my_list[i]
    return largest 

def total(my_list):
    total = 0
    for i in range(len(my_list)):
        total += my_list[i]
    return total

def avg(my_list):
    my_list_length = len(my_list)
    avg = total(my_list) / my_list_length
    return avg 

my_list = [22, 15, 10, 40, 5]
print(mini(my_list))
print(maxi(my_list))
print(total(my_list))
print(avg(my_list))


# using Built-in -functions
new_list = [1, 23, 34, 2, 4, 6]
print(sum(new_list))
print(max(new_list))
print(min(new_list))
average = sum(new_list) / len(new_list)
print(average)