from tkinter import *
from tkinter import ttk
from TP_Sol import alea_val,P
import time
#from tkinter.ttk import *


class Custom_button(Button):
    def __init__(self,txt,fct):
        super().__init__(text=txt,command=fct)



class App(Tk):
    
    def __init__(self):
        super().__init__()
        self.title('TPRO')
        #self.geometry('520x180')
        #styling
        self.configure(bg="#1C1C1C")
        self.eval('tk::PlaceWindow . center')
        #center(self)
        self.configure(padx=5,pady=10)
        self.resizable(False,False)
        #Label
        title= Label(self,text="Problème du sac à dos")
        exp = Label(self,text="TPRO N°1 : Programmation dynamique")



        
        #styling labels             #D6D6D6
        title.configure( height=1,bg="#1C1C1C",font = ("Arial", 16),fg="#D6D6D6",pady=6,padx=2)
        exp.configure(bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        
        #positioning labels
        title.grid(row = 0,columnspan=4)
        exp.grid(row = 1,columnspan=4)
        
        
        #Buttons
        btn_fr = Frame(self,bg="#1C1C1C",height=15)
        btn_fr.grid(row = 2,columnspan=4)
        #btn_fr.grid_propagate(False)
        #Start button
        start_btn= Button(self,text="Démmarrer",command=self.start_action)
        quit_btn= Button(self,text="Quitter",command=self.quit_action)
    
        start_btn.configure(width=10,pady=3,padx=3,bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        quit_btn.configure(width=10,pady=3,padx=3,bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        
        # button
        start_btn.grid(row = 3,columnspan=2,column=2,padx=2)   
        quit_btn.grid(row = 3,column=0,columnspan=2,padx=2)   
    
    def quit_action(self):
        self.destroy()       
        
    def start_action(self):
        self.withdraw()
        #show new window that if closed will unshow and show this window ()
        main = Main(self)
        # self.eval(f'tk::PlaceWindow {str(main)} center')

        
#gain,poids
# Objects =[(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),
# (54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000),(54,100),(557,487),(100,1000)]

Objects =[[54,100],[557,487],[100,1000],[54,100],[557,487]]

poids_max= 0
capacite_sac = 100
gain_max = 0


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
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)
        
        
        top_frame = Frame(self,width=self.width)
        top_frame.pack(  fill='both',  padx=10,  pady=5)
        #? The top frame
        top_frame_title = Frame(top_frame,width=self.width,bg='#1C1C1C')
        top_frame_title.pack(  fill='both')

        title_lb= Label(top_frame_title,text="Liste des objets")
        title_lb.configure(font = ("Arial", 17),bg="#1C1C1C",fg="#D6D6D6",pady=6,padx=2)
        title_lb.pack(side='left',  padx=5,  pady=5)

        #!Adding buttons for list of objects manipulation 

        top_frame_btns_frame = Frame(top_frame,width=self.width,height=100,bg="#1C1C1C")
        top_frame_btns_frame.pack( fill='both')


        add_object_btn=Button(top_frame_btns_frame,text="Ajouter",command=self.add_object_action)
        edit_object_btn=Button(top_frame_btns_frame,text="Modifier",command=self.edit_object_action)
        delete_selection_btn=Button(top_frame_btns_frame,text="Supprimer Selection",command=self.delete_selection_action)
        delete_all_objects_btn=Button(top_frame_btns_frame,text="Tout supprimer",command=self.delete_all_objects_action)
        update_capacity_btn = Button(top_frame_btns_frame,text="Modifier capacité du Sac",command=self.update_capacity_action)
        randomize_list_btn = Button(top_frame_btns_frame,text="Générer objet aléatoire",command=self.randomize_list_objects)

        #Configuring  buttons style
        add_object_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        edit_object_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        delete_selection_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        delete_all_objects_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        update_capacity_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))
        randomize_list_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 11))


        add_object_btn.grid(column=0,row=0,padx=3)
        edit_object_btn.grid(column=1,row=0,padx=3)
        delete_selection_btn.grid(column=2,row=0,padx=3)
        delete_all_objects_btn.grid(column=3,row=0,padx=3)
        update_capacity_btn.grid(column=4,row=0,padx=3)
        randomize_list_btn.grid(column=5,row=0,padx=3)

        #? the left frame with list of objects
        
        left_frame= Frame(self,width=0.5*self.width,height=300,bg="#1C1C1C")
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
        background=[('selected','#788CDE')]        )

        style.map('Treeview.Heading',
            background=[('selected','#788CDE')]        )
        #Setting the table of the objects
        tree_scroll = Scrollbar(left_frame)
        tree_scroll.pack(side=RIGHT,fill=Y,pady=10)
        
        self.tree = ttk.Treeview(left_frame,yscrollcommand=tree_scroll.set,height=300)
        tree_scroll.config(command=self.tree.yview)
        
        self.tree['columns'] = ('gain','poids')

        #The columns
        self.tree.column("#0",width=100,minwidth=25,anchor=CENTER) #to remove set minwidth to 0
        self.tree.column("gain",anchor=CENTER,width=150)
        self.tree.column("poids",anchor=CENTER,width=150)

        #The heading
        self.tree.heading("#0",text='N° Objet',anchor=CENTER)
        self.tree.heading("gain",text="Gain",anchor=CENTER)
        self.tree.heading("poids",text="Poids",anchor=CENTER)


        self.tree.pack(pady=10,padx=5)


        #? The right frame with some buttons

        right_frame= Frame(self,width=400,bg='#1C1C1C')
        right_frame.pack( side='right',padx=10,  pady=5,fill='both')

        empty_frame1 = Frame(right_frame,width=400,bg='#1C1C1C')
        empty_frame1.pack(pady=10)

        #Number of objects
        nb_object_frame=Frame(right_frame,width=400,bg='#1C1C1C')
        nb_objects_label1 = Label(nb_object_frame,text="Nombre d'objet")
        self.nb_objects_label2 = Label(nb_object_frame,text="{}".format(len(Objects)))
        
        nb_objects_label1.configure(bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        
        self.nb_objects_label2.configure(width=100,pady=5,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",highlightthickness=1, highlightbackground="white")

        nb_objects_label1.configure(bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        nb_objects_label1.pack(side='left',padx=10)
        self.nb_objects_label2.pack(side='right',padx=10)
        nb_object_frame.pack(pady=8,padx=10)



        #Maximal weight
        max_weight_frame=Frame(right_frame,width=400,bg='#1C1C1C')
        max_weight_label1 = Label(max_weight_frame,text="Poids maximale ")
        self.max_weight_label2 = Label(max_weight_frame,text="{}".format(poids_max))

        max_weight_label1.configure(bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.max_weight_label2.configure(width=100,pady=5,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",highlightthickness=1, highlightbackground="white")

        max_weight_label1.pack(side='left',padx=10)
        self.max_weight_label2.pack(side='right',padx=10)
        max_weight_frame.pack(pady=8,padx=10)
        #Capacity of the bag 
        capacity_frame=Frame(right_frame,width=400,bg='#1C1C1C')
        capacity_label1 = Label(capacity_frame,text="Capacité du sac")
        self.capacity_label2 = Label(capacity_frame,text="{}".format(capacite_sac))

        capacity_label1.configure(bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=5,padx=2)
        self.capacity_label2.configure(width=100,pady=5,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",highlightthickness=1, highlightbackground="white")

        capacity_label1.pack(side='left',padx=10)
        self.capacity_label2.pack(side='right',padx=10)
        capacity_frame.pack(pady=8,padx=10)
        #Empty frame
        empty_frame2 = Frame(right_frame,width=400,bg='#1C1C1C')
        empty_frame2.pack(pady=50)

        #Main buttons

        compute_P_btn=Button(right_frame,text="Calculer P(i,j)",command=self.compute_P_action,width=100,height=2)
        compute_P_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        compute_P_btn.pack(padx=20,pady=5)
        
        test_algorithm_btn=Button(right_frame,text="Tester l'algorithme",command=self.test_algorithm_action,width=100,height=2)
        test_algorithm_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        test_algorithm_btn.pack(padx=20,pady=5)
        
        print_algorithm_btn=Button(right_frame,text="Afficher l'algorithme",command=self.print_algorithm_action,width=100,height=2)
        print_algorithm_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        print_algorithm_btn.pack(padx=20,pady=5)
        
        print_table_P_btn=Button(right_frame,text="Afficher tables des P(i,j)",command=self.print_table_P_action,width=100,height=2)
        print_table_P_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        print_table_P_btn.pack(padx=20,pady=5)


        self.update_object_table()

    def update_object_table(self):
        global Objects
        global poids_max 
        global gain_max 
        global capacite_sac
        # print(Objects)
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

        self.nb_objects_label2.config(text="{}".format(len(Objects)))
        self.max_weight_label2.config(text="{}".format(poids_max))
        self.capacity_label2.config(text="{}".format(capacite_sac))
        

    def set_max_weight(self):
        pass

    def set_max_gain(self):
        pass


    #Defining function for list of objects manipulation 
    def add_object_action(self):
        add_object_window = AddObjectWindow(self)
        self.App_window.eval(f'tk::PlaceWindow {str(add_object_window)} center')

    def edit_object_action(self):
        # print(int(self.tree.focus()))
        # print()
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

    def test_algorithm_action(self):
        pass

    def print_algorithm_action(self):
        pass

    def print_table_P_action(self):
        pass

    #Closing action    
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
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for the weight
        weight_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        weight_frame.pack( padx=20,  pady=15,fill='both')

        weight_lb = Label( weight_frame,text="Poids de l'objet")
        weight_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.weight_input = Entry(weight_frame)
        self.weight_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        weight_lb.grid(row=0,column=0)
        self.weight_input.grid(row=0,column=1)


        #Input for the gain     
        gain_frame= Frame(self,width=400,bg='#1C1C1C')
        gain_frame.pack( padx=20,  pady=7,fill='both')

        gain_lb = Label( gain_frame,text="Gain du sac")
        gain_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.gain_input = Entry(gain_frame)
        self.gain_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        gain_lb.grid(row=0,column=0)
        self.gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg='#1C1C1C',height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')




        #adding the buttons
        btn_frame= Frame(self,width=400,bg='#1C1C1C')
        btn_frame.pack( padx=10, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        add_btn=Button(btn_frame,text="Ajouter",command=self.add_action,width=10)
        add_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        add_btn.grid(row=0,column=1,padx=17,sticky=E)


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
                print(Objects)
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
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for the weight
        weight_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        weight_frame.pack( padx=20,  pady=15,fill='both')

        weight_lb = Label( weight_frame,text="Poids de l'objet")
        weight_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.weight_input = Entry(weight_frame)
        self.weight_input.insert(0,Objects[self.object_indx][1])
        self.weight_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        weight_lb.grid(row=0,column=0)
        self.weight_input.grid(row=0,column=1)


        #Input for the gain     
        gain_frame= Frame(self,width=400,bg='#1C1C1C')
        gain_frame.pack( padx=20,  pady=7,fill='both')

        gain_lb = Label( gain_frame,text="Gain du sac")
        gain_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.gain_input = Entry(gain_frame)
        self.gain_input.insert(0,Objects[self.object_indx][0])
        self.gain_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        gain_lb.grid(row=0,column=0)
        self.gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg='#1C1C1C',height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')




        #adding the buttons
        btn_frame= Frame(self,width=400,bg='#1C1C1C')
        btn_frame.pack( padx=10, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        update_btn=Button(btn_frame,text="Modifier",command=self.update_action,width=10)
        update_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        update_btn.grid(row=0,column=1,padx=17,sticky=E)


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

            if(weight >= 0 and gain >= 0):
                if(weight > poids_max):
                    poids_max = weight
                Objects[self.object_indx][0]= gain
                Objects[self.object_indx][1]= weight
                print(Objects)
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
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for the weight
        capacity_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        capacity_frame.pack( padx=20,  pady=15,fill='both')

        capacity_lb = Label(capacity_frame,text="Nouvelle capacité")
        capacity_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.capacity_input = Entry(capacity_frame)
        #TODO add current capacity
        self.capacity_input.insert(0,capacite_sac)
        self.capacity_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        capacity_lb.grid(row=0,column=0)
        self.capacity_input.grid(row=0,column=1)



        #Input valiadtion label
        self.validation_lb = Label(self,bg='#1C1C1C',height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')



        #adding the buttons
        btn_frame= Frame(self,width=400,bg='#1C1C1C')
        btn_frame.pack( padx=10, pady=10,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        update_btn=Button(btn_frame,text="Modifier",command=self.update_action,width=10)
        update_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
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
            print("New capacity : {}".format(capacite_sac))
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
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields

        #Input for the number of objects
        nb_objects_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        nb_objects_frame.pack( padx=20,  pady=15,fill='both')

        nb_objects_lb = Label( nb_objects_frame,text="Nombre d'objets ")
        nb_objects_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.nb_objects_input = Entry(nb_objects_frame)
        self.nb_objects_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        nb_objects_lb.grid(row=0,column=0)
        self.nb_objects_input.grid(row=0,column=1)


        #Input for the min weight
        min_weight_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        min_weight_frame.pack( padx=20,  pady=15,fill='both')

        min_weight_lb = Label( min_weight_frame,text="Poids minimale ")
        min_weight_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.min_weight_input = Entry(min_weight_frame)
        self.min_weight_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        min_weight_lb.grid(row=0,column=0)
        self.min_weight_input.grid(row=0,column=1)
        
        #Input for the min weight
        max_weight_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        max_weight_frame.pack( padx=20,  pady=15,fill='both')

        max_weight_lb = Label( max_weight_frame,text="Poids maximale")
        max_weight_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.max_weight_input = Entry(max_weight_frame)
        self.max_weight_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        max_weight_lb.grid(row=0,column=0)
        self.max_weight_input.grid(row=0,column=1)

        #Input for the gain  
        # Min Gain   
        min_gain_frame= Frame(self,width=400,bg='#1C1C1C')
        min_gain_frame.pack( padx=20,  pady=15,fill='both')

        min_gain_lb = Label( min_gain_frame,text="Gain minimale")
        min_gain_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.min_gain_input = Entry(min_gain_frame)
        self.min_gain_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        min_gain_lb.grid(row=0,column=0)
        self.min_gain_input.grid(row=0,column=1)
        # Max Gain   
        max_gain_frame= Frame(self,width=400,bg='#1C1C1C')
        max_gain_frame.pack( padx=20,  pady=15,fill='both')

        max_gain_lb = Label( max_gain_frame,text="Gain maximale")
        max_gain_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)

        self.max_gain_input = Entry(max_gain_frame)
        self.max_gain_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        max_gain_lb.grid(row=0,column=0)
        self.max_gain_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg='#1C1C1C',height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')




        #adding the buttons
        btn_frame= Frame(self,width=400,bg='#1C1C1C')
        btn_frame.pack( padx=10, pady=15,fill='both')


        cancel_btn=Button(btn_frame,text="Annuler",command=self.cancel_action,width=10)
        cancel_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        cancel_btn.grid(row=0,column=0,padx=17,sticky=E)

        add_btn=Button(btn_frame,text="Valider",command=self.add_action,width=10)
        add_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
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
            print(Objects)
            self.App_window.update_object_table()
            self.grab_release()
            self.destroy()
        except:
            self.validation_lb.config(text='Les poids et les Gains et le nombre d''objets  \n doivent être des entiers positifs!!',height=2,font = ("Arial", 9))

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

        self.title('Calcule de P(i,j)')
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)

        #? Adding the input fields
        #Input for i
        i_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        i_frame.pack( padx=50,  pady=15,fill='both')

        i_lb = Label( i_frame,text="Valeur de i")
        i_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.i_input = Entry(i_frame)
        self.i_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        i_lb.grid(row=0,column=0)
        self.i_input.grid(row=0,column=1)

        #Input for j
        j_frame= Frame(self,width=400,bg='#1C1C1C') ##1C1C1C
        j_frame.pack( padx=50,  pady=15,fill='both')

        j_lb = Label( j_frame,text="Valeur de j")
        j_lb.configure(width=15,bg="#1C1C1C",font = ("Arial", 12),fg="#D6D6D6",pady=2,padx=2)


        self.j_input = Entry(j_frame)
        self.j_input.configure(width=10,relief="flat",bg="#2A2A2A",font = ("Arial", 12),fg="#D6D6D6",borderwidth=1,highlightthickness=2, highlightbackground="#788CDE",highlightcolor="#9BA8DB")

        j_lb.grid(row=0,column=0)
        self.j_input.grid(row=0,column=1)

        #Input valiadtion label
        self.validation_lb = Label(self,bg='#1C1C1C',height=0,text="",fg="#D6D6D6",font = ("Arial", 1))
        self.validation_lb.pack( padx=10,fill='both')

        #Adding labels for the  output 
        #P(i,j) value
        self.P_lb = Label( self,text="")
        self.P_lb.configure(width=35,bg="#1C1C1C",font = ("Arial", 1),fg="#D6D6D6",pady=2,padx=2)
        self.P_lb.pack()

        #calculation time
        self.T_lb = Label( self,text="")
        self.T_lb.configure(width=35,bg="#1C1C1C",font = ("Arial", 1),fg="#D6D6D6",pady=2,padx=2)
        self.T_lb.pack()

        
        
        #adding the buttons
        btn_frame= Frame(self,width=400,bg='#1C1C1C')
        btn_frame.pack( padx=40, pady=15,fill='both')


        quit_btn=Button(btn_frame,text="Quitter",command=self.quit_action,width=10)
        quit_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
        quit_btn.grid(row=0,column=0,padx=25,sticky=E)

        compute_btn=Button(btn_frame,text="Calculer P(i,j)",command=self.compute_action,width=12)
        compute_btn.configure(bg='#788CDE', fg='white',activebackground='#9BA8DB',activeforeground="white",borderwidth=0,font = ("Arial", 12))
        # add_btn.pack(padx=20,pady=5)
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
            elif j>capacite_sac:
                self.validation_lb.config(text="j doit être inférieur à la capacité du sac",height=2,font = ("Arial", 9))
            else :
                start = time.time()*1000
                P_i_j = P(i,j,Objects)
                end=time.time()*1000
                self.validation_lb.config(text="",height=1,font = ("Arial", 1))
                self.P_lb.config(text='P({},{}) = {}'.format(i,j,P_i_j),height=2,font = ("Arial", 12,'bold'))
                self.T_lb.config(text='Temps de calcul de P({},{}) = {:.2f}ms'.format(i,j,end-start),height=2,font = ("Arial", 12,'bold'))
        except Exception as e:
            print(e)
            self.validation_lb.config(text='i et j doivent être des entiers',height=2,font = ("Arial", 9))

    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()


class DisplayAlgorithmWindow(TopLevel):
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

        self.title('Calcule de P(i,j)')
        # self.geometry("{}x{}".format(self.width,self.height))
        #styling
        self.configure(bg="#1C1C1C")
        #self.eval('tk::PlaceWindow . center')
        #center(self)
        #self.configure(padx=5,pady=10)
        self.resizable(False,False)
        self.protocol("WM_DELETE_WINDOW", self.close_action)
    
    def close_action(self):
        #? Releasing the old window
        self.grab_release()
        self.destroy()


app = App()
app.mainloop()





 
        
def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center
    """
    win.update_idletasks()
    width = win.winfo_width()
    frm_width = win.winfo_rootx() - win.winfo_x()
    win_width = width + 2 * frm_width
    height = win.winfo_height()
    titlebar_height = win.winfo_rooty() - win.winfo_y()
    win_height = height + titlebar_height + frm_width
    x = win.winfo_screenwidth() // 2 - win_width // 2
    y = win.winfo_screenheight() // 2 - win_height // 2
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))
    win.deiconify()