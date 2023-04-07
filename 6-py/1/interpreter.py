math = input("Expression: ")

try:
    [x, y, z] = math.split(" ")
except(ValueError):
    print("Provide expression in correct format")
    quit()

try:
    x = int(x)
    z = int(z)
except(ValueError):
    print("Provide numbers in correct format")
    quit()

if y == '+':
    print(f"{x + z}")
elif y == '-':
    print(f"{x - z}")
elif y == '*':
    print(f"{x * z}")
elif y == '/':
    print(f"{x / z}")
else:
    print("Provide operator in correct format")