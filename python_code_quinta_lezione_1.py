import gdal
import os
import numpy
# può anche essere:
#import numpy as np
# in questo caso un righe 21 e 22 dovrei scrivere «np.Float32»

os.chdir('/Users/enricopriarone/Desktop/Lab_2')

sentinel = gdal.Open('montecristo_sentinel.tif')

proj = sentinel.GetProjection()
trans = sentinel.GetGeoTransform()

x = sentinel.RasterXSize
y = sentinel.RasterYSize

banda_red = sentinel.GetRasterBand(3)
banda_NIR = sentinel.GetRasterBand(4)

banda_red_arr = banda_red.ReadAsArray().astype(numpy.float32)
banda_NIR_arr = banda_NIR.ReadAsArray().astype(numpy.float32)
# Così valori sono float e non più in notazione esponenziale

NDVI = (banda_NIR_arr - banda_red_arr)/(banda_NIR_arr + banda_red_arr)
# print(NDVI)
# Dà la possibilità di vedere l'area in base alla vegetazione

driver = gdal.GetDriverByName('GTiff')
NDVI_raster = driver.Create('montecristo_NDVI.tif', x, y, 1, gdal.GDT_Float32)
# «1» indica che lavoriamo solo su una banda (quella dell'NDVI)
# l'ultimo argomento è il tipo di file
NDVI_raster.SetProjection(proj)
NDVI_raster.SetGeoTransform(trans)

banda_NDVI = NDVI_raster.GetRasterBand(1)
banda_NDVI.WriteArray(NDVI)

sentinel = None
NDVI_raster = None

# Una volta caricato il nuovo file «montecristo_NDVI» gli cambio la colorazione:
# «Proprietà --> «Banda singola a falso colore» --> «Viridis»
