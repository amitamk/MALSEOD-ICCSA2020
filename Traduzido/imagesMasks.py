# -*- coding: utf-8 -*-
"""
Created on Wed Jul 3 2019

@Author: Amita Muralikrishna
"""

import numpy as np
import cv2
from datetime import *
from util.functions import *

dataInicial = '01/01/2019 00:00:00'
dataFinal = '03/01/2019 23:45:00'

sufixoContinua = '_Ic_flat_1k.jpg'
sufixoMag = '_M_1k.jpg'

resolucao = 15

dataInicial = datetime.strptime(dataInicial,'%d/%m/%Y %H:%M:%S')
dataFinal = datetime.strptime(dataFinal,'%d/%m/%Y %H:%M:%S')

#qtdDias = abs((dataFinal - dataInicial).days)+1
#print('Quantidade de dias: ', qtdDias)

dataDaVez = dataInicial

path = 'C:\\Users\\Ami\\Dropbox\\Tese\\Traduzido\\'
pathMag = path + 'mag'
pathContinua = path + 'continuum'

k=0

aux_area_c = np.empty(6)
aux_area_c.fill(np.nan)

area_c = []
#area_c = np.append(area_c,aux_area_c)

aux_alpha_mu_spot = np.empty([6,11])
aux_alpha_mu_spot.fill(np.nan)

alpha_mu_spot = []
#alpha_mu_spot = np.append(alpha_mu_spot,aux_alpha_mu_spot)

area_disk_c = []
time = []

while dataDaVez<=dataFinal:
    
    ano = dataDaVez.strftime('%Y')
    mes = dataDaVez.strftime('%m')
    dia = dataDaVez.strftime('%d')
    horas = dataDaVez.strftime('%H')
    minutos = dataDaVez.strftime('%M')
    segundos = dataDaVez.strftime('%S')
    
    nomeImagem = ano + mes + dia + '_' + horas + minutos + segundos
    
    nomeImagemContinua = nomeImagem + sufixoContinua
    nomeImagemMag = nomeImagem + sufixoMag
    
    pathImagemContinua = pathContinua + '\\' + nomeImagemContinua
    pathImagemMag = pathMag + '\\' + nomeImagemMag
    
    '''VERIFICAR SE HÁ A NECESSIDADE DE ACRESCENTAR A PARTE DECINAL RELATIVA AOS MINUTOS AQUI'''
    t_obs_preliminary = date.toordinal(dataDaVez)+366 
    
    bw_mask = np.zeros((1024,1024))

    try:
        bw_mask, area_disk = magMasks(pathImagemMag,bw_mask)
    except:
        print('Magnetograms masking error...')
        
    try:
        bw_mask = continuumMasks(pathImagemContinua,bw_mask)
    except:
        print('Continuum images masking error...')
        
       
    #np.savetxt(path + nomeImagem + '_area.txt', bw_mask)
    area_disk_c = np.append(area_disk_c,area_disk)
    
    
    if ((horas=='00') | (horas == '06') | (horas == '12') | (horas == '18')) & ((minutos == '00') | (minutos == '30')):
        
        if k == 0:
            ret,thresh = cv2.threshold(bw_mask,0,1,cv2.THRESH_BINARY)
            thresh = np.uint8(thresh)
            mu, mu_rings = calc_mu_hmi(thresh)
 #           area_c = area_c.reshape(1,6)
 #           alpha_mu_spot = alpha_mu_spot.reshape(1,6,11)
            
        for i in range(2,8):
            if i==5:
                bw1 = (bw_mask == 5) | (bw_mask == 6) | (bw_mask == 7)
                itemp = np.count_nonzero(bw1)
            elif i == 6:
                bw1 = bw_mask == 6
                itemp = np.count_nonzero(bw1)
            elif i == 7:
                bw1 = bw_mask == 7
                itemp = np.count_nonzero(bw1)
            else:
                bw1 = bw_mask == i
                itemp = np.count_nonzero(bw1)
            
            ndisk = np.count_nonzero(mu_rings)
            
            if np.count_nonzero(itemp> 0):
                aux_area_c[i-2] = itemp/area_disk_c[k]
            else:
                aux_area_c[i-2] = 0
            
            for m in range(1,12):
                temp = bw1*(mu_rings==m)
                alpha_mu_preliminary = np.nansum(temp) / ndisk
                aux_alpha_mu_spot[i-2][m-1] = alpha_mu_preliminary
        
        area_c = np.append(area_c, [aux_area_c])
        
        alpha_mu_spot = np.append(alpha_mu_spot, [aux_alpha_mu_spot])
                
        time = np.append(time,t_obs_preliminary)
        
        aux_area_c = np.empty(6)
        aux_area_c.fill(np.nan)
        
        aux_alpha_mu_spot = np.empty([6,11])
        aux_alpha_mu_spot.fill(np.nan)
        
        k = k+1
    
        area_c = area_c.reshape(k,6)
        alpha_mu_spot = alpha_mu_spot.reshape(k,6,11)
        
    dataDaVez = dataDaVez + timedelta(minutes=resolucao)

np.savetxt('time.csv', time)

np.savetxt('area_c.csv', area_c)

with open('alpha_mu_spot.csv', 'w') as outfile:
    # I'm writing a header here just for the sake of readability
    # Any line starting with "#" will be ignored by numpy.loadtxt
    outfile.write('# Array shape: {0}\n'.format(alpha_mu_spot.shape))

    # Iterating through a ndimensional array produces slices along
    # the last axis. This is equivalent to data[i,:,:] in this case
    for dataSlice in alpha_mu_spot:

        # The formatting string indicates that I'm writing out
        # the values in left-justified columns 7 characters in width
        # with 2 decimal places.  
        np.savetxt(outfile, dataSlice, fmt='%-7.2f')

        # Writing out a break to indicate different slices...
        outfile.write('# New slice\n')
    
    
