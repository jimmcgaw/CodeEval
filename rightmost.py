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

try:
  lines.remove("")
except:
  pass

for line in lines:
  idx = -1
  elements = line.split(",")
  search_string = elements[0]
  search_char = elements[1]
  for char in search_string:
    if char == search_char:
      idx = search_string.index(search_char)
  print idx