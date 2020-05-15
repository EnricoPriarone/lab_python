# Comandi che servono a importare librerie e moduli esterni
import math

a = 58
b = math.sqrt(a)
# indico modulo, comando (radice quadrata) e varibile
print(b)

c = math.pi
print(c)

# Scrivere funzione che calcoli la circonferenza di un cerchio
# r = 5
def crf_cerchio(raggio):
    crf = 2*math.pi*raggio
    print(crf)

r = 5
crf_cerchio(r)

def area_cerchio(raggio):
    a = math.pi*r**2
    print(a)

r = 5
area_cerchio(r)

# Importo modulo che permette di creare numeri pseudocasuali
import random

a = random.random()
# Genera numero casuale tra 0 e 1
print(a)

# «range» permette di richiamare numeri tra 0 e il numero massimo che vogliamo
# con «rand.range»
for n in range(20):
    print(n)
    
# Stampiamo numero casuale tra 0 e 100
for n in range(10):
    a = random.randrange(1, 100)
    print(a)

# Creo una lista di valori casuali
# con «append»
for n in range(10):
    lista = []
    a = random.randrange(1, 100)
    lista.append(a)
print(lista)

# Indovinare numero in una lista pseudocasuale
def indovina_numero(n):
    lista = []
    for a in range(10):
        a = random.randrange(1,100)
        lista.append(a) # Attacca un elemento alla lista
    if n in lista:
        print('Bravo! Hai indovinato.')
        print(lista)
    else:
        print('Hai sbagliato! Riprova.')
        
numero = 45
indovina_numero(numero)

# Comando che serve per dialogare con il programma
# «input»
def indovina_numero(n):
    lista = []
    for a in range(10):
        a = random.randrange(1,100)
        lista.append(a)
    if n in lista:
        print('Bravo! Hai indovinato.')
        print(lista)
    else:
        print('Hai sbagliato! Riprova.')

# numero = input('Inserisci numero.')
# indovina_numero(numero)
# In QGIS non funziona, ma la sintassi è questa

# «insert» permette di aggiungere nuovo elemento in lista dove voglio
lista = [9, 8, 45]
a = 'pala'
lista.insert(2, a)
print(lista)
# ???

# Importiamo file .csv con coordinate punti
# usiamo «open»
import csv
import os

# definisco cartella di lavoro per permettermi di scrivere solo nome file per richiamarlo
os.chdir('/Users/enricopriarone/Desktop/Lab_2')

csv_file = open('coordinate_punti_1.csv')
# è un tipo particolare, quindi devo fare qualche passaggio:
coordinate = csv.reader(csv_file, delimiter = ',') # con «delimiter» indico separatore
print(csv_file)

# stampiamo ogni riga del file
for row in coordinate:
    print(row)

# oppure una sola colonna:
for row in coordinate:
    print(row[3])

# aggiungo una riga in cima, creando un «writer»
csv_newfile = open('nuovo_csv.csv', 'w') # crea nuovo file
writer = csv.writer(csv_newfile, delimiter = ',')

# creo lista
list = []
for row in coordinate:
    list.append(row)
print(list[1])

# Aggiungo prima riga attraverso una lista
header = ['id', 'xcoord', 'ycoord', 'quota']
writer.writerow(header)
writer.writerows(list)
# occorre ciudere i due file prima di completare
csv_file.close()
csv_newfile.close()
