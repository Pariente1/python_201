set_countries = {'col', 'mex', 'bol'} 

size = len(set_countries)
print(size)

print('col' in set_countries)
print('pe' in set_countries)

#add
set_countries.add('pe')
print(set_countries)

#Si intentamos agregar una segunda ve 'pe' no lo va a tomar en cuenta por la 
#naturaleza de los conjuntos(set)

set_countries.add('pe')
print(set_countries)

#update

set_countries.update({'ar', 'ec', 'pe'})
print(set_countries)

#remove

set_countries.remove('ar')
print(set_countries)

set_countries.remove('col')
print(set_countries)

# si intentas eliminar un elemento que no este dentro del conjunto arrojara error.

#set_countries.remove('asas')
#print(set_countries)

# para poder eliminarlos sin tener error tienes que usar el metodo .discard

set_countries.discard('asas')
print(set_countries)

# para borrar todo el contenido usamos el metodo .clear

set_countries.clear()
print(len(set_countries))