try:
    age = int(input("Enter a age: "))
    print("Your age is: ", age)
except ValueError:
    print("Age must be a number")   
else:
    print("Conversion successful: ", age) 

finally:
    print("Program finished.")          