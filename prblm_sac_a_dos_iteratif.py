from math import * 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time

#Quoi faire : générer de manière aléatoire les données 
#interface tkinter 
#Algo pour remplissage du tableau 
#affichage du tableau
#Affichage d'un temps d'execution de l'algorithme pour des valeurs différents 
#Affichage de l'algorithme dans l'interface 


V = [1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ]
W = [2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1
     ,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1]

n=20  #nb elem
w=20    #poids maximal
Cpt=0  #cpt d'appel

def P(i,j):
    Val = np.full((i+1,j+1),0,dtype=int) #tab de val deja calculees
    k=0
    m=0
    for k in range(1,i+1):
        for m in range(1,j+1):
            if m < W[k-1]:
                Val[k,m]=Val[k-1,m]
            else:
                Val[k,m]=max(Val[k-1,m],Val[k-1,m-W[k-1]]+V[k-1])
    return Val[i,j]
    
def remplir_tableau(i,j):
    P = np.full((i,j),0,dtype=int)
    k=0
    m=0
    for k in range(1,i+1):
        for m in range(1,j+1):
            if m < W[k-1]:
                P[k,m]=Val[k-1,m]
            else:
                P[k,m]=max(P[k-1,m],P[k-1,m-W[k-1]]+V[k-1])
    return P


    
    
def P_val(i,j):
    Val = np.full((i+1,j+1),0,dtype=int) #tab de val deja calculees
    k=0
    m=0
    for k in range(1,i+1):
        for m in range(1,j+1):
            if m < W[k-1]:
                Val[k,m]=Val[k-1,m]
            else:
                Val[k,m]=max(Val[k-1,m],Val[k-1,m-W[k-1]]+V[k-1])
    return Val[i,j]


    nb = 0
    tab_n=[]
    tab_cpt=[]
    global Cpt
    global Val
    for nb in range(0,sup):
        Cpt=0
        Val = np.full((nb,wb),-1,dtype=int) #tab de val deja calculees
        val = P(nb,wb)
        tab_n.append(nb)
        tab_cpt.append(Cpt)
        print("P({},{}) = {} avec {} appel recursive".format(nb,wb,val,Cpt))

    plt.figure(figsize=(5,3),dpi=100)
    plt.plot(tab_n,tab_cpt,color='red',linewidth=1)
    plt.xlabel('valeurs de n')
    plt.ylabel('Nb appels récursifs')
    plt.title("Test_avec_PD_nb_appels",fontdict={'fontname':'Comic Sans MS','fontsize':18})
    
    #Adding a legend
    plt.legend()
    plt.show()
    plt.savefig("Test_avec_PD_nb_appels.png",dpi=300)  

def test_fct_time(tab_w,sup_n):
    for wb in tab_w:
        nb = 0
        tab_n=[]
        tab_cpt=[]
        global Val
        tmp = 0
        for nb in range(0,sup_n):
            start = time.time()*1000
            val = P(nb,wb)
            end=time.time()*1000
            tab_n.append(nb)
            tab_cpt.append(end-start)
            print("P({},{}) = {} avec {} appel recursive".format(nb,wb,val,Cpt))
    
        #plt.figure(figsize=(5,3),dpi=100)
        plt.plot(tab_n,tab_cpt,linewidth=1,label="w={}".format(wb))

    
    #Adding a legend
    plt.xlabel('valeurs de n')
    plt.ylabel('Temps execution (ms)')
    plt.title("PD_Rec_temps_exec",fontdict={'fontname':'Comic Sans MS','fontsize':18})
    plt.legend()
    plt.show()
    plt.savefig("PD_Rec_temps_exec.png",dpi=300)

#test_fct_time([30,10,50],120)

print(remplir_tableau(i=10, j=15))