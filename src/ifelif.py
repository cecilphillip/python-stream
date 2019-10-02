import random
from colorama import Fore, Style

# Created a coin
coin_sides = ["HEADS", "TAILS"]

heads_count = 0
tails_count = 0

# Flip the coin 10 times
for index in range(0, 10):
    print(Style.RESET_ALL)
    print(f"We are at {index}")

    # Get the value of the flipped coin
    flip = random.choice(coin_sides)

    # print the result of our flip
    if flip == 'HEADS':
        heads_count += 1
        print(Fore.GREEN + 'HEADS wins')
    else:
        tails_count += 1
        print(Fore.CYAN + 'TAILS never fails')

def get_winner(heads, tails):
    if heads == tails:
        winner = "BOTH"
    elif heads > tails:
        winner = "HEADS"
    else:
        winner = "TAILS"

    template = f"The winner was {winner}"
    return template

winner = "something"
outcome = get_winner(heads_count, tails_count)

results = f"""
      Total heads count is {heads_count}
      Total tails count is {tails_count}
      {outcome}
"""

print(Fore.RED + results)
print(Style.RESET_ALL)
