# 14/05
import csv
import os

os.chdir('/Users/enricopriarone/Desktop/Lab_2')

'''
csv_file = open('coordinate_punti_1.csv')
coordinate = csv.reader(csv_file, delimiter = ',') # con «delimiter» indico separatore
print(csv_file)

csv_newfile = open('nuovo_csv.csv', 'w') # crea nuovo file
writer = csv.writer(csv_newfile, delimiter = ',')

list = []
for row in coordinate:
    list.append(row)
print(list[1])

header = ['id', 'xcoord', 'ycoord', 'quota']
writer.writerow(header)
writer.writerows(list) # occhio al plurale!
# occorre ciudere i due file prima di completare
csv_file.close()
csv_newfile.close()
'''

csv_file = open('nuovo_csv.csv', 'r')
coordinate = csv.reader(csv_file, delimiter = ',')

'''
coordinate = csv.DictReader(csv_file, delimiter = ',')
# «DictReader» serve a trasformare i numeri in int, associandoli alle string nell'header;
# cambia la tipologia al valore

for row in coordinate:
    print(row)
    # print(type(row))
    #a = quota + 100


lista = []
for row in coordinate:
    quota = int(row['quota'])
    # print(quota)
    # stampa la colonna ma senza la prima riga!
    a = quota + 100
    lista.append(a)
    
print(lista)
'''
# Aggiungiamo una colonna con quota ellissoidica
lista = []
for row in coordinate:
    try: # prova a fare un certo comando
        elips = int(row[3]) + 47
        row.append(elips)
        lista.append(row)
        # print(row)
    except:
        pass # Se non riesce passa oltre (serve per saltare la riga «quota»)
        
header = ['id', 'xcoord', 'ycoord', 'quota_geo', 'quota_el']
csvfile_write = open('coordinate_nuova_colonna.csv', 'w')
writer = csv.writer(csvfile_write)
writer.writerow(header)
writer.writerows(lista)
csv_file.close()
csvfile_write.close()
