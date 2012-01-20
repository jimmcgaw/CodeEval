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

for line in lines:
  line = line.lower()
  line = line.encode('us-ascii', 'ignore')
  line_characters = sorted(list(set([char for char in line])))
  letters = [char for char in string.letters[0:26]]
  remaining = [letter for letter in letters if letter not in line_characters]
    
  
  if remaining:
    print "".join(remaining)
  else:
    print "NULL"
      