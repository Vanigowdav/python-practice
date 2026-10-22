students = {
    "Vani": 85,
    "Rahul": 90,
    "Priya": 78,
    "Asha": 95
}

total = 0

# 1. Loop through the marks
for marks in students.values():
    # 2. Add each mark to total
    total += marks

# 3. Calculate the average
average = total / len(students)

print("Total marks:", total)
print("Average marks:", average)