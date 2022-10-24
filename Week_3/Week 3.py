import math
from collections import deque
from math import pi

print('Frutas')
fruits = ['Banana', 'Orange', 'Apple', 'Banana']
vegetables = ['Tomatoes', 'Onion']
print('la fruta Banana esta ', fruits.count('Banana'), 'veces en la lista')
print('Banana esta en la posición ', fruits.index('Banana'))
print('Banana esta en la posición ', fruits.index('Banana', 1))

fruits.reverse()
print(fruits)
fruits.append('Tangelo')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop(0))
print(fruits)
fruits.insert(4, 'PinneApple')
print(fruits)
fruits.remove('Orange')
print(fruits)
fruits.copy()
print(fruits)
fruits.extend(vegetables)
print(fruits)
# fruits.clear()
# print(fruits)
stack = [1, 2, 3]
stack.append(4)
stack.append(5)
stack.append(6)
print(stack)
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack)
print()
queue = deque(['John', 'Javier', 'Jose'])
queue.append('Andrea')
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)
print()
cuadrados = []
for i in range(10):
    cuadrados.append(i ** 2)
print(cuadrados)
cuadrados = list(map(lambda x: x ** 2, range(11)))
print(cuadrados)
cuadrados = [x ** 2 for x in range(12)]
print(cuadrados)
print()
combinaciones = [(x, y) for x in [1, 2, 3] for y in [2, 3, 4] if x != y]
print(combinaciones)
combinaciones = []
for x in range(4):
    for y in range(3):
        if x != y:
            combinaciones.append((x, y))
print(combinaciones)
print()
vec = [-2, -4, 0, 2, 4]
vec1 = [x * 2 for x in vec]
print(vec1)
vec2 = []
for x in vec:
    vec2.append(x * 2)
print(vec2)
vec3 = []
for x in vec:
    if x >= 0:
        vec3.append(x)
print(vec3)
vec4 = []
for x in vec:
    vec4.append(abs(x))
print(vec4)
vec5 = [x for x in vec if x >= 0]
print(vec5)
vec6 = [abs(x) for x in vec]
print(vec6)
print()
frutafresca = ['  Banana', '    Mora de logan', '   Maracuya']
frutafresca = [x.strip() for x in frutafresca]
print(frutafresca)
frutafresca1 = []
for x in frutafresca:
    frutafresca1.append(x.strip())
print(frutafresca1)
print()
tuplaNumerica = [(x, x ** 2) for x in range(7)]
print(tuplaNumerica)
tuplaNumerica1 = []
for x in range(8):
    tuplaNumerica1.append((x, x ** 2))
print(tuplaNumerica1)

vecs = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
vecs1 = [num for elem in vecs for num in elem]
print(vecs1)
print()
pi4 = [str(round(pi, i)) for i in range(1, 6)]
pi3 = []
for i in range(1, 6):
    pi3.append(round(pi, i))
print(pi3)
print()
print(pi4)
print('Listas anidadas')
matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]
matriz1 = [[fila[i] for fila in matriz] for i in range(4)]
print(matriz1)
transpuesta = []
for i in range(4):
    transpuesta.append([fila[i] for fila in matriz])
print(transpuesta)
print('')
transpuesta2 = []
for i in range(4):
    fila_traspuesta = []
    for fila in matriz:
        fila_traspuesta.append(fila[i])
    transpuesta2.append(fila_traspuesta)
print(transpuesta2)
print('')
print(list(zip(*matriz)))
print()
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0:2]
print(a)
del a[:]
print(a)
# del a
# print(a)
print()
a_list = [3, 7.5, 'Hola', 7j+5, [1, 4]]

# Indexacion access
print(a_list)
print(a_list[0])
print(a_list[2])
print(a_list[-1])
print()

# slicing
print(a_list[1:])
print(a_list[1:2])
print(a_list[1:3])
print(a_list[:2])
print(a_list[:])

# someone functions
# elements quota
print(len(a_list))
# element add to list
a_list.append('Pruebas')
print(a_list)
# Extiende la lista con elementos de otra lista
a_list.extend([1, 4])
print(a_list)

# Insert element in specific position
a_list.insert(4, 'Posicion')
print(a_list)
a_list.insert(20, 'Fuera de rango')
a_list.insert(-1, 'Posicion Negativa')
print(a_list)
# Cuenta el numero de elementos de la lista que coincidan con el parámetro enviado
print(a_list.count(4))

# Elimina el primer elemento de la lista que coincida con el parametro pasado
a_list.remove(3)
print(a_list)
# Realizar copia superficial de una lista
a_list_copy = a_list.copy()
print(a_list_copy)
a_list_copy.append('Elemento de la copia de lista')
print(a_list_copy)
print(a_list)
# Sacar y retornar el último elemento de la lista
print(a_list.pop())
print(a_list_copy.pop())
# Sacar y retornar el elemento de la lista de acuerdo a la posición enviada en el parametro
print(a_list.pop(2))
print(a_list_copy.pop(4))
# Limpiar la lista
a_list.clear()
print(a_list)
print(a_list_copy)
