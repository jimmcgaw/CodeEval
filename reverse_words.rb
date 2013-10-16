#!/usr/bin/ruby

filename = ARGV[0]

if filename.nil?
  exit
end

file = File.new(filename)

while (line = file.gets)
  puts line.split(" ").reverse.join(" ")
end