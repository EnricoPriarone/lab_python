import gdal
import os
import numpy # serve per gestire gli array con classe «numpy.ndarray»

os.chdir('/Users/enricopriarone/Desktop/Lab_2')

# apro il file
dataset = gdal.Open('Montecristo.tif')

# Ottengo il metadato
# che può essere poi elaborato
metadata = dataset.GetMetadata()
print(metadata)

# Per vedere la proiezione (cerco il GDAL Cookbook):
proiezione = dataset.GetProjection()
print(proiezione)

# Per passare da coordinate cartografiche a coordinate in pixel:
# coordinate in alto a sx dell'immagine! primo=x, secondo= valore px in gradi, quarto=y
transform = dataset.GetGeoTransform()
print(transform)

# cerco numero di pixel su x e y
x = dataset.RasterXSize
y = dataset.RasterYSize
print(x,y)

# Per lavorare con le bande/i singoli pixel del raster
# bisogna dare argomento con numero della banda (qui la 1)
banda = dataset.GetRasterBand(1)
print(banda)

# trasformo tipo «GDALRasterBandShadow» in un array
banda_array = banda.ReadAsArray()
print(banda_array[52][64])
# se lo lascio generico finisco in mare; mettendo valori specifici posso ovviare
#print(type(banda_array))
# è clase «numpy.ndarray»

# Aggiungo 100 a tutti i valori
somma = banda_array + 100
print(banda_array [45][47], somma[45][47])

# Riproietto il raster in un altro sistema di riferimento
output = 'montecristo_reprojected.tif'
# gdal.Warp(output, dataset, dstSRS = 'EPSG:32632')
# è cambiata anche l'unità di misura di coordinate e pixel (in «Proprietà»)

raster32632 = gdal.Open(output)
proj = raster32632.GetProjection()
print(proj)
# proiezione è cambiata
trans = raster32632.GetGeoTransform()
print(trans)
# abbiamo valori in coordinate metriche!

no_data_output = 'montecristo_no_data.tif'
# gdal.Translate(no_data_output, raster32632, noData=0)
# ha assegnato valore noData ai pixel corrispondenti al mare!

# L'immagine Sentinel acquisisce per ogni banda un valore dello spettro elettromagnetico
# Array devono avere le stesse dimensioni

# Chiudo
dataset = None


# Seconda parte

import gdal
import os
import numpy

os.chdir('/Users/enricopriarone/Desktop/Lab_2')

sentinel = gdal.Open('montecristo_sentinel.tif')

# assegno valori su x e y uguali a quelle del file originario
x = sentinel.RasterXSize
y = sentinel.RasterYSize
# lavoro su red (banda 3) e NIR (banda 4)
banda_red = sentinel.GetRasterBand(3)
banda_NIR = sentinel.GetRasterBand(4)

# per fare il calcolo le apro come array
banda_red_arr = banda_red.ReadAsArray()
banda_NIR_arr = banda_NIR.ReadAsArray()
print(banda_red_arr)
print(banda_NIR_arr)

# calcolo l'indice NDVI
# NDVI = (banda NIR - banda red)/(banda NIR + banda red)
NDVI = (banda_NIR_arr - banda_red_arr)/(banda_NIR_arr + banda_red_arr)
print(NDVI)

# Salvo l'array dentro il raster, creandone uno da zero
driver = gdal.GetDriverByName('GTiff') # perché l'estensione del file è GeoTiff
out_raster = driver.Create('montecristo_NDVI.tif', x, y, 1, gdal.GDT_Float32)
# per definire numero di pixel in x e y prendo il numero dell'immagine originale
# e scrivo «x» e «y»
