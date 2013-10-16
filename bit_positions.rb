#!/usr/bin/ruby

file_name = ARGV[0]

if file_name.nil?
  exit
end

file = File.new(file_name)

while (line = file.gets)
  digits = line.split(",")
  divisor_a = digits[1].to_i-1
  divisor_b = digits[2].to_i-1
  number = digits[0].to_i
  
  bin_string = number.to_s(2).reverse

  puts bin_string[divisor_a] == bin_string[divisor_b]
end