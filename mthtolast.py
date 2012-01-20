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

for line in lines:
  try:
    characters = line.split(" ")
    mth_to_last = int(characters.pop())
    print characters[-mth_to_last]
  except IndexError:
    pass
  
sys.exit(0)