#!/usr/bin/python

import sys
import re

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
  numbers = line.split(" ")
  a = int(numbers[0])
  b = int(numbers[1])
  num = int(numbers[2])
  
  current = 1
  digits = []
  while current <= num:
    digits.append(current)
    current += 1
    
  #print digits
  
  for digit in digits:
    new_value = ""
    index = digits.index(digit)
    
    divisible_by_a = digit % a == 0
    divisible_by_b = digit % b == 0
    divisible_by_both = divisible_by_a and divisible_by_b
    
    if divisible_by_a:
      new_value = "F"
    if divisible_by_b:
      new_value = "B"
    if divisible_by_both:
      new_value = "FB"
    if new_value:
      digits[index] = new_value
      
  digits = [str(d) for d in digits]
  print " ".join(digits)
  
  
