#!/usr/bin/python

import string
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
  
lines = [line.replace('\n', '') for line in lines] 

try:
  lines.remove("")
except:
  pass
  
def get_substrings(value, substring_length):
  """ returns all substrings in string value of length n """
  string_length = len(line)
  substrings = []
  
  lower_bound = 0
  upper_bound = substring_length
  while upper_bound <= string_length:
    substrings.append(value[lower_bound:upper_bound])
    lower_bound += 1
    upper_bound += 1
    
  return substrings
  
  
def get_repeated_strings(string_list):
  """ return first duplicate string in list string_list if found, otherwise return empty list """
  dups = [x for x in string_list if string_list.count(x) > 1]
  
  if dups:
    dups = dups[0:len(dups)/2]
    return dups
  else:
    return []
  
    
def do_substrings_overlap(string, substring):
  """ substring occurs in string at least once, return True if occurrences overlap within string """
  substring_length = len(substring)
  
  left_index = string.find(substring)
  right_index = string.rfind(substring)
  
  diff = right_index - left_index
  if diff < substring_length and diff != 0:
    return True
  return False
  

for line in lines:
  string_length = len(line)
  # start with half of string length
  substring_length = string_length / 2
  
  while substring_length > 1:
    substrings = get_substrings(line, substring_length)
    repeated_substrings = get_repeated_strings(substrings)
    if repeated_substrings:
      for substring in repeated_substrings:
        overlap = do_substrings_overlap(line, substring)
        if not overlap:
          # we have a winner!
          print substring
          break
          
    #print substrings
    substring_length -= 1
  
  
