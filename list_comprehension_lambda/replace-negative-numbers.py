numbers = [10, -5, 20, -8, 30, -2]
result = [
    num if num > 0
    else 0 
    for num in numbers  ]
print(result)