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

primes = [2,3,5,7]

# given a string that is n characters long, how many combinations of split
# groups with both operators are there?
# given m = n - 1:
#   combination_count = 2 ^ m + m(2^m-1) + m(2^m-2) ... m(2^1)

import copy

def compute_inserted_index_lists(line_length, space_count):
    if space_count == 1:
        return [range(1, line_length)]

operators = ['-', '+']

for line in lines:
    print line
    digits = list(line)
    test_numbers = []
    test_numbers.append(int(line)) # just append the single line value
    for space_count in range(1, len(digits)):
        # hard-coded solution for a single space being inserted
        if space_count == 1:
            for operator in operators:
                insert_index_lists = compute_inserted_index_lists(len(digits), space_count)
                for insert_index_list in insert_index_lists:
                    for insert_index in insert_index_list:
                        test_digits = list(digits)
                        test_digits.insert(insert_index, operator)
                        print eval(''.join(test_digits))
