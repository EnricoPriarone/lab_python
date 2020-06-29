'''
Scrivere una UNICA funzione in cui viene interrogato il DEM
andando ad aggiungere ad ogni csv il valore di quota corrispondente alle coordinate indicate,
successivamente trasformare i csv in shapefile.
Gli shapefile finali dovranno avere tutti gli attributi presenti nei csv iniziali con aggiunta la quota.
Sarà quindi necessario ripetere il procedimento su tutti i file della cartella utilizzando il ciclo glob.
ATTENZIONE il DEM ha un sistema di riferimento (UTM ED50 32N) differente da quello delle coordinate dei csv (UTM WGS84 32N),
sarà quindi necessario riproiettarlo (questo lo potete fare all'esterno della funzione).
'''

# Importo tutte le librerie necessarie, e forse anche di più
from osgeo import gdal, gdal_array
import ogr, osr
import os
import numpy as np
import glob
import csv

# Definisco la cartella di lavoro
os.chdir('/Users/enricopriarone/Desktop/Lab_2/es')



#### Prima parte

# Per prima cosa riproietto il dem: da ED50 32N a WGS84 32N (EPSG:32632)

# Apro il file
dataset = gdal.Open('dem_lombardia_100m_ED32N.tif')


# Riproietto il raster in un altro sistema di riferimento
output = 'dem_lombardia_100m_WGS84_32N.tif'
gdal.Warp(output, dataset, dstSRS = 'EPSG:32632')
# è cambiata anche l'unità di misura di coordinate e pixel (in «Proprietà»)

# Chiudo il file
dataset = None




#### Seconda parte

# Creo un'unica funzione che aggiunga la quota ai csv (creandone nuovi) e trasformi i nuovi file in .shp
def agg_quota(csv_file, raster):
    ### Aggiungo la quota ai .csv
    
    # Apro il csv e lo leggo con DictReader
    csvfile_read = open(csv_file) 
    reader = csv.DictReader(csvfile_read, delimiter = ',')
    
    # Apro il dem, ne estraggo la GeoTransform e la banda 1
    dem = gdal.Open(raster)
    gt = dem.GetGeoTransform()
    band = dem.GetRasterBand(1)
    
    # Definisco i campi del nuovo csv
    fields = ['COD_REG', 'COD_CM', 'COD_PRO', 'PRO_COM', 'COMUNE', 'NOME_TED', 'FLAG_CM', 'SHAPE_Leng', 'SHAPE_Area', 'xcoord', 'ycoord', 'Quota']
    # Creo la lista vuota che poi scriverò nel nuovo csv
    lista = []
    
    # Uso un ciclo for per il nuovo file che sia uguale al precedente ma con in più la quota
    for row in reader:
        # Creo la lista della riga da creare a ogni ciclo
        list_row = []
        # Prendo le coordinate x e y dal csv
        utm_x = float(row['xcoord'])
        utm_y = float(row['ycoord'])
        # Calcolo le coordinate (x e y) pixel riferite alla coordinate prese dal csv
        px = int((utm_x-gt[0])/gt[1])
        py = int((utm_y-gt[3])/gt[5])
        
        # Leggo la banda come un array e prendo in considerazione il pixel che mi serve, poi lo trasformo in intero
        quota = band.ReadAsArray(px,py,1,1)
        # print(quota)
        q = int(quota)
        # print(q)
        
        # Aggiungo a «list_row» tutti gli elementi della riga per poter formare una lista
        list_row.append(row['COD_REG'])
        list_row.append(row['COD_CM'])
        list_row.append(row['COD_PRO'])
        list_row.append(row['PRO_COM'])
        list_row.append(row['COMUNE'])
        list_row.append(row['NOME_TED'])
        list_row.append(row['FLAG_CM'])
        list_row.append(row['SHAPE_Leng'])
        list_row.append(row['SHAPE_Area'])
        list_row.append(row['xcoord'])
        list_row.append(row['ycoord'])
        list_row.append(q)
        # Aggiungo «list_row» a lista per formare una lista di liste da scrivere nel csv
        lista.append(list_row)
        
    # Scrivo la lista di liste e l'header nel csv
    # Definisco il nome del nuovo file aggiungendo una parte al nome di quello vecchio
    name = csv_file.split('.')[0] + '_q.csv'
    csvfile_write = open(name,'w') 
    writer = csv.writer(csvfile_write)
    writer.writerow(fields) 
    writer.writerows(lista)
    
    # Chiudo i file
    csvfile_read.close()
    csvfile_write.close()


    ### Trasformo i .csv in .shp
    
     # Creo il nuovo shapefile definendone il driver e il datasource
    driver = ogr.GetDriverByName('ESRI Shapefile')
    shapefile = driver.CreateDataSource(name.split('.')[0] + '_punti_quotati.shp')

    # Apro e leggo il file csv con DictReader
    csvfile = open(name)
    reader = csv.DictReader(csvfile, delimiter = ',')


    # Definisco il sistema di riferimento che poi inserirò nel layer
    SR = osr.SpatialReference()
    SR.ImportFromEPSG(32632)

    # Creo il layer definendo nome, sistema di riferimento e tipologia di geometria
    layer = shapefile.CreateLayer(name.split('.')[0] + '_punti_quotati.shp', SR, ogr.wkbPoint) 
    
    # Definisco nome e tipologia dei vari campi della tabella attributi e li creo
    layer.CreateField(ogr.FieldDefn('Cod_reg', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('Cod_cm', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('Cod_pro', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('Pro_com', ogr.OFTInteger))
    name_field = ogr.FieldDefn('Comune', ogr.OFTString)
    name_field.SetWidth(34) # Definisco lunghezza massima della stringa
    layer.CreateField(name_field)
    layer.CreateField(ogr.FieldDefn('Nome_Ted', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('Flag_cm', ogr.OFTInteger))
    layer.CreateField(ogr.FieldDefn('Shape_Leng', ogr.OFTReal))
    layer.CreateField(ogr.FieldDefn('Shape_Area', ogr.OFTReal))
    name_field_1 = ogr.FieldDefn('xcoord', ogr.OFTReal)
    layer.CreateField(name_field_1)
    layer.CreateField(ogr.FieldDefn('ycoord', ogr.OFTReal))
    layer.CreateField(ogr.FieldDefn('Quota', ogr.OFTInteger))

    # Faccio un ciclo for per scrivere ogni riga del csv nella tabella attributi del layer
    for row in reader:
        # Estraggo la definizione del layer
        layer_defn = layer.GetLayerDefn()
        # Definisco la feature all'interno della definizione dal layer
        # e ne imposto il valore nei vari campi della tabella degli attributi
        feature = ogr.Feature(layer_defn)
        feature.SetField('Cod_reg', row['COD_REG'])
        feature.SetField('Cod_cm', row['COD_CM'])
        feature.SetField('Cod_pro', row['COD_PRO'])
        feature.SetField('Pro_com', row['PRO_COM'])
        feature.SetField('Comune', row['COMUNE'])
        feature.SetField('Nome_Ted', row['NOME_TED'])
        feature.SetField('Flag_cm', row['FLAG_CM'])
        feature.SetField('Shape_Leng', row['SHAPE_Leng'])
        feature.SetField('Shape_Area', row['SHAPE_Area'])
        feature.SetField('xcoord', row['xcoord'])
        feature.SetField('ycoord', row['ycoord'])
        feature.SetField('Quota', row['Quota'])
        
        # Scrivo la geometria in linguaggio wkt
        wkt = "POINT(%f %f)" %  (float(row['xcoord']) , float(row['ycoord']))
        # Creo la geometria dalla sringa scritta in wkt
        point = ogr.CreateGeometryFromWkt(wkt)
        # Assegno la geometria creata alla feature
        feature.SetGeometry(point)
        
        # Creo la feature (con attributi e geometria) all'interno del layer
        layer.CreateFeature(feature)
        # Svuoto la variabile feature e faccio ripartire il ciclo for
        feature = None

    # Chiudo e salvo il datasource
    shapefile = None
    
# agg_quota ('comuni_lomb_cremona.csv', 'dem_lombardia_100m_WGS84_32N.tif')

# Faccio il ciclo glob per richiamare nella funzione «agg_quota» il dem riproiettato e via via i vari csv presenti nella cartella
for doc in glob.glob('*csv'):
    dem = 'dem_lombardia_100m_WGS84_32N.tif'
    agg_quota (doc, dem)
