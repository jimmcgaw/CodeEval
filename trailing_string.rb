#!/usr/bin/ruby

filename = ARGV[0]

if filename.nil?
  exit
end

file = File.new(filename)

while (line = file.gets)
  phrase, word = line.split(",")
  if phrase.end_with?(word)
    puts 1
  else
    puts 0
  end
end