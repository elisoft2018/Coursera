import csv

print('OBJETO READER')
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

print('\n')
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

print('\n')

with open('Libreria.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in reader:
        print(', '.join(row))

print('\n')

csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('Libreria.csv', newline='') as f:
    reader = csv.reader(f, 'unixpwd')
    for row in reader:
        print(row)

print('\nOBJETO DICTREADER')

with open('Libreria.csv', newline='') as csvfiles:
    reader = csv.DictReader(csvfiles)
    for row in reader:
        print(row['Nombre'], row['Apellido'])

