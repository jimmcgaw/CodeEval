#!/usr/bin/python

prime_number_list = []

def is_prime(value):
  """ returns True if 'value' (integer) is a prime number """
  if value < 4:
    return True
    
  lower_bound = 2
  upper_bound = value-1
  
  prime = True
  test_value = lower_bound
  
  while test_value < upper_bound:
    #print "testing divisibility of %d for %d" % (value, test_value)
    if value % test_value == 0:
      prime = False
    test_value += 1
  return prime


test_number = 2

# compile list of prime numbers less than 1000
while len(prime_number_list) < 1000:
  if is_prime(test_number):
    prime_number_list.append(test_number)
  test_number += 1

print len(prime_number_list)
print sum(prime_number_list)
