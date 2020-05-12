# 07/05
# Primi esercizi in Python, Lab. 2

type(5)
# è utile per apire di che tipo è un valore
print(type)

a = 'ciao' # va tra gli apici: «'» o «"»
# è utile usare il doppio apice se abbiamo apostrofi nella stringa
print (a)

c = 'Ciao'
type(c)

x = 47 # è valore «int»
y = 6.9 # è valore «float»

x = 5 # Se cambio valore variabile, Python prende l'ultimo inserito
y = 'ciao'
z = x*y
print(z)
'''
con diviso, meno e potenza («/», «-», «**») dà errore:
non si può divideere stringa per intero;
dà errore anche con somma tra int e string;
è invece utile somma tra stringhe
'''

s = 'Ciao '
u = 'mamma!'
l = s + u
print(l)

# funzione permette di eseguire algoritmo cambiando parametri senza doverlo riscrivere
# «def» serve per definire la funzione
def stampa2volte(stringa):
    print(stringa, stringa)
    
stampa = 'Ohi!'
stampa2volte(stampa)
# parametro funzione non è «stringa», perché è parametro locale, essendo all'interno della funzione
# non posso usare parole riservate come «def»

# posso richiamare funzione all'interno di un'altra funzione
def unione(par_1, par_2):
    union = par_1+par_2
    stampa2volte(union)
    
stampa = 'W Fabrizio '
stampa_2 = 'Miccoli!'
unione(stampa, stampa_2)

# istruzioni condizionali
def n_maggiore_10 (n):
    if n > 10:
        print('Il numero che hai inserito è maggiore di 10')
    elif n == 10: # per il confronto condizionale occorre il doppio uguale
        print ('Il numero è 10')
    else:
        print('Il numero che hai inserito è minore di 10')
        
numero = 10
n_maggiore_10(numero)

# Esercizio: quale dei due numeri è maggiore?
def maggiore(num_1, num_2):
    if num_1 > num_2:
        print('Il primo numero è maggiore del secondo')
    elif num_1 == num_2:
        print('I numeri sono uguali')
    else:
        print('Il secondo numero è maggiore del primo')
        
num1 = 13
num2 = 13
maggiore(num1, num2)

# Esercizio: funzione di controllo di una divisione, per vedere se denominatore = 0
def controllo_divisione (num, denom):
    if denom == 0:
        print('La divisione non si può fare')
    else:
        ris = num/denom # così stampa anche il risultato
        print(ris)

numeratore = 34
denominatore = 10
controllo_divisione(numeratore, denominatore)

# Stampo la stessa cosa, ma facendo uscire «Il risultato è n»
def area_rettangolo(base, altezza):
    area = base*altezza
    print("L'area del rettangolo è: ", area)
    
ba = 20
h = 30
area_rettangolo(ba, h)

# Altrimenti cambio natura della variabile
def area_rettangolo(base, altezza):
    area = base*altezza
    # print(type(area))
    string_area = str(area) # ha trasformato il risultato in stringa!
    # print(type(string_area))
    # string_area = float(area) # l'ha trasformato in decimale!
    # print(string_area)
    print("L'area del rettangolo è: " + string_area) # uso il «+»!
    
ba = 20
h = 30
area_rettangolo(ba, h)

# Posso anche trasformare una stringa in valore intero, purché sia un numero
# funziona anche con il «float»
    
k = '4564' # è una stringa
j = int(k)
# print(type(a))
print(type(j))

# Altrimenti posso farlo direttamente nel print
def area_rettangolo(base, altezza):
    area = base*altezza
    print("L'area del rettangolo è: " + str(area)) # uso il «+»!
ba = 20
h = 30
area_rettangolo(ba, h)

# Cicli di iterazione: «while»
def conto_rovescia (n):
    while n > 0:
        print(n)
        n = n-1 # quest'assegnazione permette di ridurre di uno il valore di n, altrimenti andrebbe all'infinito
    print('Bravo! Sei arrivato a zero.')
    
nc = 10 # questa è una variabile globale
conto_rovescia(nc)

# Liste: serie ordinate di valori all'interno di un unico oggetto
# utili per incapsulare valori come coordinate dei punti o attributi vettori
lista = [2, 4, 6, 7, 8, 9.8]
print(lista)

lista_1 = [1, 3, 4, 5]

# si possono sommare tra loro
lista_unita = lista + lista_1
print(lista_unita)

# Si può pescare il valore della posiizone nella lista
listas = ['Terra', 'Luna']
# print(lista_str)
e = listas [1]
print(e)

# Posso iterare la lista con il ciclo «for»
lista_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for elemento in lista_2:
    print(elemento)

# oppure:
for elemento in lista_2:
    a = elemento + 10
    print(a)
    
# Scrivo funzione che riconosce numeri pari in una lista
def num_pari(lista):
    for numero in lista:
        if numero%2 == 0: # «%» è il modulo, e restituisce il resto tra primo numero diviso il secondo: resto è 0 se numero pari è diviso 2
            print (numero)
        # else:
            # pass --> significa che non fa nulla
        
num_pari (lista_2)

# Per sapere quanti sono creo nuova variabile
def qnum_pari(lista):
    pari = 0
    dispari = 0
    for numero in lista:
        if numero%2 == 0:
            pari = pari + 1
        else:
            dispari = dispari + 1
    print('La lista ha ' + str(pari) + ' numeri pari e ' + str(dispari) + ' numeri dispari.')
        
qnum_pari (lista_2)

# Esiste comando che dà numero massimo di una lista:
print (max(lista_2))
