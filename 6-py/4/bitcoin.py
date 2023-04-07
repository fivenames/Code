import sys
import requests

if len(sys.argv) == 1:
    while True:
        try:
            amount = input("Number of Bitcoins you want to buy: ")
            amount = float(amount)
        except ValueError:
            pass
        else:
            break
elif len(sys.argv) == 2:
    amount = float([argv[1]])
else:
    print("Invalid command-line argument")
    quit()

r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = r.json()

price = r["bpi"]["USD"]["rate_float"]

pay = price * amount

print(f"${pay:,.2f}")