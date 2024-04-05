import functools

numbers = [1,2,3,4]

'''
def accum(counter, item): 
  print('counter', counter)
  print('item', item)
  return counter + item
'''

def accum(items, it):
  print('counter', it)
  print('items', items[it])
  return it + items[it]
    
    

it = 0
for number in numbers:
  result = accum(numbers, it)
  it = it + 1
  print(result)
  
  
#result = functools.reduce(lambda counter, item: counter + item, numbers)

#result = functools.reduce(accum, numbers)

#result = accum(numbers)


