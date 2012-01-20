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

lines = [line.replace('\n', '') for line in lines] 

lines.remove("")

for line in lines:
  words = line.split(" ")
  words.reverse()
  new_line = " ".join(words)
  print new_line
  