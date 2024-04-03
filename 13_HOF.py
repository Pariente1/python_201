def increment(x):
  return x + 1


increment_v2 = lambda x: x + 1


# hof= higher order function
def hof(x, func):
  print(func)
  return x + func(x)


#hof_v2= lambda x,func: x+ func(x)

result = hof(2, increment)
# 2 + (2 + 1)
#result_2 = hof_v2(2, increment_v2)

print(result)
