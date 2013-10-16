#!/usr/bin/ruby

filename = ARGV[0]

if filename.nil?
  exit
end

file = File.new(filename)

class FibbonacciGenerator
  
  def initialize
    @sequence = [0,1]
  end
  
  def get_value_for_index(index)
    value = @sequence[index]
    
    if value.nil?
      generate_sequence_up_to_index(index)
      value = @sequence[index]
    end
    
    value
  end
  
  private
  
  def generate_sequence_up_to_index(index)
    while @sequence.length < index+1
      last_index = @sequence.length-1
      last_value = @sequence[last_index]
      penultimate_value = @sequence[last_index-1]
      next_value = penultimate_value + last_value
      @sequence.push(next_value)
    end
  end
  
end

fg = FibbonacciGenerator.new

while (line = file.gets)
  puts fg.get_value_for_index(line.to_i)
end