class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if 90 <= self.marks <= 100:
            return "Grade A"
        elif 80 <= self.marks  <= 89:
            return "Grade B"
        elif 70 <= self.marks  <= 79:
            return "Grade C"
        elif 60 <= self.marks  <= 69:
            return "Grade D"
        elif 50 <= self.marks  <= 59:
            return "Grade E"
        else:
            return "Fail"
    def show(self):
        return f"{self.name}: {self.marks}"      

s1 = Student("Vani", 90)
s2 = Student("Dia", 85)
print(s1.is_passed())
print(s2.is_passed())
print(s1.show())
print(s2.show())
