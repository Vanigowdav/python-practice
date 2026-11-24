import re 
email = "vani19@gmail.com"
pattern = r"^[\w.-]+@[\w.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")