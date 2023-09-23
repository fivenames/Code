print("What is the Answer to the Great Question of Life, the Universe, and Everything?")

answer = input()

if(answer == "42" or answer.lower() == "forty-two" or answer.lower() == "forty two"):
    print("Yes")
else:
    print("No")