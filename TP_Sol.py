# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:06:23 2022

@author: Oussama Silem SIQ2
"""

from math import *
from multiprocessing.resource_sharer import stop 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import random as rd



def alea_val(nb_objet,min_gain,max_gain,min_poids,max_poids):
    """
    Génération d'une liste d'objets d'une manière aléatoire
    
    Parameters
    ----------
    nb_objet : int
        Nombre d'objets.
    min_gain : int
        Gain minimale.
    max_gain : int
        Gain maximale.
    min_poids : int
        Poids minimale.    
    max_poids : int
        Poids maximale.

    Returns
    -------
    Objects : Tableau d'objets 

    """
    Objects = []
    for i in range(nb_objet):
        Objects.append([rd.randint(min_gain, max_gain),rd.randint(min_poids,max_poids)])
    return Objects

def P(n,w,Objects):
    """
    Calcul de P(n,w)

    Parameters
    ----------
    n : int
        Nombre d'objets.
    w : int
        Capacité du sac.
    Objects : list
        Liste des objets.

    Returns
    -------
    P(n,w) : Gain maximale obtenu

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
    
    Parameters
    ----------
    n : int
        Nombre d'objets.
    w : int
        Capacité du sac.
    Objects : list
        Liste des objets.

    Returns
    -------
    [P(i,j),temp_calcul,liste_objets_selction]

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

def P_rec(i,j,Objects):
    """
    Calcul de P(i,j) d'une manière récursive

    Parameters
    ----------
    n : int
        Nombre d'objets.
    w : int
        Capacité du sac.
    Objects : list
        Liste des objets.

    Returns
    -------
    P(i,j)

    """
    if i==0 or j==0:
        return 0
    elif j<Objects[i-1][1] and i>0:
        return P_rec(i-1,j,Objects)
    else:        
        return max(P_rec(i-1,j,Objects), P_rec(i-1,j-Objects[i-1][1],Objects)+Objects[i-1][0])

def test_P_objects(n,w,Objects):
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
    P1= P(n,w,Objects)
    (P2,t,selected_objects)= P_objets(n,w,Objects)
    P3=P_rec(n,w,Objects)
    print("Output : {}".format((P1,P2,P3)))
    print("Time : {}".format(t))
    print("Objects : {}".format(selected_objects))
    tmp_w=0
    tmp_g=0
    for indx in selected_objects:
        tmp_w += Objects[indx][1]
        tmp_g += Objects[indx][0]
    print("(Cum_g,Cum_w) = ({},{})".format(tmp_g,tmp_w))

def test_fct_time(sup_n,Objects):
    """
    Générer un graph de l'evolution du temps d'execution en fonction du nombre d'objets 

    Parameters
    ----------
    sup_n : int
        Nombre d'objets maximale.
    Objects : list
        Liste des objets.

    Returns
    -------
    None.

    """
    step = int(sup_n /100)
    nb=0
    
    nb = 0
    tab_n=[]
    tab_cpt=[]
    tmp = 0
    nb = 0
    while nb < sup_n:
        start = time.time()*1000
        P(nb,nb,Objects)
        end=time.time()*1000
        tab_n.append(nb)
        tab_cpt.append(end-start)
        nb += step
    plt.plot(tab_n,tab_cpt,linewidth=1,label="w={}".format(step))
    plt.xlabel('valeurs de n')
    plt.ylabel('Temps execution (ms)')
    plt.title("Evolution temps d'execution en fonction du nombre d'objets",fontdict={'fontname':'Comic Sans MS','fontsize':18})
    plt.legend()
    plt.show()
    plt.savefig("PD_Rec_temps_exec.png")



# Objects = alea_val(10000,1,100,1,10)
# test_P_objects(20,100,Objects)

# test_fct_time(100,Objects)