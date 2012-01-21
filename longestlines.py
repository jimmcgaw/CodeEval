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

number_of_lines = int(lines[0])
del lines[0]
counts_lines = [(len(line), line) for line in lines]
counts_lines.sort()
counts_lines.reverse()

longest_lines = counts_lines[:number_of_lines]

for long_line in longest_lines:
  print long_line[1]