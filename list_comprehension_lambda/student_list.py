students = [
    ["Rahul", 85],
    ["Priya", 92],
    ["Arun", 65],
    ["Sneha", 78],
    ["Kiran", 95]
]
result = [
    name for name, mark in students 
    if mark > 90
]
print(result)