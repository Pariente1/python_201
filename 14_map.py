numbers = [1,2,3,4,5,6,7]
numbers_v2 = []


for i in numbers:
  numbers_v2.append(i*2)

numbers_v3= list(map(lambda i: i*2, numbers))

print(numbers)
print(numbers_v2)
print(numbers_v3)

numbers_1 = [1,2,3,4,5]
numbers_2= [5,6,7]

# va a iterar las 2 listas, pero nos va a retornar la suma de cada uno de sus iteraciones solo que tomara
#la mas corta
result = list(map(lambda x,y: x+y, numbers_1, numbers_2))
print(result)
