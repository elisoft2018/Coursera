frutas = {'manzana', 'pera', 'naranja', 'kiwi', 'uvas', 'naranja', 'pera', 'uvas'}
print(frutas)
print('manzana' in frutas)
print('mandarina' in frutas)
a = set('abracadabra')
b = set('alakazam')
print(a)
print(b)
print(a - b)  # Letras en a pero no en b
print(a | b)  # Letras en a o en b o en ambas
print(a & b)  # Letras en a y en b
print(a ^ b)  # Leras en a o b pero no en ambos

# Comprensión de conjuntos
c = {x for x in a if x not in 'abc'}
print(c)
c.add('w')
print(c)
c.remove('r')
print(c)
