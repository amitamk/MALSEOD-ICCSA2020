# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:42:06 2020

@author: Ami
"""

from library import *
from allFunctions import *
from settings import *

downloadImagens(sufixoContinua, pathContinua)
downloadImagens(sufixoMag, pathMag)

tsi_Alltime, Alltsi, sig = read_tim_tsi()


dt = 1/4

tHours = dataInicial.hour/24
tMinutes = dataInicial.minute/(24*60)
tSeconds = dataInicial.second/(24*60*60)
#dI = dataInicial.toordinal()+366+tHours+tMinutes+tSeconds
dI = dataInicial.toordinal()+tHours+tMinutes+tSeconds

tHours = dataFinal.hour/24
tMinutes = dataFinal.minute/(24*60)
tSeconds = dataFinal.second/(24*60*60)
#dF = dataFinal.toordinal()+366+tHours+tMinutes+tSeconds
dF = dataFinal.toordinal()+tHours+tMinutes+tSeconds

#dI = date.toordinal(dataInicial)+366
#dF = date.toordinal(dataFinal)+366+1/4
period = np.arange(dI,dF,dt)

t = []
tsi = []
tsi_time = []


for j in range(len(period)):
    t1 = period[j]
    
    jj = np.where((tsi_Alltime >= (t1 - dt/2)) & (tsi_Alltime < (t1 + dt/2)))
    
    if (np.squeeze(jj)).size > 0:
        tsi.append(Alltsi[jj])
        tsi_time.append(tsi_Alltime[jj])
    else:
        tsi.append(np.nan)
        tsi_time.append(np.nan)
    
    t.append(t1)
    
t = np.array(t)
tsi = np.array(tsi)
tsi_time = np.array(tsi_time)

tsi = tsi[1:]

np.savetxt(path+'\\tsi.csv', tsi)
print(path+'tsi.csv')