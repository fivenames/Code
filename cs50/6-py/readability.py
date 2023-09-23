text = input("Text: ")

text = text.lstrip().rstrip()
text = text.split()

num_word = len(text)
num_lettr = 0
num_senten = 0

for word in text:
    for lettr in word:
        if lettr.isalpha():
            num_lettr += 1
        elif lettr == '.' or lettr == '!' or lettr == '?':
            num_senten += 1
        else:
            continue

l = num_lettr / (num_word / 100)

s = num_senten / (num_word / 100)

grade = 0.0588 * l - 0.296 * s - 15.8

if grade < 1:
    print('Before Grade 1.')
elif grade > 16:
    print('Grade 16+')
else:
    print(round(grade))