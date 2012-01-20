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
  pairs = []
  digits, value = line.split(";")
  value = int(value)
  numbers = [int(d) for d in digits.split(",")]
  
  # remove any numbers greater than target value
  too_high = [x for x in numbers if x > value]
  [numbers.remove(x) for x in too_high]
  
  # if sum of all digits is less than value, there are no pairs
  if sum(numbers) < value:
    print "NULL"
    break
    
  for number in numbers:
    compliment = value - number
    if compliment in numbers:
      # we have a pair, add to list
      pairs.append([str(number), str(compliment)])
      
      # remove compliment from numbers to remove duplicates
      numbers.remove(compliment)
  if pairs:
    pairs = ";".join([",".join(pair) for pair in pairs])
    print pairs
  else:
    print "NULL"
