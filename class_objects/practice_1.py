class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        return self.marks >= 35

    def show(self):
        print(f"{self.name}: {self.marks}")


s1 = Student("Vani", 30)
s2 = Student("Druv", 50)
s1.show()
print(s2.is_passed())