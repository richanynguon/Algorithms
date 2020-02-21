#!/usr/bin/python
import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
# http://book.pythontips.com/en/latest/function_caching.html

def eating_cookies(n, cache=None):
  # creates an array of 0s for amount of cookies + 1 
  cache = cache or [0 for i in range(n+1)]
  # set return value for n values when 0 and 1 as 1
  # and sets up function to continue on setting cache array properly
  if n > 0:
      cache[0] = 1
      cache[1] = 1
  else:
      cache[0] = 1
  if cache[n] == 0:
      for i in range(1, min(n+1, 4)): 
        # since there is 4 numbers to run through max is 4 but 
        # if n = 2 , 4 cannot be used but 3 can be
        # calls recursive nature because of this
        cache[n] += eating_cookies(n - i, cache)
  print(cache)
  return cache[n]

  # iterative sorting is better than cache

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')