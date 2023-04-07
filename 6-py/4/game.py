from random import randint

while True:
    try:
        level = input("Level: ")
        level = int(level)
    except ValueError:
        pass
    else:
        if level <= 0:
            pass
        else:
            break

answer = randint(1, level)

while True:
    guess = input("Guess: ")
    guess = int(guess)

    if guess == answer:
        print("Just right!")
        break
    elif guess < answer:
        print("Too small!")
    else:
        print("Too large!")

quit()
