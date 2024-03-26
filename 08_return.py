def sum_with_range(min, max):
  print(min,max)
  sum = 0
  for x in range(min, max):

    sum = sum + x
  return sum
    
result = sum_with_range(1,10)
print(result)
result2 = sum_with_range(result, result + 5)
print(result2)

