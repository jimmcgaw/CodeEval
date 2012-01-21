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
  target_string, chars_to_remove = line.split(",")
  chars_to_remove = chars_to_remove.strip()
  for char in chars_to_remove:
    target_string = target_string.replace(char, "")
  print target_string.strip()