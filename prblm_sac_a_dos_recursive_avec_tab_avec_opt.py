# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 17:52:54 2022

@author: Oussa
"""
from math import * 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
from datetime import datetime

V = [1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ]
W = [2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1
     ,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1]

n=50  #nb elem
w=30    #poids maximal
Val = np.full((n+1,w+1),-1,dtype=int) #tab de val deja calculees
Cpt=0  #cpt d'appel

def P(i,j):
    global Cpt
    Cpt +=1
    if i==0 or j==0:
        Val[i,j] = 0
        return Val[i,j]
    elif j<W[i-1] and i>0:
        if(Val[i-1,j]!=-1):
            tmp = Val[i-1,j]
        else:
            tmp = P(i-1,j)
        Val[i,j] = tmp
        return tmp
    else:
        if(Val[i-1,j]!=-1):
            tmp1= Val[i-1,j]
        else:
            tmp1 = P(i-1,j)
                
        if(Val[i-1,j-W[i-1]]!=-1):
            tmp2 = Val[i-1,j-W[i-1]]
        else:
            tmp2 = P(i-1,j-W[i-1])
            
        Val[i,j] = max(tmp1,tmp2+V[i-1])
        return  Val[i,j]



def plot_data(x_data,y_data,graph_legend):
    #resize the graph
    plt.figure(figsize=(5,3),dpi=100)
    
    
    plt.plot(x_data,y_data,color='red',linewidth=1)


    
    plt.xlabel('valeurs de n')
    plt.ylabel('Nb appels récursifs')
    plt.title(graph_legend,fontdict={'fontname':'Comic Sans MS','fontsize':18})
    
    #Adding a legend
    plt.legend()
    plt.show()
    plt.savefig("{}.png".format(graph_legend),dpi=300)

def test_fct_cpt(tab_w,sup_n):
    global Cpt
    for wb in tab_w:
        nb = 0
        tab_n=[]
        tab_cpt=[]
        global Val
        tmp = 0
        for nb in range(0,sup_n):
            Cpt=0
            Val = np.full((nb+1,wb+1),-1,dtype=int) #tab de val deja calculees
            val = P(nb,wb)
            tab_n.append(nb)
            tab_cpt.append(Cpt)
            print("P({},{}) = {} avec {} appel recursive".format(nb,wb,val,Cpt))
    
        #plt.figure(figsize=(5,3),dpi=100)
        plt.plot(tab_n,tab_cpt,linewidth=1,label="w={}".format(wb))

    
    #Adding a legend
    plt.xlabel('valeurs de n')
    plt.ylabel('Nb appels récursifs')
    plt.title("PD_Rec_nb_appels",fontdict={'fontname':'Comic Sans MS','fontsize':18})
    
    #Adding a legend
    plt.legend()
    plt.show()
    plt.savefig("PD_Rec_nb_appels.png",dpi=300) 

def test_fct_time(tab_w,sup_n):
    for wb in tab_w:
        nb = 0
        tab_n=[]
        tab_cpt=[]
        global Val
        tmp = 0
        for nb in range(0,sup_n):
            Val = np.full((nb+1,wb+1),-1,dtype=int) #tab de val deja calculees
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

test_fct_cpt([30,10,50],128)
test_fct_time([30,10,50],20)



