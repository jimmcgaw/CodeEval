#!/usr/bin/python

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

from itertools import groupby
from operator import itemgetter

for line in lines:
    # print line
    chars = [char.lower() for char in list(line)]
    index_list = []
    for index, char in enumerate(chars):
        if char.isalpha():
            index_list.append(index)

    word_indices = []
    for key, group in groupby(enumerate(index_list), lambda (index, char_index): index - char_index):
        word_indices.append( map(itemgetter(1), group) )

    words = []
    for word_index in word_indices:
        word_chars = [chars[wi] for wi in word_index]
        word = ''.join(word_chars)
        words.append(word)

    print ' '.join(words)
