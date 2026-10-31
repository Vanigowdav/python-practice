class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def role(self):
        return "Employee"

    def show(self):
        print(f"{self.name} | {self.role()} | Rs.{self.salary}")


class Manager(Employee):
    def role(self):
        return "Manager"


class Developer(Employee):
    def __init__(self, name, salary, language):
        super().__init__(name, salary)
        self.language = language

    def role(self):
        return f"Developer ({self.language})"


class Intern(Employee):
    def role(self):
        return "Intern"


staff = [
    Manager("Anil", 90000),
    Developer("Sita", 70000, "Python"),
    Developer("Ravi", 65000, "Java"),
    Intern("Meena", 15000),
]

# Loop 1: call the same method on every object
for person in staff:
    person.show()

# Loop 2: calculate total salary
total = 0
for person in staff:
    total += person.salary
print("Total salary:", total)

# Loop 3: filter using isinstance
print("Developers:")
for person in staff:
    if isinstance(person, Developer):
        print(" -", person.name, person.language)