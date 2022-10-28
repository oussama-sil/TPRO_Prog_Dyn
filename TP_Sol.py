# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:06:23 2022

@author: Oussa
"""
#TODO : ajouter trouver configuration otpimale pour le cas 

from math import *
from multiprocessing.resource_sharer import stop 
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


def P(n,w,Objects):
    """
        Recherche du gain maximale 

        @param
        i : nombre d'objets
        j : capacité du sac
        Objects : matrice contenant les objets [gain,poids]
        
        @return
        int : P(i,j)

        @complexity
        T = o(i*j)    
    """
    P_tab = np.full((n+1,w+1),0,dtype=int) #tab de P(i,j) déja calculé deja calculés, initialisé à 0
    # i=0 
    # j=0
    for i in range(1,n+1):  #parcour des lignes
        for j in range(1,w+1):  #parcour des colonnes 
            if j < Objects[i-1][1]:   # j < wi
                P_tab[i,j]=P_tab[i-1,j]  #P(i,j)=P(i-1,j)
            else:  #P(i,j)=max(P(i-1,j),P(i-1,j-wi)+gi)
                P_tab[i,j]=max(P_tab[i-1,j],P_tab[i-1,j-Objects[i-1][1]]+Objects[i-1][0])
    return P_tab[n,w]

def P_objets(n,w,Objects):
    """
        Recherche du gain maximale ainsi que la liste des objets qui permettent de l'atteindre

        @param
        n : nombre d'objets
        w : capacité du sac
        Objects : matrice contenant les objets [[gain_1,poids_1],
                                                [gain_2,poids_2]
                                                ...]
        @return
        [P(i,j),temps_calcul,liste_objets_selection]
        P(i,j) : 
        temps_calcul : tmps pour calculer P(i,j)
        liste_objets_selection : La liste des objets qui donnent le gain maximale

    """
    #?Remplissage du tableau P_val 

    start=time.time()*1000
    P_tab = np.full((n+1,w+1),0,dtype=int) #tab de P(i,j) déja calculé deja calculés, initialisé à 0
    # i=0 
    # j=0
    for i in range(1,n+1):  #parcour des lignes
        for j in range(1,w+1):  #parcour des colonnes 
            if j < Objects[i-1][1]:   # j < wi
                P_tab[i,j]=P_tab[i-1,j]  #P(i,j)=P(i-1,j)
            else:  #P(i,j)=max(P(i-1,j),P(i-1,j-wi)+gi)
                P_tab[i,j]=max(P_tab[i-1,j],P_tab[i-1,j-Objects[i-1][1]]+Objects[i-1][0])
    end=time.time()*1000

    #?Recherche des objets qui réalise le gain maximale
    liste_objets_selection = []
    i = n
    j = w 
    stop = False
    while(not stop):
        if i==0 or j==0:
            stop = True
        elif j<Objects[i-1][1] and i>0:
            i -=1
        else:     
            p1 = P_tab[i-1,j] #P(i-1,j)
            p2 = P_tab[i-1,j-Objects[i-1][1]]+Objects[i-1][0] #P(i-1,j-wi)+gi   
            if(p1>=p2): #objet non selectionné
                i -= 1
            else: #object séléctionné 
                liste_objets_selection.append(i-1)
                i = i - 1
                j = j-Objects[i][1]


    return (P_tab[n,w],end-start,liste_objets_selection)

def P_rec(i,j):
    # print(i,j)
    if i==0 or j==0:
        return 0
    elif j<Objects[i-1][1] and i>0:
        return P_rec(i-1,j)
    else:        
        return max(P_rec(i-1,j), P_rec(i-1,j-Objects[i-1][1])+Objects[i-1][0])

def test_P_objects(n,w,Objects):
    P1= P(n,w,Objects)
    (P2,t,selected_objects)= P_objets(n,w,Objects)
    P3=P_rec(n,w)
    print("Output : {}".format((P1,P2,P3)))
    print("Time : {}".format(t))
    print("Objects : {}".format(selected_objects))
    tmp_w=0
    tmp_g=0
    for indx in selected_objects:
        tmp_w += Objects[indx][1]
        tmp_g += Objects[indx][0]
    print("(Cum_g,Cum_w) = ({},{})".format(tmp_g,tmp_w))



    

# Objects =[[5, 85], [8, 26], [2, 25], [3, 82], [2, 53], [5, 83], [6, 29], [4, 69], [7, 74], [8, 4], [9, 5], [2, 49], [3, 42], [6, 58], [1, 27], [9, 45], [8, 30], [8, 64], [10, 28], [5, 93], [4, 57], [3, 20], [8, 99], [9, 3], [8, 36], [8, 8], [10, 75], [6, 51], [7, 46], [1, 38], [7, 43], [1, 8], [1, 95], [3, 52], [8, 39], [9, 15], [2, 17], [5, 42], [8, 78], [3, 53], [7, 65], [10, 54], [4, 25], [10, 21], [9, 39], [2, 9], [9, 77], [6, 23], [6, 59], [7, 29], [8, 94], [5, 39], [6, 22], [7, 77], [1, 64], [1, 29], [8, 92], [4, 89], [8, 95], [10, 73], [7, 72], [7, 72], [2, 1], [2, 77], [9, 91], [8, 2], [3, 5], [8, 83], [10, 80], [3, 35], [4, 24], [1, 79], [2, 40], [2, 90], [6, 81], [6, 5], [7, 50], [1, 52], [1, 76], [9, 8], [5, 25], [9, 71], [4, 44], [5, 22], [8, 45], [5, 14], [10, 10], [6, 85], [8, 51], [4, 62], [3, 70], [10, 54], [10, 10], [7, 4], [4, 77], [1, 82], [1, 27], [4, 49], [2, 42], [9, 72]]


# test_P_objects(19,352,Objects)



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
