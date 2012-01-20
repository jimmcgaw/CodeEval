#!/usr/bin/python

import sys

class FibbonacciGenerator(object):
  """ The Fibonacci series is defined as: F(0) = 0; F(1) = 1; 
  F(n) = F(n-1) + F(n-2) when n>1;. Given a positive integer 'n', 
  print out the F(n).
  
  """
  def __init__(self):
    """ store Fibbonacci sequence as cached list, seeded with initial two values: F(0) = 0; F(1) = 1 """
    self._cache = [0,1]
    # check initialized object against specification
    assert(self._cache[0] == 0)
    assert(self._cache[1] == 1)
    
  def get_value_for_index(self, index):
    """ takes int value; looks up Fibbonacci series value at index in cache """
    
    # ensure that we have a valid integer provided as an index, 
    try:
      index = int(index)
      
      # check that sequence has been built up to provided index; generate if it has not
      if len(self._cache) < index+1:
        self._generate_cache_up_to_index(index)
        
      return self._cache[index]
    except ValueError:
      """ ignore any invalid integers in input file """
      return None

  def _generate_cache_up_to_index(self, index):
    """ Build cached sequence list up to provided index """
    while (len(self._cache) < index+1):
      last_index = (len(self._cache)-1)
      last_value = self._cache[last_index]
      penultimate_value = self._cache[last_index-1]
      next_value = last_value + penultimate_value
      self._cache.append(next_value)


# check that a filename argument was provided, otherwise
if len(sys.argv) < 2:
  raise Exception("Filename must be first argument provided")
  
filename = sys.argv[1]
fib_indexes = []

# open file in read mode, assuming file  is in same directory as script
try:
  file = open(filename, 'r')

  # read Fibbonacci indexes from file into list
  fib_indexes = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename

fg = FibbonacciGenerator()

for fib_index in fib_indexes:
  sequence_value = fg.get_value_for_index(fib_index)
  if sequence_value:
    print sequence_value
