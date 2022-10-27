# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:06:23 2022

@author: Oussa
"""
#TODO : ajouter trouver configuration otpimale pour le cas 

from math import * 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import random as rd

#Quoi faire : générer de manière aléatoire les données 
#interface tkinter 
#Algo pour remplissage du tableau et inistialisation des données avec des valeurs qui sont aléatoires 
#affichage du tableau
#Affichage d'un temps d'execution de l'algorithme pour des valeurs différents 
#Affichage de l'algorithme dans l'interface 
#Entrer es valeurs ou bien les générer de manière aléatoire
#doit afficher le temps en second
# V = [1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
#      ,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
#      ]
# W = [2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1
#      ,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1]

# n= len(V)  #nb elem
# w=50    #poids maximal

def P(i,j,Objects):
    Val = np.full((i+1,j+1),0,dtype=int) #tab de val deja calculees
    k=0
    m=0
    for k in range(1,i+1):
        for m in range(1,j+1):
            if m < Objects[k-1][1]:
                Val[k,m]=Val[k-1,m]
            else:
                Val[k,m]=max(Val[k-1,m],Val[k-1,m-Objects[k-1][1]]+Objects[k-1][0])
    return Val[i,j]

# def P(i,j,Gains,Poids):
#     Val = np.full((i+1,j+1),0,dtype=int) #tab de val deja calculees
#     k=0
#     m=0
#     for k in range(1,i+1):
#         for m in range(1,j+1):
#             if m < Poids[k-1]:
#                 Val[k,m]=Val[k-1,m]
#             else:
#                 Val[k,m]=max(Val[k-1,m],Val[k-1,m-Poids[k-1]]+Gains[k-1])
#     return Val[i,j]

def remplir_tableau(n,w,Gains,Poids):
    """
    Parameters
    ----------
    n : nombre objet
    w : Poids maximale
    V : Les Gains .
    W : Les Poids .

    Returns
    -------
    (tab_val,temps_exec)
    tab_val : tablea de P(i,j) pour i allant de 0 à n et j allant de 0 à w
    tamps_exec : temps nécessaire pour remplir le tablea 
    """
    start = time.time()
    Val = np.full((n+1,w+1),0,dtype=int) #tab de val deja calculees
    k=0
    m=0
    for k in range(1,n+1):
        for m in range(1,w+1):
            if m < Poids[k-1]:
                Val[k,m]=Val[k-1,m]
            else:
                Val[k,m]=max(Val[k-1,m],Val[k-1,m-Poids[k-1]]+Gains[k-1])
    end = time.time()
    return (Val,end-start)  


def alea_val(nb_objet,min_gain,max_gain,min_poids,max_poids):
    """
    Parameters
    ----------
    nb_objet : TYPE
        DESCRIPTION.
    max_gain : TYPE
        DESCRIPTION.
    max_poids : TYPE
        DESCRIPTION.

    Returns
    -------
    [tab_gain,tab_poids,]
    None.

    """
    Objects = []
    for i in range(nb_objet):
        Objects.append([rd.randint(min_gain, max_gain),rd.randint(min_poids,max_poids)])
    return Objects


# nb_objet = 1000
# max_gain = 100
# max_poids  = 1000

# n = 50
# w = 10000

# (Gains,Poids)=alea_val(nb_objet,max_gain,max_poids)
# (res,temps_exec) = remplir_tableau(n, w, Gains,Poids)

# print(P(10,10,V,W))
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