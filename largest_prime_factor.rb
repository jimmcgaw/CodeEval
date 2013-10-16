#!/usr/bin/ruby

number_to_factor = ARGV[0].to_i

prime_numbers = []
factors = []

def is_prime n
  
  for d in 2..(n - 1)
   if (n % d) == 0
    return false
   end
  end

  true
end

for n in 2..number_to_factor
  if is_prime(n)
    puts n
    prime_numbers.push(n)
  end
end

def factor n
  prime_numbers.each {|pn|
    puts pn
  }
end