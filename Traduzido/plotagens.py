
import matplotlib.pyplot as plt
from scipy import stats
import numpy.ma as ma
import numpy as np

# PLOT COMPARATIVO ENTRE AS MATRIZES AREA_C E ALPHA_MU_SPOT 

def plotComparativo():
    
    time = np.loadtxt(path+'time.csv')
    area_c = np.loadtxt(path+'area_c.csv')
    alpha_mu_spot = np.loadtxt(path+'alpha_mu_spot.csv')
    #time = np.loadtxt(file1)
    #area_c = np.loadtxt(file2)
    #alpha_mu_spot = np.loadtxt(file3)

    alpha_mu_spot = np.reshape(alpha_mu_spot,(np.size(time),6,11))

    for i in range(11):
        
        fig, axs = plt.subplots(3, 2)
        
        plt.title('alpha_mu_spot: áreas do +'+str(i)+'º anel')
        
        #Plotando as 6 classes do anel i
        arquivo = path+'alpha_mu_spot_ML'+str(i+1)+'.csv'
        alpha_mu_spot2 = np.loadtxt(arquivo)
        print(arquivo)
        
        y=0
        
        for j in range(6):
            X = alpha_mu_spot[:,j,i]
            Y = alpha_mu_spot2[:,j]

            r = ma.corrcoef(ma.masked_invalid(X), ma.masked_invalid(Y))[0][1]

            rLegend = 'r = '+str(r)
            print(rLegend)
            #r = 'r = '+str(stats.pearsonr(alpha_mu_spot[:,j,i],alpha_mu_spot2[:,j])[0]) #retorna coeficiente de correlação e a probabilidade da correlação ser ao acaso.
            
            x = np.mod(j,2)
            
            axs[y*1,x].plot(X,Y, 'b*')
            axs[y*1,x].scatter(X,Y)
            axs[y*1,x].legend([rLegend], loc=0)
            #axs[y*1,x].set_title('Variável alpha_mu_spot[:,'+str(j)+','+str(i)+']')
            axs[y*1,x].set_xlim([0,0.01])
            axs[y*1,x].set_ylim([0,0.01])
            #plt.legend(loc='best')
            
            y += x
        
            #print('r = ',stats.pearsonr(alpha_mu_spot[:,0,i],alpha_mu_spot2[:,0]))    

        for ax in axs.flat:
            ax.set(xlabel='Python', ylabel='Matlab')
    
        ## Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()
    
        plt.show
        file = (path+'Anel'+str(i+1)+'.png')
        plt.savefig(file, transparent = True)


def plotComparativoCheckAreas():
    time = np.loadtxt(path+'check_areas_time.csv')
    area_c = np.loadtxt(path+'check_areas_area_c.csv')
    alpha_mu_spot = np.loadtxt(path+'check_areas_alpha_mu_spot.csv')
    #time = np.loadtxt(file1)
    #area_c = np.loadtxt(file2)
    #alpha_mu_spot = np.loadtxt(file3)

    alpha_mu_spot = np.reshape(alpha_mu_spot,(np.size(time),6,11))

    for i in range(11):
        
        fig, axs = plt.subplots(3, 2)
        
        plt.title('alpha_mu_spot: áreas do +'+str(i)+'º anel')
        
        #Plotando as 6 classes do anel i
        arquivo = path+'check_areas_alpha_mu_spot_ML'+str(i+1)+'.csv'
        alpha_mu_spot2 = np.loadtxt(arquivo)
        print(arquivo)
        
        y=0
        
        for j in range(6):
            X = alpha_mu_spot[:,j,i]
            Y = alpha_mu_spot2[:,j]

            r = ma.corrcoef(ma.masked_invalid(X), ma.masked_invalid(Y))[0][1]

            rLegend = 'r = '+str(r)
            print(rLegend)
            #r = 'r = '+str(stats.pearsonr(alpha_mu_spot[:,j,i],alpha_mu_spot2[:,j])[0]) #retorna coeficiente de correlação e a probabilidade da correlação ser ao acaso.
            
            x = np.mod(j,2)
            
            axs[y*1,x].plot(X,Y, 'b*')
            axs[y*1,x].scatter(X,Y)
            axs[y*1,x].legend([rLegend], loc=0)
            #axs[y*1,x].set_title('Variável alpha_mu_spot[:,'+str(j)+','+str(i)+']')
            axs[y*1,x].set_xlim([0,0.01])
            axs[y*1,x].set_ylim([0,0.01])
            #plt.legend(loc='best')
            
            y += x
        
            #print('r = ',stats.pearsonr(alpha_mu_spot[:,0,i],alpha_mu_spot2[:,0]))    

        for ax in axs.flat:
            ax.set(xlabel='Python', ylabel='Matlab')
    
        ## Hide x labels and tick labels for top plots and y ticks for right plots.
        for ax in axs.flat:
            ax.label_outer()
    
        plt.show
        file = (path+'Anel_check_area_'+str(i+1)+'.png')
        plt.savefig(file, transparent = True)



def plotComparativoPT():
    
    P_py = np.loadtxt(path+'P_PY.csv')
    T_py = np.loadtxt(path+'T_PY.csv')
    P_ml = np.loadtxt(path+'P_ML.csv')
    T_ml = np.loadtxt(path+'T_ML.csv')

#    pn_py = np.loadtxt(path+'pn_py.csv')
#    tn_py = np.loadtxt(path+'tn_py.csv')
#    pn_ml = np.loadtxt(path+'pn_ML.csv')
#    tn_ml = np.loadtxt(path+'tn_ML.csv')
    
    series_size = T_ml.size
    
#    for i in range(series_size):
#        fig, axs = plt.plot(range(pn_py.shape[0]),pn_py[:,i],'b.',range(pn_py.shape[0]),pn_ml[:,i],'r*')
#        plt.show
#    
#    fig, axs = plt.plot(tn_py,tn_ml)
#    plt.show

    for i in range(series_size):
        plt.figure(i)
        plt.plot(range(P.shape[0]),P_py[:,i],'b*-',range(P.shape[0]),P_ml[:,i],'r*-')
        plt.show
    
    plt.plot(range(series_size),T_py,'g*',range(series_size),T_ml,'b-')
    plt.show

def plotComparativoPnTn():
    
    P_py = np.loadtxt(path+'pn_PY.csv')
    T_py = np.loadtxt(path+'tn_PY.csv')
    P_ml = np.loadtxt(path+'pn_ML.csv')
    T_ml = np.loadtxt(path+'tn_ML.csv')

#    P_py = np.loadtxt(path+'P_PY.csv')
#    T_py = np.loadtxt(path+'T_PY.csv')
#    P_ml = np.loadtxt(path+'P_ML.csv')
#    T_ml = np.loadtxt(path+'T_ML.csv')
    
    series_size = T_ml.size
    
#    for i in range(series_size):
#        fig, axs = plt.plot(range(pn_py.shape[0]),pn_py[:,i],'b.',range(pn_py.shape[0]),pn_ml[:,i],'r*')
#        plt.show
#    
#    fig, axs = plt.plot(tn_py,tn_ml)
#    plt.show

    for i in range(series_size-45):
        plt.figure(i)
        plt.plot(range(P_py.shape[0]),P_py[:,i],'b*-',range(P_py.shape[0]),P_ml[:,i],'r*-')
        plt.show
    
    plt.figure(i+1)
    plt.plot(range(series_size),T_py,'g*',range(series_size),T_ml,'b-')
    plt.show