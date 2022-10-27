# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 21:29:46 2022

@author: Oussa
"""
from math import * 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
V = [1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5,1,1,4,1,2,3,4,5,1,4,3,2,1,5,4,2,4,1,3,5,7,1,3,6,5,1,1,2,4,2,6,5
     ]
W = [2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1
     ,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1,2,2,2,4,1,2,4,5,2,1,1,3,4,2,3,1,2,1,1,2,3,2,1,2,2,2,1,2,1,2,3,1]
n=20  #nb elem
w=20    #poids maximal
Cpt=0  #cpt d'appel
Calls = [] #les appels (val de i et j)

def P(i,j):
    global Cpt
    Cpt += 1
    if i==0 or j==0:
        return 0
    elif j<W[i-1] and i>0:
        return P(i-1,j)
    else:        
        return max(P(i-1,j), P(i-1,j-W[i-1])+V[i-1])
    
Val = np.full((n,w),-1,dtype=int) #tab de val deja calculees
def P_opt(i,j):
    global Cpt
    Cpt +=1
    if i==0 or j==0:
        return 0
    elif j<W[i-1] and i>0:
        
        if(Val[i-2,j-1]!=-1):
            Val[i-1,j-1]=Val[i-2,j-1]
            return Val[i-2,j-1]
        else:
                
            if(i-1==0 or j==0):
                tmp = 0
            else:
                tmp = P(i-1,j)
        
            Val[i-1,j-1] = tmp
            return tmp
    else:
        
        if(Val[i-2,j-1]!=-1):
            tmp1= Val[i-2,j-1]
        else:
            if(i-1==0 or j==0):
                tmp1 = 0
            else:
                tmp1 = P(i-1,j)
                
        if(Val[i-2,j-W[i-1]-1]!=-1):
            tmp2 = Val[i-2,j-W[i-1]-1]
        else:
            if(i-1==0 or j-W[i-1]==0):
                tmp2 = 0
            else:
                tmp2 = P(i-1,j-W[i-1])
            
        Val[i-1,j-1] = max(tmp1,tmp2+V[i-1])
        return  Val[i-1,j-1]
    

def plot_data(x_data,y_data,graph_legend):
    #resize the graph
    plt.figure(figsize=(5,3),dpi=100)
    
    
    plt.plot(x_data,y_data,label='2x',color='red', 
             linewidth=1)


    
    plt.xlabel('valeurs de n')
    plt.ylabel('Nb appels récursifs')
    plt.title(graph_legend,fontdict={'fontname':'Comic Sans MS','fontsize':18})
    
    #Adding a legend
    plt.legend()
    plt.show()
    plt.savefig("{}.png".format(graph_legend),dpi=300)



def test_fct(Pf,w,sup,graph_legend):
    n = 0
    tab_n=[]
    tab_cpt=[]
    global Cpt
    global Val
    for n in range(0,sup):
        Cpt=0
        Val = np.full((n,w),-1,dtype=int) #tab de val deja calculees
        P_opt(n,w)
        tab_n.append(n)
        tab_cpt.append(Cpt)
    plot_data(tab_n, tab_cpt, graph_legend)        


#test_fct(P,30,12,"Test_sans_PD")
test_fct(P_opt,30,20,"Test_avec_PD")