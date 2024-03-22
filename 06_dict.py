import random 

'''
countries = ['col', 'mex', 'bol', 'pe']

population_v2 = {country: random.randint(1,100) for country in countries}
#print(population_v2)

result = {country: population for (country, population) in population_v2.items() if population > 90}
print(result)


text = 'hola, soy Nicolas'
unique = { c: c.upper() for c in text if not c in 'aeiou'}
print(unique)

'''

numbers = [35, 16, 10, 34, 37, 25]

even_numbers = []
for number in numbers:
  if number % 2 == 0:
    even_numbers.append(number)
print('v1 =>', even_numbers)

# Ahora usando List Comprehension 👇
even_numbers_v2 = [n for n in numbers if n % 2 == 0]

print('v2 =>', even_numbers_v2)
