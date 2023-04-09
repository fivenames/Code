import validators

email = input("What is your email? ")

if validators.email(email, whitelist=None):
    print("Valid")
else:
    print("Invalid")