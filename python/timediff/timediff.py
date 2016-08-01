#!/usr/bin/python

import sys
import datetime

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
    start_time, end_time = line.split(' ')
    # print start_time
    # print end_time
    start_time = datetime.datetime.strptime(start_time, '%H:%M:%S')
    end_time = datetime.datetime.strptime(end_time, '%H:%M:%S')
    if end_time < start_time:
        start_time, end_time = end_time, start_time
    diff = end_time - start_time
    hours = diff.seconds
    minutes = 0
    seconds = 0
    print '%02d:%02d:%02d' % (hours, minutes, seconds)
