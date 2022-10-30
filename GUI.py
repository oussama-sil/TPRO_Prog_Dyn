# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 11:07:17 2022

@author: Oussama Silem SIQ2
"""

# import code
from tkinter import *
from tkinter import ttk
from TP_Sol import alea_val,P,P_objets
import time
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import time
import threading


#Styling schema
color_schema = {
    'window_bg' : '#1C1C1C',  #ori: #1C1C1C
    'font_color':'#D6D6D6', #ori #D6D6D6
    'title_color':'#788CDE', #ori :#788CDE
    'btn_color' : "#3B52AD",   #ori : #788CDE
    'btn_color_active' : "#5466AA", #ori #5466AA
    'input_border_color':'#1C1C1C', #ori #788CDE
    'input_border_color_active':'#3B52AD',
    'input_bg_color':'#323232',  #ori:#9BA8DB #323232 #2A2A2A
    'input_relief':'sunken',
    'input_border_width':2,
    'input_insert_color' :'#788CDE' ,
    'btn_relief' : 'raised',
    'btn_borderwidth':1,
}

#Global Variables
Objects =[[54,100],[557,487],[100,1000],[54,100],[557,487]]
capacite_sac = 100
gain_max = 0
poids_max= 0



class App(Tk):
    def __init__(self):
        super().__init__()
        self.title('TPRO')
        self.configure(bg=color_schema['window_bg'])
        self.eval('tk::PlaceWindow . center')
        self.configure(padx=5,pady=10)
        self.resizable(False,False)
        
        #Labels
        title= Label(self,text="Problème du sac à dos")
        exp = Label(self,text="TPRO N°1 : Programmation dynamique")      
        title.configure( height=1,bg=color_schema['window_bg'],font = ("Arial", 16),fg=color_schema['font_color'],pady=6,padx=2)
        exp.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg=color_schema['font_color'],pady=5,padx=2)
        
        #positioning labels
        title.grid(row = 0,columnspan=4)
        exp.grid(row = 1,columnspan=4)
        
        #Buttons
        btn_fr = Frame(self,bg=color_schema['window_bg'],height=15)
        btn_fr.grid(row = 2,columnspan=4)
        start_btn= Button(self,text="Démmarrer",command=self.start_action)
        quit_btn= Button(self,text="Quitter",command=self.quit_action)
        start_btn.configure(relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,width=10,pady=3,padx=3,bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",font = ("Arial", 11))
        quit_btn.configure(relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,width=10,pady=3,padx=3,bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",font = ("Arial", 11))
        start_btn.grid(row = 3,columnspan=2,column=2,padx=2)   
        quit_btn.grid(row = 3,column=0,columnspan=2,padx=2)   
    
    def quit_action(self):
        self.destroy()       
        
    def start_action(self):
        self.withdraw()
        main = Main(self)

class Main(Toplevel):  #The main windows 
    def __init__(self,App_window):
        super().__init__()

        #? Setting attributes

        self.App_window = App_window
        self.width = 750
        self.height=600
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('TPRO')
        self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)
        
        
        top_frame = Frame(self,width=self.width)
        top_frame.pack(  fill='both',  padx=10,  pady=5)
        #? The top frame
        top_frame_title = Frame(top_frame,width=self.width,bg=color_schema['window_bg'])
        top_frame_title.pack(  fill='both')

        title_lb= Label(top_frame_title,text="Liste des objets")
        title_lb.configure(font = ("Arial", 17),bg=color_schema['window_bg'],fg=color_schema['font_color'],pady=6,padx=2)
        title_lb.pack(side='left',  padx=5,  pady=5)

        #!Adding buttons for list of objects manipulation 

        top_frame_btns_frame = Frame(top_frame,width=self.width,height=100,bg=color_schema['window_bg'])
        top_frame_btns_frame.pack( fill='both')


        add_object_btn=Button(top_frame_btns_frame,text="Ajouter",command=self.add_object_action)
        edit_object_btn=Button(top_frame_btns_frame,text="Modifier",command=self.edit_object_action)
        delete_selection_btn=Button(top_frame_btns_frame,text="Supprimer",command=self.delete_selection_action)
        delete_all_objects_btn=Button(top_frame_btns_frame,text="Tout supprimer",command=self.delete_all_objects_action)
        update_capacity_btn = Button(top_frame_btns_frame,text="Modifier capacité du Sac",command=self.update_capacity_action)
        randomize_list_btn = Button(top_frame_btns_frame,text="Générer liste d'objets aléatoire",command=self.randomize_list_objects)

        #Configuring  buttons style
        add_object_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))
        edit_object_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))
        delete_selection_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))
        delete_all_objects_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))
        update_capacity_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))
        randomize_list_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 11))

        #Adding the button to the window
        add_object_btn.grid(column=0,row=0,padx=3)
        edit_object_btn.grid(column=1,row=0,padx=3)
        delete_selection_btn.grid(column=2,row=0,padx=3)
        delete_all_objects_btn.grid(column=3,row=0,padx=3)
        update_capacity_btn.grid(column=4,row=0,padx=3)
        randomize_list_btn.grid(column=5,row=0,padx=3)

        #? the left frame with list of objects
        left_frame= Frame(self,width=0.5*self.width,height=300,bg=color_schema['window_bg'])
        left_frame.pack( side='left',padx=10,  pady=5)
        
        
        style=ttk.Style()
        style.theme_use("classic")
        style.configure("Treeview",
            background="#2A2A2A",
            foreground="white",
            rowheight=20,
            fieldbackground="#1C1C1C",
        )
        style.configure("Treeview.Heading",
            background="#2A2A2A",
            foreground="white",
            rowheight=20,
            fieldbackground="#2A2A2A",
        )

        style.map('Treeview',
        background=[('selected',color_schema['btn_color'])],foreground=[('selected','white')],
               )

        style.map('Treeview.Heading',
            background=[('selected','#788CDE')]        )
        
        #Table of objects
        tree_scroll = Scrollbar(left_frame)
        tree_scroll.pack(side=RIGHT,fill=Y,pady=10)
        
        self.tree = ttk.Treeview(left_frame,yscrollcommand=tree_scroll.set,height=300)
        tree_scroll.config(command=self.tree.yview)
        
        self.tree['columns'] = ('gain','poids')

        #The columns
        self.tree.column("#0",width=100,minwidth=100,anchor=CENTER) #to remove set minwidth to 0
        self.tree.column("gain",anchor=CENTER,width=150,minwidth=100)
        self.tree.column("poids",anchor=CENTER,width=150,minwidth=100)

        #The heading
        self.tree.heading("#0",text='N° Objet',anchor=CENTER)
        self.tree.heading("gain",text="Gain",anchor=CENTER)
        self.tree.heading("poids",text="Poids",anchor=CENTER)


        self.tree.pack(pady=10,padx=5)


        #? The right frame with some buttons

        right_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        right_frame.pack( side='right',padx=10,  pady=5,fill='both')

        empty_frame1 = Frame(right_frame,width=400,bg=color_schema['window_bg'])
        empty_frame1.pack(pady=10)

        #Number of objects
        nb_object_frame=Frame(right_frame,width=400,bg=color_schema['window_bg'])
        nb_objects_label1 = Label(nb_object_frame,text="Nombre d'objet  ")
        self.nb_objects_label2 = Label(nb_object_frame,text="{}".format(len(Objects)))
        
        nb_objects_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg=color_schema['font_color'],pady=5,padx=2)
        
        self.nb_objects_label2.configure(width=100,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,'bold'),fg=color_schema['title_color'],highlightthickness=1, highlightbackground="white")

        nb_objects_label1.pack(side='left',padx=10)
        self.nb_objects_label2.pack(side='right',padx=10)
        nb_object_frame.pack(pady=8,padx=10)



        #Maximal weight
        max_weight_frame=Frame(right_frame,width=400,bg=color_schema['window_bg'])
        max_weight_label1 = Label(max_weight_frame,text="Poids maximale ")
        self.max_weight_label2 = Label(max_weight_frame,text="{}".format(poids_max))

        max_weight_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg=color_schema['font_color'],pady=5,padx=2)
        self.max_weight_label2.configure(width=100,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,'bold'),fg=color_schema['title_color'],highlightthickness=1, highlightbackground="white")

        max_weight_label1.pack(side='left',padx=10)
        self.max_weight_label2.pack(side='right',padx=10)
        max_weight_frame.pack(pady=8,padx=10)

        #Maximal gain 
        max_gain_frame=Frame(right_frame,width=400,bg=color_schema['window_bg'])
        max_gain_label1 = Label(max_gain_frame,text="Gain maximale   ")
        self.max_gain_label2 = Label(max_gain_frame,text="{}".format(gain_max))

        max_gain_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg=color_schema['font_color'],pady=5,padx=2)
        self.max_gain_label2.configure(width=100,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,'bold'),fg=color_schema['title_color'],highlightthickness=1, highlightbackground="white")

        max_gain_label1.pack(side='left',padx=10)
        self.max_gain_label2.pack(side='right',padx=10)
        max_gain_frame.pack(pady=8,padx=10)

        #Capacity of the bag 
        capacity_frame=Frame(right_frame,width=400,bg=color_schema['window_bg'])
        capacity_label1 = Label(capacity_frame,text="Capacité du sac")
        self.capacity_label2 = Label(capacity_frame,text="{}".format(capacite_sac))

        capacity_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg=color_schema['font_color'],pady=5,padx=2)
        self.capacity_label2.configure(width=100,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,'bold'),fg=color_schema['title_color'],highlightthickness=1, highlightbackground="white")

        capacity_label1.pack(side='left',padx=10)
        self.capacity_label2.pack(side='right',padx=10)
        capacity_frame.pack(pady=8,padx=10)

        #Empty frame
        empty_frame2 = Frame(right_frame,width=400,bg=color_schema['window_bg'])
        empty_frame2.pack(pady=10)


        #Main buttons

        resolve_problem_btn=Button(right_frame,text="Résoudre le problème",command=self.resolve_problem_action,width=100,height=2)
        resolve_problem_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        resolve_problem_btn.pack(padx=20,pady=5)

        compute_P_btn=Button(right_frame,text="Calculer P(i,j)",command=self.compute_P_action,width=100,height=2)
        compute_P_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        compute_P_btn.pack(padx=20,pady=5)
        
        test_algorithm_btn=Button(right_frame,text="Tester l'algorithme",command=self.test_algorithm_action,width=100,height=2)
        test_algorithm_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        test_algorithm_btn.pack(padx=20,pady=5)
        
        print_algorithm_btn=Button(right_frame,text="Afficher l'algorithme",command=self.print_algorithm_action,width=100,height=2)
        print_algorithm_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        print_algorithm_btn.pack(padx=20,pady=5)
 

        #Putting the data on the window
        self.update_object_table()

    def update_object_table(self):
        global Objects
        global poids_max 
        global gain_max 
        global capacite_sac
        gain_max = 0
        poids_max = 0

        for record in self.tree.get_children():
            self.tree.delete(record)
        for i in range(0,len(Objects)):
            o = Objects[i]
            if(o[0]>gain_max):
                gain_max = o[0]
            if(o[1]>poids_max):
                poids_max = o[1]
            self.tree.insert(parent='',index='end',iid=i,text=i,values=(o[0],o[1]))
        self.max_gain_label2.config(text="{}".format(gain_max))
        self.nb_objects_label2.config(text="{}".format(len(Objects)))
        self.max_weight_label2.config(text="{}".format(poids_max))
        self.capacity_label2.config(text="{}".format(capacite_sac))

    def add_object_action(self):
        add_object_window = AddObjectWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(add_object_window)} center')

    def edit_object_action(self):
        if(self.tree.focus() != ""):
            update_object_window = UpdateObjectWindow(self,int(self.tree.focus()))
            self.App_window.eval(f'tk::PlaceWindow {str(update_object_window)} center')

    def delete_selection_action(self):
        global Objects
        cpt = 0
        for id in self.tree.selection():
            Objects.pop(int(id)-cpt)
            cpt+=1
        self.update_object_table()

    def delete_all_objects_action(self):
        global Objects
        for elem in self.tree.get_children():
            self.tree.delete(elem)
        Objects = []
        self.update_object_table()

    def randomize_list_objects(self):
        randomize_objects_window = RandomizeObjectsWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(randomize_objects_window)} center')

    def update_capacity_action(self):
        update_capacity_window = UpdateCapacityWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(update_capacity_window)} center')
        
    def compute_P_action(self):
        compute_P_window = ComputePWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(compute_P_window)} center')

    def resolve_problem_action(self):
        resolve_problem_window = ResolveProblemWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(resolve_problem_window)} center')

    def test_algorithm_action(self):
        test_algorithm_window = TestAlgorithmWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(test_algorithm_window)} center')

    def print_algorithm_action(self):
        print_algorithm_window = DisplayAlgorithmWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(print_algorithm_window)} center')
        pass

    def close_action(self):
        self.destroy()
        self.App_window.deiconify()

class AddObjectWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Ajouter un nouveau objet')
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        
        #Input for the weight
        weight_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        weight_frame.pack( padx=10,  pady=15,fill='both')

        weight_lb = Label( weight_frame,text="Poids de l'objet")
        weight_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.weight_input = Entry(weight_frame)
        self.weight_input.configure(insertbackground=color_schema['input_insert_color']  ,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,width=10,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        weight_lb.grid(row=0,column=0)
        self.weight_input.grid(row=0,column=1)


        #Input for the gain     
        gain_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        gain_frame.pack( padx=10,  pady=7,fill='both')

        gain_lb = Label( gain_frame,text="Gain de l'objet")
        gain_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.gain_input = Entry(gain_frame)
        self.gain_input.configure(insertbackground=color_schema['input_insert_color']  ,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,width=10,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        gain_lb.grid(row=0,column=0)
        self.gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')




        #Buttons
        btn_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        btn_frame.pack( padx=15, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        add_btn=Button(btn_frame,text="Ajouter",command=self.add_action,width=10)
        add_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        add_btn.grid(row=0,column=1,padx=15,sticky=E)

    def cancel_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

    def add_action(self):
        try:
            weight = int(self.weight_input.get())
            gain = int(self.gain_input.get())
            global Objects
            global poids_max

            if(weight >= 0 and gain >= 0):
                if(weight > poids_max):
                    poids_max = weight
                Objects.append([gain,weight])
                # print(Objects)
                self.App_window.update_object_table()
                self.grab_release()
                self.destroy()
            else :
                self.validation_lb.config(text='Le poids et le Gain doivent être \ndes entiers positifs!!',height=2,font = ("Arial", 9))

        except:
            self.validation_lb.config(text='Le poids et le Gain doivent être \ndes entiers positifs!!',height=2,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class UpdateObjectWindow(Toplevel):
    def __init__(self,Main_window,objct_indx):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes
        self.App_window = Main_window
        self.object_indx = objct_indx
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Modifier objet')
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        weight_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        weight_frame.pack( padx=10,  pady=15,fill='both')

        weight_lb = Label( weight_frame,text="Poids de l'objet")
        weight_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.weight_input = Entry(weight_frame)
        self.weight_input.insert(0,Objects[self.object_indx][1])
        self.weight_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        weight_lb.grid(row=0,column=0)
        self.weight_input.grid(row=0,column=1)


        #Input for the gain     
        gain_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        gain_frame.pack( padx=10,  pady=7,fill='both')

        gain_lb = Label( gain_frame,text="Gain de l'objet")
        gain_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.gain_input = Entry(gain_frame)
        self.gain_input.insert(0,Objects[self.object_indx][0])
        self.gain_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        gain_lb.grid(row=0,column=0)
        self.gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')




        #adding the buttons
        btn_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        btn_frame.pack( padx=10, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        update_btn=Button(btn_frame,text="Modifier",command=self.update_action,width=10)
        update_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        update_btn.grid(row=0,column=1,padx=15,sticky=E)


    def cancel_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

    def update_action(self):
        try:
            weight = int(self.weight_input.get())
            gain = int(self.gain_input.get())

            global Objects
            global poids_max
            global gain_max

            if(weight >= 0 and gain >= 0):
                Objects[self.object_indx][0]= gain
                Objects[self.object_indx][1]= weight
                self.App_window.update_object_table()
                self.grab_release()
                self.destroy()
            else :
                self.validation_lb.config(text='--Le poids et le Gain doivent être \ndes entiers positifs!!',height=2,font = ("Arial", 9))

        except:
            self.validation_lb.config(text='Le poids et le Gain doivent être \ndes entiers positifs!!',height=2,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class UpdateCapacityWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes
        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Modifier la capacité du sac')
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for the weight
        capacity_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        capacity_frame.pack( padx=10,  pady=13,fill='both')

        capacity_lb = Label(capacity_frame,text="Nouvelle capacité")
        capacity_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.capacity_input = Entry(capacity_frame)
        #TODO add current capacity
        self.capacity_input.insert(0,capacite_sac)
        self.capacity_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6" ,highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        capacity_lb.grid(row=0,column=0)
        self.capacity_input.grid(row=0,column=1)



        #Input valiadtion label
        self.validation_lb = Label(self,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')



        #adding the buttons
        btn_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        btn_frame.pack( padx=10, pady=10,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        update_btn=Button(btn_frame,text="Modifier",command=self.update_action,width=10)
        update_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        update_btn.grid(row=0,column=1,padx=17,sticky=E)


    def cancel_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

    def update_action(self):
        try:
            capacity = int(self.capacity_input.get())
            global capacite_sac
            capacite_sac = capacity
            # print("New capacity : {}".format(capacite_sac))
            self.App_window.update_object_table()
            self.grab_release()
            self.destroy()
        except:
            self.validation_lb.config(text='La capacité doit être un entier positif!!',height=1,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class RandomizeObjectsWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Génération aléatoire d''objets')
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg=color_schema['window_bg'])
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields

        #Input for the number of objects
        nb_objects_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        nb_objects_frame.pack( padx=17,  pady=10,fill='both')

        nb_objects_lb = Label( nb_objects_frame,text="Nombre d'objets ")
        nb_objects_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.nb_objects_input = Entry(nb_objects_frame)
        self.nb_objects_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        nb_objects_lb.grid(row=0,column=0)
        self.nb_objects_input.grid(row=0,column=1)


        #Input for the min weight
        min_weight_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        min_weight_frame.pack( padx=17,  pady=10,fill='both')

        min_weight_lb = Label( min_weight_frame,text="Poids minimale ")
        min_weight_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.min_weight_input = Entry(min_weight_frame)
        self.min_weight_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        min_weight_lb.grid(row=0,column=0)
        self.min_weight_input.grid(row=0,column=1)
        
        #Input for the min weight
        max_weight_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        max_weight_frame.pack( padx=17,  pady=10,fill='both')

        max_weight_lb = Label( max_weight_frame,text="Poids maximale")
        max_weight_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.max_weight_input = Entry(max_weight_frame)
        self.max_weight_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        max_weight_lb.grid(row=0,column=0)
        self.max_weight_input.grid(row=0,column=1)

        #Input for the gain  
        # Min Gain   
        min_gain_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        min_gain_frame.pack( padx=17,  pady=10,fill='both')

        min_gain_lb = Label( min_gain_frame,text="Gain minimale")
        min_gain_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.min_gain_input = Entry(min_gain_frame)
        self.min_gain_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        min_gain_lb.grid(row=0,column=0)
        self.min_gain_input.grid(row=0,column=1)
        # Max Gain   
        max_gain_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        max_gain_frame.pack( padx=17,  pady=10,fill='both')

        max_gain_lb = Label( max_gain_frame,text="Gain maximale")
        max_gain_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.max_gain_input = Entry(max_gain_frame)
        self.max_gain_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        max_gain_lb.grid(row=0,column=0)
        self.max_gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=8,fill='both')




        #adding the buttons
        btn_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        btn_frame.pack( padx=17, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        add_btn=Button(btn_frame,text="Valider",command=self.add_action,width=10)
        add_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        add_btn.grid(row=0,column=1,padx=17,sticky=E)


    def cancel_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

    def add_action(self):
        try:
            
            global Objects
            global poids_max
            
            min_weight = int(self.min_weight_input.get())
            max_weight = int(self.max_weight_input.get())
            min_gain = int(self.min_gain_input.get())
            max_gain = int(self.max_gain_input.get())
            nb_objects = int(self.nb_objects_input.get())
            Objects = alea_val(nb_objects,min_gain,max_gain,min_weight,max_weight)
            self.App_window.update_object_table()
            self.grab_release()
            self.destroy()
        except:
            self.validation_lb.config(text="Les poids et les Gains et le nombre d'objets  \n doivent être des entiers positifs!!",height=2,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class ComputePWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Calcul de P(i,j)')
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for i
        i_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        i_frame.pack( padx=50,  pady=10,fill='both')

        i_lb = Label( i_frame,text="Valeur de i")
        i_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.i_input = Entry(i_frame)
        self.i_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        i_lb.grid(row=0,column=0)
        self.i_input.grid(row=0,column=1)

        #Input for j
        j_frame= Frame(self,width=400,bg=color_schema['window_bg']) ##1C1C1C
        j_frame.pack( padx=50,  pady=10,fill='both')

        j_lb = Label( j_frame,text="Valeur de j")
        j_lb.configure(width=15,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.j_input = Entry(j_frame)
        self.j_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])

        j_lb.grid(row=0,column=0)
        self.j_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both',pady=0)

        #Adding labels for the  output 
        #P(i,j) value
        self.P_lb = Label( self,text="")
        self.P_lb.configure(width=35,bg=color_schema['window_bg'],font = ("Arial", 1),fg="#D6D6D6",pady=0,padx=0)
        self.P_lb.pack()

        #calculation time
        self.T_lb = Label( self,text="")
        self.T_lb.configure(width=35,bg=color_schema['window_bg'],font = ("Arial", 1),fg="#D6D6D6",pady=0,padx=0)
        self.T_lb.pack()

        
        
        #adding the buttons
        btn_frame= Frame(self,width=400,bg=color_schema['window_bg'])
        btn_frame.pack( padx=30, pady=13,fill='both')


        quit_btn=Button(btn_frame,text="Quitter",command=self.quit_action,width=10)
        quit_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        quit_btn.grid(row=0,column=0,padx=25,sticky=E)

        compute_btn=Button(btn_frame,text="Calculer P(i,j)",command=self.compute_action,width=12)
        compute_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        compute_btn.grid(row=0,column=1,padx=25,sticky=E)


    def quit_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

    def compute_action(self):
        try:
            i = int(self.i_input.get())
            j = int(self.j_input.get())
            global Objects
            global capacite_sac
            if i>len(Objects):
                self.validation_lb.config(text="i doit être inférieur au nombre d'objets crées",height=2,font = ("Arial", 9))
            # elif j>capacite_sac:
            #     self.validation_lb.config(text="j doit être inférieur à la capacité du sac",height=2,font = ("Arial", 9))
            else :
                start = time.time()*1000
                P_i_j = P(i,j,Objects)
                end=time.time()*1000
                self.validation_lb.config(text="",height=1,font = ("Arial", 1))
                self.P_lb.config(text='P({},{}) = {}'.format(i,j,P_i_j),height=1,font = ("Arial", 12,'bold'))
                self.T_lb.config(text='Temps de calcul de P({},{}) = {:.2f}ms'.format(i,j,end-start),height=1,font = ("Arial", 12,'bold'))
        except Exception as e:
            self.validation_lb.config(text='i et j doivent être des entiers',height=2,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class ResolveProblemWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title('Résolution du problème')
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #Big Title lb
        title_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        title= Label(title_frame,text="Solution Optimale")
        title.configure(pady=10,bg=color_schema['window_bg'],font = ("Arial", 20,'bold'),fg=color_schema['title_color'])
        title.pack(padx=20,pady=5,side=LEFT)
        title_frame.pack(pady=5,padx=10)

        #Gain maximal lb
        max_gain_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        max_gain_label1 = Label(max_gain_frame,text="Gain maximale obtenu            ")
        self.max_gain_label2 = Label(max_gain_frame,text="{}".format(14568229))

        max_gain_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.max_gain_label2.configure(width=15,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg="#788CDE",highlightthickness=1, highlightbackground="white")

        max_gain_label1.pack(side='left',padx=5)
        self.max_gain_label2.pack(side='right',padx=5)
        max_gain_frame.pack(pady=6,padx=10)
    
        #cumulative weight lb
        cum_weight_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        cum_weight_label1 = Label(cum_weight_frame,text="Poids cumulé des objets         ")
        self.cum_weight_label2 = Label(cum_weight_frame,text="{}".format(145689))

        cum_weight_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.cum_weight_label2.configure(width=15,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg="#788CDE",highlightthickness=1, highlightbackground="white")

        cum_weight_label1.pack(side='left',padx=5)
        self.cum_weight_label2.pack(side='right',padx=5)
        cum_weight_frame.pack(pady=6,padx=10)

        #nb  objects lb
        nb_objects_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        nb_objects_label1 = Label(nb_objects_frame,text="Nombre d'objets sélectionnés")
        self.nb_objects_label2 = Label(nb_objects_frame,text="{}".format(1489))

        nb_objects_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.nb_objects_label2.configure(width=15,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg="#788CDE",highlightthickness=1, highlightbackground="white")

        nb_objects_label1.pack(side='left',padx=5)
        self.nb_objects_label2.pack(side='right',padx=5)
        nb_objects_frame.pack(pady=6,padx=10)

        #calculation time lb
        calc_time_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        calc_time_label1 = Label(calc_time_frame,text="Temps de calcule (ms)            ")
        self.calc_time_label2 = Label(calc_time_frame,text="{:.2f}".format(1489188.15568))

        calc_time_label1.configure(bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.calc_time_label2.configure(width=15,pady=5,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg="#788CDE",highlightthickness=1, highlightbackground="white")

        calc_time_label1.pack(side='left',padx=5)
        self.calc_time_label2.pack(side='right',padx=5)
        calc_time_frame.pack(pady=6,padx=10)

        #List of selected objects 
        selected_objects_frame=Frame(self,width=400,bg=color_schema['window_bg'])
        selected_objects= Label(selected_objects_frame,text="Liste des objets sélectionnés")
        selected_objects.configure(pady=10,bg=color_schema['window_bg'],font = ("Arial", 14,'bold'),fg=color_schema['title_color'])
        selected_objects.pack(padx=20,pady=3,side=LEFT)
        selected_objects_frame.pack(pady=3,padx=8)


        #Adding the reeview of selected objects 
        list_selected_objects_frame= Frame(self,bg=color_schema['window_bg'])
        
        
        style=ttk.Style()
        style.theme_use("classic")
        style.configure("Treeview",
            background="#2A2A2A",
            foreground="white",
            rowheight=20,
            fieldbackground="#1C1C1C",
        )
        style.configure("Treeview.Heading",
            background="#2A2A2A",
            foreground="white",
            rowheight=20,
        fieldbackground="#2A2A2A",
        )

        style.map('Treeview',
        background=[('selected',color_schema['btn_color'])],foreground=[('selected','white')],        )

        style.map('Treeview.Heading',
            background=[('selected','#788CDE')]        )
        #Table of selected objects
        tree_scroll = Scrollbar(list_selected_objects_frame)
        tree_scroll.pack(side=RIGHT,fill=Y,pady=10)
        
        self.tree = ttk.Treeview(list_selected_objects_frame,yscrollcommand=tree_scroll.set)
        tree_scroll.config(command=self.tree.yview)
        
        self.tree['columns'] = ('gain','poids')

        #The columns
        self.tree.column("#0",width=100,minwidth=0,anchor=CENTER) #to remove set minwidth to 0
        self.tree.column("gain",anchor=CENTER,width=100)
        self.tree.column("poids",anchor=CENTER,width=100)

        #The heading
        self.tree.heading("#0",text='N° Objet',anchor=CENTER)
        self.tree.heading("gain",text="Gain",anchor=CENTER)
        self.tree.heading("poids",text="Poids",anchor=CENTER)

        self.tree.pack(pady=1,padx=5)
        list_selected_objects_frame.pack(padx=10,  pady=1)

        #Void Frame
        void_frame=Frame(self,width=400,bg=color_schema['window_bg'],height=20)
        void_frame.pack(pady=6,padx=10)

        self.update_fields()

    def update_fields(self):
        global Objects
        global capacite_sac
        (P,t,selected_objects)= P_objets(len(Objects),capacite_sac,Objects)
        self.max_gain_label2.config(text="{}".format(P))

        self.nb_objects_label2.config(text="{}".format(len(selected_objects)))
        self.calc_time_label2.config(text="{:.2f}".format(t))
        #Updating the list of selected objects
        tmp_weight = 0
        for indx in selected_objects:
            tmp_weight += Objects[indx][1]
            self.tree.insert(parent='',index='end',iid=indx,text=indx,values=(Objects[indx][0],Objects[indx][1]))
        self.cum_weight_label2.config(text="{}".format(tmp_weight)) #TODO
    
    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class DisplayAlgorithmWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title("Affichage de l'algorithme")
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        

        var_frame=Frame(self,bg=color_schema['window_bg'])

        var= Label(var_frame,text="Variables globales")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 14,"bold"),fg=color_schema['title_color'])
        var.pack(padx=0,pady=3,anchor="w")


        var= Label(var_frame,text="Objects : tableau[1..n,0..1] d'entier ")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6")
        var.pack(padx=0,pady=2,anchor="w")

        var= Label(var_frame,text="\\\\ Chaque ligne de Objects représente un objet",pady=0,bg=color_schema['window_bg'],font = ("Arial", 11),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="\\\\ La première colonne contient les gains et la deuxième les poids",pady=0,bg=color_schema['window_bg'],font = ("Arial", 11),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="\\\\ Ex : Objects[i-1,0] représente le gain du ième objet et Objects[i-1,1] son poids",pady=0,bg=color_schema['window_bg'],font = ("Arial", 11),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")


        var= Label(var_frame,text="P(n,w)")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 14,"bold"),fg=color_schema['title_color'])
        var.pack(padx=0,pady=3,anchor="w")

        var= Label(var_frame,text="Var ")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg=color_schema['title_color'])
        var.pack(padx=0,pady=2,anchor="w")

        var= Label(var_frame,text="  P_Val : tableau[0..i,0..j] d'entier")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6")
        var.pack(padx=0,pady=0,anchor="w")

        var= Label(var_frame,text="Debut ")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg=color_schema['title_color'])
        var.pack(padx=0,pady=2,anchor="w")
        
        var= Label(var_frame,text="  Pour i = 0, n",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      Pour j = 0, w",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \tSi (i=0 ou j=0)",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\tP_Val[i,j] = 0",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \tSinon",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\tSi (j <Objects[i-1,1] et i>0)",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\t\tP_Val[i,j] = P_Val[i-1,j]",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\tSinon ",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\t\tP_Val[i,j] = max ( P_Val[i-1,j] , P_Val[i-1,j-Objects[i-1,1]]+Objects[i-1,0])",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="      \t\tFSI ",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="     \tFSI",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="    FPour",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="  FPour",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")
        var= Label(var_frame,text="  P = P_Val[n,w]",pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6").pack(padx=0,pady=0,anchor="w")


        var= Label(var_frame,text="Fin ")
        var.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg=color_schema['title_color'])
        var.pack(padx=0,pady=2,anchor="w")

        var_frame.pack(pady=5,padx=20)

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()

class TestAlgorithmWindow(Toplevel):
    def __init__(self,Main_window):
        super().__init__(Main_window)
        #? Disabling the old window
        self.grab_set()

        #? Setting attributes

        self.App_window = Main_window
        self.width = 200
        self.height=200
        
        #? Global Variables 
        global Objects
        global poids_max
        global capacite_sac

        self.title("Test de l'algorithme")
        self.configure(bg=color_schema['window_bg'])
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)


        #Side left
        self.left_frame=Frame(self,bg=color_schema['window_bg'])


        title= Label(self.left_frame,text="Complexité de l'algorithme :")
        title.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 14,"bold"),fg=color_schema['title_color'])
        title.pack(padx=0,pady=3,anchor="w")

        text= Label(self.left_frame,text=""" 
La complexité de l'algorithme = o(n.w) ou n est  
le nombre d'objets et w est la capacité du sac. 
En posant n=w, la complexité devient égale a o(n^2),
elle peut être observé en testant l'algorithme
""")
        text.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6")
        text.pack(padx=0,pady=1,anchor="w")

        title= Label(self.left_frame,text="Test de l'algorithme")
        title.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 14,"bold"),fg=color_schema['title_color'])
        title.pack(padx=0,pady=1,anchor="w")

        text= Label(self.left_frame,text=""" 
Cette fonctionnalité permet de voire l'évolution 
du temps d'execution de l'algorithme en fonction du 
nombre d'objets n. elle calcul P(i,i) pour des valeurs 
de i entre 0 et n et affiche le graphe T_exec = f(n)
        """)
        text.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6")
        text.pack(padx=0,pady=1,anchor="w")

        title= Label(self.left_frame,text="Remarque : ")
        title.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12,"bold"),fg=color_schema['title_color'])
        title.pack(padx=0,pady=1,anchor="w")

        text= Label(self.left_frame,text=
"""
Les valeurs de n choisies ne doit pas être trop grande 
(<2000),sinon le programme risque de prendre trop
de temps pour afficher le graphe """)
        text.configure(pady=0,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6")
        text.pack(padx=0,pady=1,anchor="w")

        input_frame= Frame(self.left_frame,bg=color_schema['window_bg'],pady=20) ##1C1C1C

        input_lb = Label( input_frame,text="Valeur de n")
        input_lb.configure(width=12,bg=color_schema['window_bg'],font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=0)


        self.n_input = Entry(input_frame)
        self.n_input.configure(insertbackground=color_schema['input_insert_color']  ,width=10,relief=color_schema["input_relief"],borderwidth=color_schema["input_border_width"] ,bg=color_schema['input_bg_color'],font = ("Arial", 12),fg="#D6D6D6",highlightthickness=2, highlightbackground=color_schema['input_border_color'],highlightcolor=color_schema['input_border_color_active'])


        input_lb.grid(row=0,column=0)
        self.n_input.grid(row=0,column=1)
        

        self.display_btn=Button(input_frame,text="Afficher Graphe",command=self.handle_btn_click,width=15)
        self.display_btn.configure(bg=color_schema['btn_color'], fg='white',activebackground=color_schema['btn_color_active'],activeforeground="white",relief=color_schema["btn_relief"],borderwidth=color_schema["btn_borderwidth"]  ,font = ("Arial", 12))
        self.display_btn.grid(row=0,column=2,padx=10,sticky=E)
        self.display_btn.configure(state=NORMAL)

        input_frame.pack()
        input_frame.pack(padx=0,pady=1,anchor="w")
        
        self.validation_lb = Label(self.left_frame,bg=color_schema['window_bg'],height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=0)
        

        s = ttk.Style()
        s.configure("red.Horizontal.TProgressbar", foreground=color_schema["btn_color"], background=color_schema["btn_color"],troughcolor=color_schema["window_bg"])
        self.progress_bar = ttk.Progressbar(self.left_frame,style="red.Horizontal.TProgressbar",orient=HORIZONTAL,length=300,mode='indeterminate')
        self.progress_bar.pack(pady=5)


        self.left_frame.pack(padx=10,pady=20,side=LEFT)        
        #Side Right 
        self.right_frame=Frame(self,bg=color_schema['window_bg'],height=0,width=0)
        self.right_frame.pack(padx=0,pady=0,side=RIGHT)

    def handle_btn_click(self,event=None):
        try:
            n = int(self.n_input.get())
            self.validation_lb.config(text="",font = ("Arial",1),pady=0)

            #Creating a second thread for computing
            self.second_thread = threading.Thread(target=self.display_action)
            self.second_thread.daemon = True
            self.second_thread.start()
            
            #Disabling the button
            self.display_btn.configure(state=DISABLED)


            self.progress_bar.start()
            self.after(20, self.stop_progress_bar)
        except:
            self.validation_lb.config(text="le nombre d'objets n doit être un entier!!",font = ("Arial", 10),pady=0)

    def stop_progress_bar(self):
        if self.second_thread.is_alive():
            self.after(20, self.stop_progress_bar)
        else:
            self.progress_bar.stop() 
            self.display_btn.configure(state=NORMAL)

    def display_action(self):

        try:
            n = int(self.n_input.get())
            Objects=alea_val(n,0,100,0,int(n/100))

            if n>=4000:
                step = max(1,int(n /10))
            elif n>=1000 and n<4000:
                step = max(1,int(n /25))
            else:
                step = max(1,int(n /50))
            nb = 0
            tab_n=[]
            tab_cpt=[]
            tmp = 0
            nb = 0
            while nb < n:
                start = time.time()*1000
                P(nb,nb,Objects)
                end=time.time()*1000
                tab_n.append(nb)
                tab_cpt.append(end-start)
                nb += step


            #Plotting
            self.right_frame.destroy()
            self.right_frame=Frame(self,bg=color_schema['window_bg'],height=0,width=0)
            fig = Figure(figsize = (5, 5),dpi = 100)
            plot1 = fig.add_subplot(111)
            plot1.plot(tab_n,tab_cpt,linewidth=1)
            plot1.set_xlabel('valeurs de n') 
            plot1.set_ylabel('Temps execution (ms)')
            plot1.set_title("Temps d'execution en fonction de n")          
            canvas = FigureCanvasTkAgg(fig,master = self.right_frame)  
            canvas.draw()
            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()
            self.right_frame.pack(padx=40,pady=20,side=RIGHT)
        except:
            self.validation_lb.config(text="le nombre d'objets n doit être un entier!!",font = ("Arial", 10),pady=0)
    
    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()




#Starting the app
app = App()
app.mainloop()





 
