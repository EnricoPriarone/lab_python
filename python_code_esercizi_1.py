# Esercizio 1:
# Scrivi una funzione che prende come parametro
# la temperatura in gradi Celsius e la trasforma in gradi Fahrenheit.
# Fahrenheit = (9*Celsius + (32*5))/5

def celsius_fahr (cels):
    fahr = (9 * cels + (32*5))/5
    print(str(cels) + ' gradi Celsius equivangono a ' + str(fahr) + ' gradi Fahrenheit.')

c = 2
celsius_fahr(c)


# Esercizio 2:
# Scrivi una funzione che prende tre numeri come parametri
# e restituisce il più grande tra loro.
# Utilizzare «AND»

def num_max (num_1, num_2, num_3):
    if num_1 >= num_2  and num_1 >= num_3:
        print('Il numero maggiore è ' + str(num_1))
    elif num_2 >= num_3 and num_2 >= num_1:
        print('Il numero maggiore è ' + str(num_2))
    elif num_3 >= num_1 and num_3 >= num_2:
        print('Il numero maggiore è ' + str(num_3))
  
n1 = 17
n2 = 1
n3 = 17
num_max(n1, n2, n3)


# Esercizio 3:
# Scrivi un programma che, passata come parametro una lista,
# elevi al quadrato tutti gli elementi della stessa.

def elevam_lista(lista):
    for elemento in lista:
        quadr = elemento ** 2
        print('Il quadrato di: ' + str(elemento) + ' è ' + str(quadr))
        
lista_1 = [2, 4, 6, 3]
elevam_lista(lista_1)


# Esercizio 4:
# Scrivi un programma che, passata come parametro una lista di interi,
# fornisce in output il maggiore tra i numeri contenuti nella lista.

def max_lista(lista):
    max = 0
    for elemento in lista:
        if elemento > max:
            max = elemento
    print('Il numero maggiore della lista è: ' + str(max))

lista_2 = [9, 6, 7, 2]
max_lista(lista_2)

# Esercizio 5:
# Scrivi una funzione che, prese come parametri due liste,
# restituisce il numero di combinazioni tra elementi comuni tra le due liste.
# Usare due cicli FOR uno dentro l'altro per confrontare tutti i valori delle due liste.

def comb_liste (lista_a, lista_b):
    num_comb = 0
    for num_a in lista_a:
        for num_b in lista_b:
            if num_a == num_b:
                num_comb = num_comb + 1
    print ('Le liste hanno ' + str(num_comb) + ' numeri in comune.')
    
lista_x = [1, 5, 90, 12, 3]
lista_y = [5, 90, 8, 24, 12, 5, 1, 3]
comb_liste(lista_x, lista_y)
