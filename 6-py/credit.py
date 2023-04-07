card = input("Card Number: ")

card = list(card)

n = len(card)

if n < 13 or n > 16:
    print("Invalid")
    quit()

try:
    sum = 0
    for i in range(n):
        card[i] = int(card[i])
        if i % 2 == 0:
            card[i] = card[i] * 2
            if card[i] < 10:
                sum += card[i]
            else:
                sum += (1 + (card[i] % 10))
        else:
            sum += card[i]
except ValueError:
    print("Enter a card number.")
    quit()

if sum % 10 == 0 and n == 15:
    if card[0] == 6:
        if card[1] == 4 or card[1] == 7:
            print('American Express')
    elif card[0] == 10 and n == 16:
        if card[1] == 1 or card[1] == 2 or card[1] == 3 or card[1] == 4 or card[1] == 5:
            print('MasterCard')
    elif card[0] == 4:
        if n == 13 or n == 16:
            print('Visa')
    else:
        print('Unable to identify card type.')
else:
    print("Invalid")