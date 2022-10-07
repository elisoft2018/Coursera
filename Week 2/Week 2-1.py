import math

s = "Hola Mundo"
print(str(s))
print(repr(s))
print(str(1 / 7))

print('\n')

x = 10 * 3.25
y = 200 * 200
s = 'El valor de x es ' + repr(x) + ', y es ' + repr(y) + '....'
print(s)

print('\n')

hola = 'hola mundo\n'
holas = repr(hola)
print(holas)

print('\n')

print(repr((x, y, ('carne', 'huevos'))))

print('\n')

for x in range(1, 11):
    print(repr(x).rjust(2), repr(x * x).rjust(3), end='')
    print(repr(x * x * x).rjust(4))

print('\n')

for x in range(1, 11):
    print('{0:2d},{1:3d},{2:4d}'.format(x, x * x, x * x * x))

print('\n')

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.1443445455'.zfill(5))

print('\n')

print('Los {}  somos quienes decimos {}'.format('Caballeros', 'No!'))
print('{0} y {1}'.format('Carne', 'Huevo'))
print('la {comida} es {adjetivo}'.format(comida='Carne', adjetivo='espantosa'))
print('El {animal} es un {0} del {1}'.format('hervivoro', 'campo', animal='Caballo'))

print('\n')

contents = 'anguilas'
print('mi aerodeslizador esta lleno {}'.format(contents))
print('my hovercraft is full {!r}.'.format(contents))

print('\n')

print('el valor de PI es aproximadamente {0:.3f}'.format(math.pi))

print('\n')

tabla = {'John': 4350, 'Eliseo': 3435, 'Andres': 5456}
for nombre, telefono in tabla.items():
    print('{0:10} ===> {1:10d}'.format(nombre, telefono))
print('John: {0[John]:d};Eliseo: {0[Eliseo]:d};Andres: {0[Andres]:d}'.format(tabla))
print('John:{John:d};Eliseo:{Eliseo:d};Andres:{Andres:d}'.format(**tabla))

