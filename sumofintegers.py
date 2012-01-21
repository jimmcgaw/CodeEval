#!/usr/bin/python

import sys

# check that a filename argument was provided, otherwise
if len(sys.argv) < 2:
  raise Exception("Filename must be first argument provided")
  
filename = sys.argv[1]
lines = []

# open file in read mode, assuming file  is in same directory as script
try:
  file = open(filename, 'r')

  # read Fibbonacci indexes from file into list
  lines = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename

# strip out newline characters
lines = [line.replace('\n', '') for line in lines]

# ignore empty lines
try:
  lines.remove("")
except:
  pass

for line in lines:
  numbers = [int(x) for x in line.split(",")]
  number_length = len(numbers)
  largest_sum = 0
  
  for subarray_length in range(2, number_length+1):
    for initial_index in range(0, number_length-(subarray_length-1)):
      subarray = numbers[initial_index:initial_index+subarray_length]
      if subarray:
        subarray_sum = sum(subarray)
        if subarray_sum > largest_sum:
          largest_sum = subarray_sum
  print largest_sum