# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 14:29:29 2020

@author: Ami
"""
def conferirImagens():
    
    #dias = abs((dataFinal - dataInicial).days)+1
    
    dataDaVez = dataInicial
    
    while (dataDaVez<=dataFinal):
        
        horasInteiras = 0
        meiasHoras = 0
        
        #print(str(dataDaVez))
        
        for j in range(4):   
            
            ic00 = 0
            im00 = 0
            ic30 = 0
            im30 = 0
            i00 = 0
            i30 = 0
           
            nomeImagemC = dataDaVez.strftime('%Y') + dataDaVez.strftime('%m') + dataDaVez.strftime('%d') + '_' + dataDaVez.strftime('%H') + dataDaVez.strftime('%M') + dataDaVez.strftime('%S') + sufixoContinua
            pathImagemC = pathContinua + '\\' + nomeImagemC
            
            nomeImagemM = dataDaVez.strftime('%Y') + dataDaVez.strftime('%m') + dataDaVez.strftime('%d') + '_' + dataDaVez.strftime('%H') + dataDaVez.strftime('%M') + dataDaVez.strftime('%S') + sufixoMag
            pathImagemM = pathMag + '\\' + nomeImagemM

            meiaHora = dataDaVez + timedelta(minutes=30)

            meiaHoraC = meiaHora.strftime('%Y') + meiaHora.strftime('%m') + meiaHora.strftime('%d') + '_' + meiaHora.strftime('%H') + meiaHora.strftime('%M') + meiaHora.strftime('%S') + sufixoContinua        
            pathMeiaHoraC = pathContinua + '\\' + meiaHoraC
            
            meiaHoraM = meiaHora.strftime('%Y') + meiaHora.strftime('%m') + meiaHora.strftime('%d') + '_' + meiaHora.strftime('%H') + meiaHora.strftime('%M') + meiaHora.strftime('%S') + sufixoMag        
            pathMeiaHoraM = pathMag + '\\' + meiaHoraM
            
            if os.path.isfile(pathImagemC) and os.path.isfile(pathImagemM):
                ic00 = 1
                im00 = 1
                i00 = 1
            elif os.path.isfile(pathImagemC):
                ic00 = 1
            elif os.path.isfile(pathImagemM):
                im00 = 1
            
            if os.path.isfile(pathMeiaHoraC) and os.path.isfile(pathMeiaHoraM):
                ic30 = 1
                im30 = 1
                i30 = 1
            elif os.path.isfile(pathMeiaHoraC):
                ic30 = 1
            elif os.path.isfile(pathMeiaHoraM):
                im30 = 1

            if (i00==0) and (i30==0):
                print(str(dataDaVez) + ' e ' + str(meiaHora) + ' faltantes!')
                
                
            #if not(os.path.isfile(pathImagemC)) or not(os.path.isfile(pathImagemM)):
            #    if os.path.isfile(pathMeiaHoraC) and os.path.isfile(pathMeiaHoraM):
            #        print(str(dataDaVez.date()) + ' com arquivos dos instantes ' + str(dataDaVez.time()) + ' e ' + str(meiaHora.time()) + ' faltantes!')        
            
            
            dataDaVez += timedelta(hours=6)
            
