#!/usr/bin/python

import string
import sys

# check that a filename argument was provided, otherwise
if len(sys.argv) < 2:
  raise Exception("Filename must be first argument provided")
  
filename = sys.argv[1]
lines = []

# open file in read mode, assuming file  is in same directory as script
try:
  file = open(filename, 'r')
  lines = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename
  
lines = [line.replace('\n', '') for line in lines] 

try:
  lines.remove("")
except:
  pass
  
class PrimeChecker(object):
  def __init__(value):
    self._cache = []
  
  def is_prime(value):
    if value == 1:
      return False
    if value < 4:
      return True
      
    return self._check_cache(value)
    
    lower_bound = 2
    upper_bound = value-1

    prime = True
    test_value = lower_bound

    while test_value < upper_bound:
      #print "testing divisibility of %d for %d" % (value, test_value)
      if value % test_value == 0:
        prime = False
      test_value += 1
    return prime
    
  def _generate_cache(value):
    """ add prime numbers to cache from cache_max to value """
    cache_max = max(self._cache) if self._cache else 2
    while cache_max < value:
      if 
    
  def _check_if_prime(value):
    self._generate_cache(value)
    return value in self._cache
    
  def _check_cache(value):
    """ if max value in cache is greater than or equal to value,
    then check cache list. If value in list, it is prime.
    If not in cache, generate values from cache max to value provided.
    
    """
    if self._cache and max(self._cache) >= value:
      if value in self._cache:
        return True
      else:
        return False
    else:
      return self._check_if_prime(value)
      
pc = PrimeChecker()

for line in lines:
  primes = []
  start = 2
  ceiling = int(line)
  while start < ceiling:
    if pc.is_prime(start):
      primes.append(start)
  