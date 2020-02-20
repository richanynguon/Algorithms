#!/usr/bin/python

import sys

def making_change(amount, denominations):
  cache = [0] * (amount + 1)
  cache[0] = 1 
  for select_coin_value in denominations:
    for new_index in range(select_coin_value, amount+1):
      ## adds info to cache system for each part of cents change
      before_new_index = new_index - select_coin_value
      # keeps building left over to get change value
      cache[new_index] += cache[before_new_index]
      print(cache[new_index])
  return cache[amount]


if __name__ == "__main__":
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")