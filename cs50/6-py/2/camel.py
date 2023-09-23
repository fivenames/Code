string = input("camelCase: ")

result = []

for c in string:
    if c.isupper():
        result.append('_')
        result.append(c.lower())
    else:
        result.append(c)

result = ''.join(result)

print(f"snake_case: {result}")

# or

for c in string:
    if c.isupper():
        print('_' + c.lower(), end='')
    else:
        print(c, end='')
print()