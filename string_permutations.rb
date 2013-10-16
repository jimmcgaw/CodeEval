#!/usr/bin/ruby

file_name = ARGV[0]

if file_name.nil?
  exit
end

file = File.new(file_name)

while (line = file.gets)
  letters = line.split("")
  n = letters.count
  digits = 1.upto(n)
  a = []
  digits.each {|d|
  	a.push(letters[d-1])
  }
  puts a.join("")
end