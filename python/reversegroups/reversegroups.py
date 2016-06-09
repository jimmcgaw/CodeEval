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

def chunkify(sequence, k):
    for i in xrange(0, len(sequence), k):
        yield sequence[i:i+k]

for line in lines:
    sequence, k = line.split(';')
    k = int(k)
    sequence = sequence.split(',')
    subsequences = [sequence[i:i+k] for i in xrange(0, len(sequence), k)]
    for sub in subsequences:
        if len(sub) >= k:
            sub.reverse()

    print ','.join( sum(subsequences, []) )
