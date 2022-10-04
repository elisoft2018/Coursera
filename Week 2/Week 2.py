"""i = 0
while i < 5:
    print('Hola Mundo')
    i = i + 1

a = 2
b = 1
c = a / b

#a + spam * 1

#d = '2' + 2

while True:
    try:
        x = int(input('Por favor ingrese un número: '))
        break
    except ValueError:
        print('Oops, el valor es valido....Intenta nuevamente')

def esto_falla():
    x = 1 / 0
try:
    esto_falla()
except ZeroDivisionError as err:
    print('Manejando error en tiempo de ejecución',err)
"""


def dividir(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("¡división por cero!")
    else:
        print("el resultado es", result)
    finally:
        print("ejecutando la clausula finally")

dividir(2,0)




