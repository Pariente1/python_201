# Los {} se usan tanto para definir los diccionarios como los conjuntos(sets)

# Los conjuntos acepta elementos repetidos o duplicados.

set_countries = {'col', 'mex', 'bol'} 
print(set_countries)
print(type(set_countries))

set_numbers = {1,2,3,4,5,22,234}
print(set_numbers)

set_types = {1, 'hola', False, 12.12}
print(set_types)

set_from_string = set('hoola')
print(set_from_string)

set_from_tuples = set(('abc', 'cbv', 'abc'))
print(set_from_tuples)

numbers = [1,2,3,4,5,5,5,5,5]
set_numbers = set(numbers)
print(set_numbers)

# Ya tenemos en las lineas de arriba una lista, que luego pasamos a un conjunto.
# Como los conjuntos no pueden tener repetidos, podemos volver a convertirlo en lista
#Y asi tendremos una lista sin repetidos.

unique_numbers = list(set_numbers)
print(unique_numbers)
