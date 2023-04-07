try:
    change = float(input("Change owed: $"))
    if change < 0:
        raise ValueError
except ValueError:
    print("Input an amount in dollar.")
    quit()

quarters = 0.25
q_count = 0
dimes = 0.1
d_count = 0
nickels = 0.05
n_count = 0
pennies = 0.01
p_count = 0

while (change > 0):
    if change >= quarters:
        change -= quarters
        q_count += 1
    elif change < quarters and change >= dimes:
        change -= dimes
        d_count += 1
    elif change < dimes and change >= nickels:
        change -= nickels
        n_count += 1
    elif change < nickels and change >= pennies:
        change -= pennies
        p_count += 1
    else:
        break

print(f"{q_count} quarters, {d_count} dimes, {n_count} nickels and {p_count} pennies")
