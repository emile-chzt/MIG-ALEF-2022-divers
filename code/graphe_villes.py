import tkinter as tk
from fonctions import *
from itertools import cycle

transportation_cost = 1.5 #camion plein €/km
production_cost = 5000 #5€/t
truck_capacity = 0.600 # IRENA à 600kg pour 200 bar
road_cost =  transportation_cost / truck_capacity #€/(t*km)

D_DISTANCES_CITIES = {'Marseille' : {'Fos': 40, 'Nice' : 188}, 'Nice' : {'Marseille' : 188, 'Fos': 225}, 'Fos' : {'Nice' : 225, 'Marseille' : 188}}

d_prod_cities = {'Fos' : 175000 , 'Nice' : 0, 'Marseille' : 200}

d_use_cities = {'Fos' : 150000, 'Nice' : 200, 'Marseille' : 500}


    
class ToggleButton(tk.Button):
    def __init__(self,master,**kw):
        self.states = cycle(kw.pop('states'))
        tk.Button.__init__(self,master,**kw)
        self['command'] = self.next_state
        self.next_state()
    def next_state(self):
        self.state = next(self.states)
        self['text'] = self.state

def refresh():
    prod_type = button_production_type.state
    print(prod_type)
    d_prod_cities['Nice'] = Nice_prod.get()
    d_prod_cities['Marseille'] = Marseille_prod.get()
    d_prod_cities['Fos'] = Fos_prod.get()

    d_use_cities['Nice'] = Nice_use.get()
    d_use_cities['Marseille'] = Marseille_use.get()
    d_use_cities['Fos'] = Fos_use.get()

def bilan():
    refresh()
    
    d_cost_cities = compute_cities_cost(D_DISTANCES_CITIES, d_prod_cities, d_use_cities, road_cost)
    total_cost, total_prod = 0,0
    for c in d_cost_cities.values() :
        total_cost += c
    for p in d_prod_cities.values():
        total_prod += p
    text.config(text = f'{d_cost_cities=} et {d_prod_cities=} \n {total_cost=} et {total_prod=}')
    text.grid(row = 0, column = 3)

    


   

    

########## fenetre #########

root = tk.Tk()

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
#prod
Nice_prod = tk.DoubleVar()
scale_1 = tk.Scale(root, from_ = 1000, to = 3000, var = Nice_prod , label = ' Nice prod (t)')

Fos_prod = tk.DoubleVar()
scale_2 = tk.Scale(root, from_ = 1000, to = 150000, var = Fos_prod , label = ' Fos prod (t)')
   
Marseille_prod = tk.DoubleVar()
scale_3 = tk.Scale(root, from_ = 1000, to = 8000, var = Marseille_prod , label = 'Marseille prod (t)')
scale_1.grid(row = 0, column = 0, sticky = 'w')
scale_2.grid(row = 0, column = 1, sticky = 'w') 
scale_3.grid(row = 0, column = 2, sticky= 'w')
#use
Nice_use = tk.DoubleVar()
scale_4 = tk.Scale(root, from_ = 1000, to = 3000, var = Nice_use , label = ' Nice use (t)')
Fos_use = tk.DoubleVar()
scale_5 = tk.Scale(root, from_ = 1000, to = 150000, var = Fos_use , label = ' Fos use (t)')
Marseille_use = tk.DoubleVar()
scale_6 = tk.Scale(root, from_ = 1000, to = 8000, var = Marseille_use , label = 'Marseille use (t)')
scale_4.grid(row = 1, column = 0, sticky='w')
scale_6.grid(row = 1, column = 2, sticky='w')
scale_5.grid(row = 1, column = 1, sticky='w')
#type of prod
button_production_type = ToggleButton(root,states=['full renouvelables','sur réseau'])
button_production_type.grid(row = 2, column = 1)
    


text = tk.Label( master = root)
text.grid(row = 0, column = 3)
bouton2 = tk.Button(master = root, command =  lambda : bilan(), height = 3, width=15,text = "evaluer coûts")
bouton2.grid(row = 1, column = 3)




root.mainloop()