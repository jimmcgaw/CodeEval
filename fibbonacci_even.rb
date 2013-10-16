#!/usr/bin/ruby

fibbonacci = [1,2]

evens = []

while fibbonacci[0] < 4000000
  if fibbonacci[0] % 2 == 0
    evens.push(fibbonacci[0])
  end
  
  #swap
  next_fibbonacci = fibbonacci[0] + fibbonacci[1]
  fibbonacci[0] = fibbonacci[1]
  fibbonacci[1] = next_fibbonacci
  
end

puts evens.inject{|sum,x| sum+x }