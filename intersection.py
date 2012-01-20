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
  lines = file.readlines()
  file.close()
except IOError:
  print "File '%s' was not found in current directory" % filename
  
lines = [line.replace('\n', '') for line in lines] 

for line in lines:
  lists = line.split(";")
  first_list = lists[0].split(",")
  second_list = lists[1].split(",")
  intersect = sorted([item for item in first_list if item in second_list])
  print ",".join(intersect)