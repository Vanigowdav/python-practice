employee = {
    "name": "Rahul",
    "role": "Python Developer",
    "salary": 30000
}

# 1. Get the employee's role
print(employee.get("role"))

# 2. Get the city, or display "Not found"
print(employee.get("city", "Not found"))

# 3. Add the city
employee["city"] = "Bengaluru"

# 4. Print the updated dictionary
print(employee)