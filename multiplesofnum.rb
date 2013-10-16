#!/usr/bin/ruby

filename = ARGV[0]

if filename.nil?
  exit
end

file = File.new(filename)

while (line = file.gets)
  digits = line.split(",")
  floor = digits[0].to_i
  base = digits[1].to_i
  multiple = 1
  value = base*multiple
  
  while value < floor
    multiple += 1
    value = base*multiple
  end
  
  puts value
end