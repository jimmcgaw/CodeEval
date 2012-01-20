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

  # read Fibbonacci indexes from file into list
  lines = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename
  
lines = [line.replace('\n', '') for line in lines] 

try:
  lines.remove("")
except:
  pass
  
def is_palendrome(my_string):
    """ returns true is 'my_string' is a palendrome """
    characters = []
    for char in my_string:
      characters.append(char)
    characters.reverse()
    reversed_string = "".join(characters)
    if my_string == reversed_string:
      return True
    else:
      return False
  
def reverse_add(number):
  """ takes number (as string) and returns number + number with digits reversed """
  original_number = int(number)
  new_number = int(number[::-1])
  return original_number + new_number


for line in lines:
  attempt = 1
  calculated = line
  while attempt <= 100:
    calculated = str(reverse_add(calculated))
    if is_palendrome(calculated):
      print str(attempt) + " " + str(calculated)
      break
    attempt += 1
  
  