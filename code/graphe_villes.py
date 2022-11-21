import tkinter as tk

transportation_cost = 1.5 #camion plein €/km
production_cost = 5000 #5€/t
truck_capacity = 0.600 # IRENA à 600kg pour 200 bar
road_cost =  transportation_cost / truck_capacity #€/(t*km)

D_DISTANCES_CITIES = {'Marseille' : {'Fos': 40, 'Nice' : 188}, 'Nice' : {'Marseille' : 188, 'Fos': 225}, 'Fos' : {'Nice' : 225, 'Marseille' : 188}}

d_prod_cities = {'Fos' : 175000 , 'Nice' : 0, 'Marseille' : 200}

d_use_cities = {'Fos' : 150000, 'Nice' : 200, 'Marseille' : 500}

def cost_prod(H2_tons):
    if H2_tons > 1000:
        return H2_tons * 3
    else : return H2_tons * 5
    
def cost_import(city, H2_need):#H2_need > 0
    #def find_best_supplier(city):
    if city != 'Fos':
        cost_unit = D_DISTANCES_CITIES[city]['Fos'] * road_cost
        cost = cost_unit * H2_need
        
    else : cost = H2_need * 3
    return cost


def compute_cities_cost(d_prod_cities):

    d_cost_cities = {}
    
    for city,prod in d_prod_cities.items():

            H2_need = d_use_cities[city] - prod
            d_cost_cities[city] = cost_prod(prod) + cost_import(city, H2_need)

            #coût négatif possible
    return d_cost_cities
def refresh():
    d_prod_cities['Nice'] = Nice_prod.get()
    d_prod_cities['Marseille'] = Marseille_prod.get()
    d_prod_cities['Fos'] = Fos_prod.get()

    d_use_cities['Nice'] = Nice_use.get()
    d_use_cities['Marseille'] = Marseille_use.get()
    d_use_cities['Fos'] = Fos_use.get()

def bilan():
    refresh()
    d_cost_cities = compute_cities_cost(d_prod_cities)
    total_cost, total_prod = 0,0
    for c in d_cost_cities.values() :
        total_cost += c
    for p in d_prod_cities.values():
        total_prod += p
    text.config(text=f'{d_cost_cities=} et {d_prod_cities=} \n {total_cost=} et {total_prod=}')
    text.pack(side = tk.LEFT)

    


   

    

########## fenetre #########

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

Nice_prod = tk.DoubleVar()
scale_1 = tk.Scale(root, from_ = 1000, to = 3000, var = Nice_prod , label = ' Nice prod (t)')
scale_1.pack(side = tk.LEFT)
Fos_prod = tk.DoubleVar()
scale_2 = tk.Scale(root, from_ = 1000, to = 150000, var = Fos_prod , label = ' Fos prod (t)')
scale_2.pack(side=tk.LEFT)    
Marseille_prod = tk.DoubleVar()
scale_3 = tk.Scale(root, from_ = 1000, to = 8000, var = Marseille_prod , label = 'Marseille prod (t)')
scale_3.pack(side=tk.LEFT)
#use
Nice_use = tk.DoubleVar()
scale_4 = tk.Scale(root, from_ = 1000, to = 3000, var = Nice_use , label = ' Nice use (t)')
scale_4.pack(anchor = 'nw')
Fos_use = tk.DoubleVar()
scale_5 = tk.Scale(root, from_ = 1000, to = 150000, var = Fos_use , label = ' Fos use (t)')
scale_5.pack(anchor = 'nw')    
Marseille_use = tk.DoubleVar()
scale_6 = tk.Scale(root, from_ = 1000, to = 8000, var = Marseille_use , label = 'Marseille use (t)')
scale_6.pack(anchor = 'nw', side = tk.LEFT)


    


text = tk.Label( master = root)
bouton2 = tk.Button(master = root, command =  lambda : bilan(), height = 3, width=15,text = "evaluer coûts")
bouton2.pack(anchor = 'center')




root.mainloop()