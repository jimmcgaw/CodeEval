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

words = []

for line in lines:
  word = line.strip()
  words.append(word)
  
#print words

def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
    if not s1:
        return len(s2)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
    
social_network = []    

def get_social_network_for_word(test_word):
  for word in words:
    print "Testing %s, %s" % (word, test_word)
    leven_distance = levenshtein(word, test_word)
    if leven_distance == 1:
      social_network.append(word)
      friends = get_social_network_for_word(word)
      for friend in friends:
        if friend not in social_network:
          social_network.append(friend)
      
  return social_network
  
print get_social_network_for_word("causes")