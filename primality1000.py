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


def is_palendrome(my_string):
  """ returns true is 'my_string' is a palendrome """
  characters = []
  for char in my_string:
    characters.append(char)
  characters.reverse()
  reversed_string = "".join(characters)
  if my_string == reversed_string:
    return True
  else:
    return False

test_number = 1

# compile list of prime numbers less than 1000
while test_number <= 1000:
  if is_prime(test_number):
    prime_number_list.append(test_number)
  test_number += 1

prime_number_list.reverse()

prime_number_list = [str(num) for num in prime_number_list]

for prime_number in prime_number_list:
  if is_palendrome(prime_number):
    print prime_number
    break