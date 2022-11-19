import tkinter as tk

transportation_cost = 1.5 #camion plein €/km
production_cost = 5000 #5€/t
truck_capacity = 0.600 # IRENA à 600kg pour 200 bar
road_cost =  transportation_cost / truck_capacity #€/(t*km)

D_DISTANCES_CITIES = {'Marseille' : {'Fos': 40, 'Nice' : 188}, 'Nice' : {'Marseille' : 188, 'Fos': 225}, 'Fos' : {'Nice' : 225, 'Marseille' : 188}}

d_prod_cities = {'Fos' : 175000 , 'Nice' : 0, 'Marseille' : 200}

d_conso_cities = {'Fos' : 150000, 'Nice' : 200, 'Marseille' : 500}

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
    d_prod_cities['Nice'] = Nice_prod.get()
    d_prod_cities['Marseille'] = Marseille_prod.get()
    d_prod_cities['Fos'] = Fos_prod.get()

    for city,prod in d_prod_cities.items():

            H2_need = d_conso_cities[city] - prod
            d_cost_cities[city] = cost_prod(prod) + cost_import(city, H2_need)

            #coût négatif possible
    return d_cost_cities

def bilan():
    d_cost_cities = compute_cities_cost(d_prod_cities)
    total_cost, total_prod = 0,0
    for c in d_cost_cities.values() :
        total_cost += c
    for p in d_prod_cities.values():
        total_prod += p
    text.config(text=f'{d_cost_cities=} et {d_prod_cities=} \n {total_cost=} et {total_prod=}')
    text.pack(anchor='se')

    


   

    

########## fenetre #########

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

Nice_prod = tk.DoubleVar()
scale = tk.Scale(root, from_ = 1000, to = 3000, var = Nice_prod , label = ' Nice prod (t)')
scale.pack(side = tk.LEFT)
Fos_prod = tk.DoubleVar()
scale = tk.Scale(root, from_ = 1000, to = 150000, var = Fos_prod , label = ' Fos prod (t)')
scale.pack(side=tk.LEFT)    
Marseille_prod = tk.DoubleVar()
scale = tk.Scale(root, from_ = 1000, to = 8000, var = Marseille_prod , label = 'Marseille prod (t)')
scale.pack(side=tk.LEFT)



    


text = tk.Label( master = root)
bouton2 = tk.Button(master = root, command =  lambda : bilan(), height = 3, width=15,text = "evaluer coûts")
bouton2.pack(side=tk.BOTTOM)




root.mainloop()