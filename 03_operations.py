set_a = {'col', 'mex', 'bol'}

set_b = {'pe', 'bol'}

#union

set_union = set_a.union(set_b)
print(f'\n aqui se imprime la union: {set_union} \n')

# tambien se puede hacer con el operador | que significa union:

print(set_a | set_b)

#intersection

set_intersection = set_a.intersection(set_b)
print(f'Aqui se imprime la intersection:\n{set_intersection}\n')

# La intersection tambien se puede hacer con el operador &:

print(set_a & set_b)

# diferencia

set_difference = set_a.difference(set_b)
print(set_difference)

# La diferencia tambien la podemos usar el operador - :

print(set_a - set_b)

# Diferencia simetrica o Symmetric Difference

set_SymDiff = set_a.symmetric_difference(set_b)
print(set_SymDiff)

# La symmetric_difference se puede hacer con el operador ^ :
# Consiste en encontrar los elementos que son exclusivos de un conjunto o de otro. 
# O tambien comprar dos conjuntos y encontrar los elementos que son diferentes.
print(set_a ^ set_b)

