#!/usr/bin/ruby

prime_numbers = []

value = 2

def is_prime n
  for d in 2..(n - 1)
   if (n % d) == 0
    return false
   end
  end

  true
end

while prime_numbers.length < 1000
  if is_prime(value)
    prime_numbers.push(value)
  end
  value += 1
end

puts prime_numbers.inject{|sum,x| sum + x }