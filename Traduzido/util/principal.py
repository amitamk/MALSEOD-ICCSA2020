# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 11:57:59 2019

@author: Ami
"""
from util.functions import *

    #path = 'C:\\Users\\Ami\\Dropbox\\Tese\\Traduzido\\'
    path = 'D:\\Amita\\Doutorado\\Tese\\Traduzido\\'

    pathMag = path + 'mag'
    pathContinua = path + 'continuum'

    dataInicial = '07/03/2012 00:00:00'
    dataFinal = '09/03/2012 23:45:00'

    url = "http://jsoc.stanford.edu/data/hmi/images"
    
    sufixoContinua = '_Ic_flat_1k.jpg'
    sufixoMag = '_M_1k.jpg'
    
    resolucao = 30

    downloadImagens(url, pathContinua, dataInicial, dataFinal, resolucao, sufixoContinua)

    downloadImagens(url, pathMag, dataInicial, dataFinal, resolucao, sufixoMag)
        
    imagesMasks(pathMag, pathContinua, dataInicial, dataFinal, sufixoMag, sufixoContinua, resolucao)
    
    model_mdi_02_03(path, dataInicial, dataFinal)
    
'''
downloadImagensContinuas()

downloadMagnetogramas()

imagesMasks()
    magMasks()
        calc_mu_hmi()
    continuumMasks()

model_mdi_02_03()
    check_areas()
        le_interp()
    read_tim_tsi()
    le_interp()
    rnn()
'''    

