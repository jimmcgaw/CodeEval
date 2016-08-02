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

import itertools

for line in lines:
    seqs = []
    d = {k: v for k, v in enumerate(sorted(list(line)))}
    indices = sorted(d.keys())
    perms = list(itertools.permutations(indices))
    for perm in perms:
        chars = []
        for index in perm:
            chars.append(d[index])
        seq = ''.join(chars)
        seqs.append(seq)
    print ','.join(seqs)
