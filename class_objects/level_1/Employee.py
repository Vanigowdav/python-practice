class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

e1 = Employee("Vani", 110, 70000)
e2 = Employee("Aishu", 10, 80000)
e3 = Employee("Giri", 23, 120000)

# print(e1.name)
# print(e1.employee_id)
# print(e1.salary)
# print(e2.employee_id)

#use looping method insted of printing one at a time 
employees = []
employees.append(e1)
employees.append(e2)
employees.append(e3)

for attr in employees:
    print(f'{attr.name}:{attr.salary} - {attr.employee_id}')