class Father:
    def __init__(self):
        self.surname = "Sharma"

    def skills(self):
        print("Father: Driving, Cooking")


class Mother:
    def __init__(self):
        self.hometown = "Mysuru"

    def skills(self):
        print("Mother: Singing, Painting")

    def language(self):
        print("Mother: Speaks Kannada")


class Child(Father, Mother):
    def __init__(self):
        Father.__init__(self)       # call each parent's __init__
        Mother.__init__(self)
        self.name = "Arjun"

    def show(self):
        print(f"{self.name} {self.surname} from {self.hometown}")


c = Child()
c.show()          # Arjun Sharma from Mysuru
c.skills()        # Father: Driving, Cooking
c.language()      # Mother: Speaks Kannada

print(Child.__mro__)