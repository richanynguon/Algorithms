#!/usr/bin/python

import argparse
# https://www.geeksforgeeks.org/enumerate-in-python/ - shows both index and value
# [before:]
# [:after]

def find_max_profit(prices):
  largest_profit = float('-inf')
  for i, stake_price in enumerate(prices): #o(n)
    for sell_price in prices[i + 1:]: #o(n)
      profit = sell_price - stake_price
      if profit > largest_profit:
          largest_profit = profit
  return largest_profit

  # hint - tracking largest profit but also tracking something else




if __name__ == '__main__':
    # This is just some code to accept inputs from the command line
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
