#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 21:43:30 2020

@author: gautammathur
"""
####################importing required packages##################
import os
from pathlib import Path
import gdal
import numpy as np
import math
###################setting up directory#########################
data = Path(r"/Users/gautammathur/Desktop/Landsat_Aus/tifs")
filenames=os.listdir(data)
os.chdir(data)
#######################setting up variables for names##############
sat='lsat' # what saetllite is it from
desc="_sonoma" # location
date="_10_19_20" # date
ext='.tif' 
bandtypes=["_band1", "band10", "band11",  "_blue", "_green", "_red", "_nir", "_swir1", "_swir2", "_band8", "_band9"] #BEFORE YOU RUN THIS: make sure length/corresponding order of filenames and bandtypes is the same
#######################renaming files#############################
for i in(range(len(filenames))):
    conc= sat + desc + date + bandtypes[i] + ext
    os.rename(data / filenames[i] , data / conc)
######################opening files#################
filenames=os.listdir(data)
band1=gdal.Open(filenames[2]).ReadAsArray().astype(np.float64)
band2=gdal.Open(filenames[5]).ReadAsArray().astype(np.float64)
band3=gdal.Open(filenames[6]).ReadAsArray().astype(np.float64)
band4=gdal.Open(filenames[8]).ReadAsArray().astype(np.float64)
band5=gdal.Open(filenames[7]).ReadAsArray().astype(np.float64)
band6=gdal.Open(filenames[9]).ReadAsArray().astype(np.float64)
band7=gdal.Open(filenames[10]).ReadAsArray().astype(np.float64)
bands=[band1, band2, band3, band4, band5, band6, band7]
##############################extracting info from metadata##########################
metadata=[]
data = Path(r"C:\Users\gmathur\Desktop\landsat")
os.chdir(data)
with open("mtl.txt", "rt") as metafile:
    for lines in metafile:
        metadata.append(lines)
print(metadata)
refmult=metadata[187:194]
refadd=metadata[196:203]
mult=[]
for i in refmult:
    mult.append(float(i[29:]))
add=[]
for i in refadd:
    add.append(float(i[29:]))
########################converting to reflectance and extracting reflectance bands###############
toadd = []
for i  in range(len(bands)):
    toadd.append(bands[i]*mult[i])
todiv=[]
for i in range(len(toadd)):
    todiv.append(toadd[i]+add[i])

    
sunelev=metadata[78] 
a=float(sunelev[20:])
b=math.pi/180
c=math.sin(a/b)
reflectance=[]
for i in range(len(todiv)):
    reflectance.append(todiv[i]/c)
redr=reflectance[3]
bluer=reflectance[1]
greenr=reflectance[2]
nirr=reflectance[4]
swir1r=reflectance[5]
swir2r=reflectance[6]
###################setting up for witing rasters#############################################
##extracting information needed from a reference raster
reference=gdal.Open("red.tif")
gt = reference.GetGeoTransform()
proj = reference.GetProjection()
xsize = reference.RasterXSize
ysize = reference.RasterYSize
nbands = 1
##setting up lists for desired file names and current names of the arrays
outputnames={}
outnames1=["redr", "greenr", "bluer", "nirr", "swir1r", "swir2r"]
outnames=[]
for i in outnames1:
    outnames.append(sat + desc + date + i + ext)
outvar=[redr, greenr, bluer, nirr, swir1r, swir2r]
##creating a dictionary where the desired file name links to the current array name
for i in range(len(outnames)):
    outputnames[outnames[i]] = outvar[i]

#looping through the dictionary to export the rasters
for key in outputnames:
   outf=key
   driver = gdal.GetDriverByName('GTiff')
   output = driver.Create(outf, xsize, ysize, nbands, gdal.GDT_Float64)
   output.SetGeoTransform(gt)
   output.SetProjection(proj)
   output.GetRasterBand(1).WriteArray(outputnames[key])
   output = None