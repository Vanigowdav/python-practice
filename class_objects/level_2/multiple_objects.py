class multiple_objects:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def display(self, students):
        for obj in students:
            print(f"{obj.name} : {obj.marks}")

students = []
s1 = multiple_objects("Vani", 48)
s2 = multiple_objects("Aishu", 50)
s3 = multiple_objects("Giri", 49)
students.append(s1)
students.append(s2)
students.append(s3)
s1.display(students)