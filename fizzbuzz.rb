#!/usr/bin/ruby

file_name = ARGV[0]

if file_name.nil?
  exit
end

file = File.new(file_name)

while (line = file.gets)
  digits = line.split(" ")
  divisor_a = digits[0].to_i
  divisor_b = digits[1].to_i
  upto_value = digits[2].to_i
  numbers = []
  1.upto(upto_value) {|x| numbers.push(x)}
  numbers.each{ |x|
    idx = numbers.index(x)
    
    if x % divisor_a == 0
      numbers[idx] = 'F'
    end
    
    if x % divisor_b == 0
      numbers[idx] = 'B'
    end
    
    if x % divisor_a == 0 && x % divisor_b == 0
      numbers[idx] = 'FB'
    end
  }
  
  puts numbers.join(" ")
end