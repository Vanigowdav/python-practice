def even():
    new_list = []
    for i in range(1, 21):
        if i % 2 == 0:
            new_list.append(i)
    return new_list

print(even())