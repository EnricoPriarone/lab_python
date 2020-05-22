# Seguiamo un tutorial presente nel Cookbook di gdal
import gdal, ogr, osr # si può fare insieme perché tipo libreria è uguale
# osr serve per gestione sistemi di riferimento
import os
import csv

os.chdir('/Users/enricopriarone/Desktop/Lab_2/shp')

# apro il driver
driver = ogr.GetDriverByName('ESRI Shapefile')

# apro il file
shapefile = driver.CreateDataSource('punti_quotati.shp')

# apro il file csv
csvfile = open('coordinate_header.csv')
reader = csv.DictReader(csvfile, delimiter = ',')
# si può fare in un'unica riga:
# reader = csv.DictReader(open("coordinate_header.csv",delimiter = ',')

# uso osr e poi definisco il sistema di riferimento
SR = osr.SpatialReference()
SR.ImportFromEPSG(32632)

layer = shapefile.CreateLayer('punti_quotati', SR, ogr.wkbPoint)
# l'ultimo argomento definisce il tipo di layer:
# questo è shp puntuale (ma volendo posso fare anche poligonale o lineare)

# aggiungiamo i campi dello shp
# e ne definisco tipo (int, real, float ecc.) e lunghezza (se string)
# creo il primo
name_field = ogr.FieldDefn('ID', ogr.OFTString)
name_field.SetWidth(24)
layer.CreateField(name_field)

# creo gli altri
name_field_1 = ogr.FieldDefn('xcoord', ogr.OFTReal)
layer.CreateField(name_field_1)
# ora faccio tutto in un'unica riga
layer.CreateField(ogr.FieldDefn('ycoord', ogr.OFTReal))
layer.CreateField(ogr.FieldDefn('Altitudine', ogr.OFTInteger))

# gestisco il file csv
# scrive ogni riga del csv nella tabella in QGIS
for row in reader:
    layer_defn = layer.GetLayerDefn()
    feature = ogr.Feature(layer_defn)
    feature.SetField('ID', row['id'])
    feature.SetField('xcoord', row['xcoord'])
    feature.SetField('ycoord', row['ycoord'])
    feature.SetField('Altitudine', row['quota'])
    
    # crea la geometria
    wkt = "POINT(%f %f)" %  (float(row['xcoord']) , float(row['ycoord']))
    # è modo più rapido di scrivere una stringa («wkt» è string
    
    # oppure
    wkt_new = 'POINT (' + str(row['xcoord']) + ' ' + str(row['ycoord']) + ')'
    point = ogr.CreateGeometryFromWkt(wkt)
    feature.SetGeometry(point)
    
    layer.CreateFeature(feature)
    
    feature = None

shapefile = None
