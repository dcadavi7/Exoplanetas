# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:33:10 2019

@author: Daniela
"""

#Functions

global Sector
global Time
global Flux
global Writexl
global Error
global ID
global Quantity

def ligthcurve(Telescope,Method,Planet,Quantity,i):
    
    Flux = 0
    Time = 0
    Error = 0
    
    if Telescope == Satellite1 and Method == Discmethod:
        
        try:
            
            lcf = search_lightcurvefile(Planet,mission='Kepler').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
        
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err

            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)
        
        except KeyError:
            
            RA = hoja.cell(row = i, column = 16) 
            Dec = hoja.cell(row = i, column = 18) 
            
            Coordenada = str(RA.value) +" " + str(Dec.value)
            
            lcf = search_lightcurvefile(Coordenada,mission='Kepler').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
        
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err
            
            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)
            
        except Exception as e:
            print(str(e))

#-------------------------------------------------------------------------
            
    elif Telescope == Satellite2 and Method == Discmethod:
        
        try:
            
            lcf = search_lightcurvefile(Planet,mission='K2').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
        
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err
    
            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)
        
        except KeyError:
            
            RA = hoja.cell(row = i, column = 16) 
            Dec = hoja.cell(row = i, column = 18) 
            
            Coordenada = str(RA.value) +" " + str(Dec.value)
            
            lcf = search_lightcurvefile(Coordenada,mission='K2').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
        
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err
            
            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)

        except Exception as e:
            print(str(e))
        
#-------------------------------------------------------------------------------

    elif Telescope == Satellite3 and Method == Discmethod:
        
        try:
            
            lcf = search_lightcurvefile(Planet,mission='TESS').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
        
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err

            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)
        
        except KeyError:
            
            RA = hoja.cell(row = i, column = 16) 
            Dec = hoja.cell(row = i, column = 18) 
            
            Coordenada = str(RA.value) +" " + str(Dec.value)
            
            lcf = search_lightcurvefile(Coordenada,mission='TESS').download_all(download_dir = MAST)
                
            lc = lcf.PDCSAP_FLUX.stitch().remove_nans().remove_outliers().flatten(window_length = 1001, polyorder = 3, niters=5)
            
            Time = lc.time
            Flux = lc.flux
            Error = lc.flux_err
            
            Writexl = hoja.cell(row = i, column = 25) 
            Writexl.value = "Found"
            
            createfile(Planet,Time,Flux,Error,Quantity)

        except Exception as e:
            print(str(e))
            
#--------------------------------------------------------------------------------

    else:
        Writexl = hoja.cell(row = i, column = 25) 
        Writexl.value = "No search"
        
#--------------------------------------------------------------------------------

def createfile(Planetfile,Timefile,Fluxfile,Errorfile,Quantity):
    
    print(" ")
    print(i)
    print(Planet.value)
    
    if Quantity == 1:
        
        save_path = path + "\Planet_1"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    elif Quantity == 2:
        
        save_path = path + "\Planet_2"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    elif Quantity == 3:
        
        save_path = path + "\Planet_3"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    elif Quantity == 4:
        
        save_path = path + "\Planet_4"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    elif Quantity == 5:
        
        save_path = path + "\Planet_5"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    elif Quantity == 6:
        
        save_path = path + "\Planet_6"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
        
    elif Quantity == 7:
        
        save_path = path + "\Planet_7"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
    
    elif Quantity == 8:
        
        save_path = path + "\Planet_8"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1) 
        
    else:

        save_path = path + "\Other"
        
        file = save_path+'\\'+Planetfile+".txt" 
        np.savetxt(file, (Fluxfile, Timefile, Errorfile),delimiter = ',', newline = '\n\n')
        
        Writexl = hoja.cell(row = i, column = 26) 
        Writexl.value = "File created"
        
        doc.save(path + "\\" + excel)
        
        time.sleep(1)

#------------------------------MAIN CODE-------------------------------------------

from lightkurve import search_lightcurvefile
import openpyxl
import time
import numpy as np
import os

path = r"C:\Users\HP\Desktop\Prueba_BD"
excel = "planets_2020.05.16_11.23.37.xlsx"
sheet = "planets_2020.05.16_11.23.37"

for i in range(1,9):
    folder = path + "\Planet_" + str(i)
    os.mkdir(folder)

os.mkdir(path + "\Other")
MAST = os.mkdir(path + "\MAST")

doc = openpyxl.load_workbook(path + "\\" + excel)

hoja = doc[sheet]

Satellite1 = 'Kepler'
Satellite2 = 'K2'
Satellite3 = 'Transiting Exoplanet Survey Satellite (TESS)'
Discmethod = 'Transit'

Writexl = hoja.cell(row = 29, column = 25)
Writexl.value = "Light Curve"
Writexl = hoja.cell(row = 29, column = 26)
Writexl.value = "File Status"
        

for i in range(30,150):
    Planet = hoja.cell(row = i, column = 4) 
    Telescope = hoja.cell(row = i, column = 23)
    Method = hoja.cell(row = i, column = 5)
    Quantity = hoja.cell(row = i, column = 6)
    
    try:
        
        ligthcurve(Telescope.value,Method.value,Planet.value,Quantity.value,i)

    except Exception as exc:
        print(exc)
        Writexl = hoja.cell(row = i, column = 25) 
        Writexl.value = "Not found"

    
doc.save(path + "\\" + excel)
