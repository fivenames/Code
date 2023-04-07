# Simulate a sports tournament

import csv
import sys
import random

# Number of simluations to run
N = 1000


def main():

    if len(sys.argv) != 2:
        sys.exit("Usage: python tournament.py FILENAME")

    # List of dictionaries.
    teams = []
    with open(sys.argv[1], "r") as file:
# this function will read the first row and set the keys to be the headers of the columns and the values are the corresponding data in each row. (2 key-value pairs in this case)
# teams = [    {"team": "Norway", "rating": 1915},    {"team": "Australia", "rating": 2003},    {"team": "England", "rating": 2049},    ...]
        reader = csv.DictReader(file)
        # iterates over each row.
        for each_pair in reader:
            # convert rating to int as DictReader reads all data as str.
            # note that the key to each data is mapped by the header. (This case "rating" is the key, the team's rating is the value.)
            each_pair["rating"] = int(each_pair["rating"])

            teams.append(each_pair)

    counts = {}

    for i in range(N):
        # winner is a str that stores a team's name
        winner = simulate_tournament(teams)

        if winner in counts:
            counts[winner] += 1
        # If winner is not in the dictionary.
        else:
            # This line adds a new key-value pair to the dictionary.
# This is a feature of Python, which allows a new key to be added the dictionary without explicitly creating the key in the dictionary.
            counts[winner] = 1

    # Print each team's chances of winning, according to simulation

# def get_team(team):
#     return counts[team]
# sorted(counts, key=get_team, reverse=True) works the same.
# This will pass the number of rounds won by each team to the function and sort them in descending order.

# reverse is set to true, the team will be sorted descendingly.
    for team in sorted(counts, key=lambda team: counts[team], reverse=True):
        print(f"{team}: {counts[team] * 100 / N:.1f}% chance of winning")


def simulate_game(team1, team2):
    """Simulate a game. Return True if team1 wins, False otherwise."""
    rating1 = team1["rating"]
    rating2 = team2["rating"]
    probability = 1 / (1 + 10 ** ((rating2 - rating1) / 600))
    return random.random() < probability


def simulate_round(teams):
    """Simulate a round. Return a list of winning teams."""
    winners = []

    # Simulate games for all pairs of teams
    for i in range(0, len(teams), 2):
        if simulate_game(teams[i], teams[i + 1]):
            winners.append(teams[i])
        else:
            winners.append(teams[i + 1])

    return winners


def simulate_tournament(teams):
    """Simulate a tournament. Return name of winning team."""
    while len(teams) > 1:
        teams = simulate_round(teams)

    # the first and only element in the list team[0], passing in the key: [team] will return the final winner tema's name.
    return teams[0]["team"]


if __name__ == "__main__":
    main()
