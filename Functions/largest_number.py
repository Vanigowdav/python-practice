def max_of_three(a, b, c):
    if a > b & a > c:
        return a
    elif b > a & b > c:
        return b
    else:
        return c

print(max_of_three(5, 15, 23))
print(max_of_three(800, 801, 799))