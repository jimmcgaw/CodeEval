#!/usr/bin/python

from decimal import Decimal

import string
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
  
VOWELS = ['a','e','i','o','u','y']
PRODUCT_LETTERS_EVEN_MULTIPLE = Decimal("1.5")
COMMON_FACTOR_MULTIPLE = Decimal("1.5")
  
class DiscountDay(object):
  def __init__(self, persons, products):
    self.persons = persons
    self.products = products
    self._scores = []
    
  def get_max_suitability_score(self):
    self._compute_suitability_scores()
    return self._scores   #max(self._scores).quantize(Decimal("10")**-2)
    
  def _compute_suitability_scores(self):
    self._scores = []
    for person in self.persons:
      for product in self.products:
        score = self._compute_suitability_score(person, product)
        self._scores.append(score)
        
  def _highest_common_factor(self, no1, no2):
    """ 
    method sourced from: http://www.stealthcopter.com/blog/2009/12/python-highest-common-factor/
    """ 
    while no1!=no2:  
      if no1>no2:  
        no1-=no2  
      elif no2>no1:  
        no2-=no1  
    return no1
    
  def _has_common_factor(self, person, product):
    hcf = self._highest_common_factor(person.get_letter_count(), product.get_letter_count())
    return hcf != 1
      
  
  def _compute_suitability_score(self, person, product):
    """ 
    Given an instance of Person and an instance of Product, compute suitability score.
    1. If the number of letters in the product's name is even then the SS is the number 
      of vowels (a, e, i, o, u, y) in the customer's name multiplied by 1.5.
    2. If the number of letters in the product's name is odd then the SS is the number 
      of consonants in the customer's name.
    3. If the number of letters in the product's name shares any common factors (besides 1) 
      with the number of letters in the customer's name then the SS is multiplied by 1.5.
    
    """
    if product.is_letter_count_even():
      score = person.get_vowel_count() * PRODUCT_LETTERS_EVEN_MULTIPLE
    else:
      score = Decimal(person.get_consonant_count())
    
    if self._has_common_factor(person, product):
      score *= COMMON_FACTOR_MULTIPLE
    return score
      
      
class Person(object):
  def __init__(self, name):
    self.name = name
  
  def get_vowel_count(self):
    return len(self._get_vowels())
    
  def get_consonant_count(self):
    return len(self._get_consonants())
    
  def get_letter_count(self):
    name = self.name
    for char in name:
      if char not in string.letters:
        name.replace(char, "")
    return len(name)
    
  def _get_vowels(self):
    vowels = []
    for char in self.name.lower():
      if char in VOWELS:
        vowels.append(char)
    return vowels
    
  def _get_consonants(self):
    consonants = []
    for char in self.name.lower():
      if char in string.letters and char not in VOWELS:
        consonants.append(char)
    return consonants
  
  
    
    
class Product(object):
  def __init__(self, name):
    self.name = name
    
  def is_letter_count_even(self):
    return self.get_letter_count() % 2 == 0
    
  def get_letter_count(self):
    name = self.name
    for char in name:
      if char not in string.letters:
        name.replace(char, "")
    return len(name)
    
    
    
discount_days = []
  
for line in lines:
  line = line.encode('ascii', 'ignore')
  persons_as_string, products_as_string = line.split(";")
  person_names = persons_as_string.split(",")
  product_names = products_as_string.split(",")
  
  persons = [Person(name) for name in person_names]
  products = [Product(name) for name in product_names]
  
  discount_day = DiscountDay(persons, products)
  discount_days.append(discount_day)
  
  
for discount_day in discount_days:
  print discount_day.get_max_suitability_score()