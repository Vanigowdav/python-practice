class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)      # calls Animal's __init__
        self.breed = breed

    def speak(self):                # overrides parent's method
        print(f"{self.name} says Woof!")

    def info(self):
        print(f"{self.name} is a {self.breed}")


d = Dog("Rex", "Labrador")
d.speak()    # Rex says Woof!
d.info()     # Rex is a Labrador