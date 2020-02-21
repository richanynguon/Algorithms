#!/usr/bin/python

import sys


def rps_possibilities(n, combinations, actions, cache=[]):
  if n == 0:
      return combinations.append(cache)
  for choices in actions:
      # after going through one choice
      # n must be n-1 gives permutation
      rps_possibilities(n - 1, combinations, actions, cache + [choices])


def rock_paper_scissors(n):
  combinations = []
  actions = ["rock", "paper", "scissors"]
  rps_possibilities(n, combinations, actions)
  return combinations


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_plays = int(sys.argv[1])
        print(rock_paper_scissors(num_plays))
    else:
        print('Usage: rps.py [num_plays]')
