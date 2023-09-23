greeting = input("Greeting: ")

string = greeting.lower()

if string.startswith("hello"):
    print("$0.00")
elif string.startswith('h'):
    print("$20.00")
else:
    print("$100.00")