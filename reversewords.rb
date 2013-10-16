#!/usr/bin/ruby

filename = ARGV[0]

if filename.nil?
  exit
end

file = File.new(filename)

while (line = file.gets)
  line = line.gsub("\n", "")
  words = line.split(" ")
  if !words.empty?
    words = words.reverse
    puts words.join(" ")
  end
  
end