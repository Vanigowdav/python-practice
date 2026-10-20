def email_check(your_email):
    if "@" in your_email and your_email.upper().endswith(".COM"):
        return "Valid"
    else:
        return "Invalid"

your_email = input("Enter your email: ")
print(email_check(your_email))