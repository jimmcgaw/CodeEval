#!/usr/bin/python

import sys

if sys.byteorder == 'little':
  print "LittleEndian"
else:
  print "BigEndian"