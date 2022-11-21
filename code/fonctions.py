###fonctions

def cost_prod(H2_tons):
    '''entrée en tonne
    en sortie un prix int'''
    if H2_tons > 1000:
        return H2_tons * 3
    else : return H2_tons * 5

def cost_import(D_DISTANCES_CITIES, city, H2_need, road_cost):
    '''H2_need (int) > 0
    city (string)
    D_DISTANCE_CITIES (dico des villes)
    return : cost (float)
    '''
    if city != 'Fos':
        cost_unit = D_DISTANCES_CITIES[city]['Fos'] * road_cost
        cost = cost_unit * H2_need
        
    else : cost = H2_need * 3
    return cost

def compute_cities_cost(D_DISTANCES_CITIES, d_prod_cities, d_use_cities, road_cost):
    '''entrée : dico des prod et conso et coût routier(float)
    return dico des coûts'''

    d_cost_cities = {}
    
    for city,prod in d_prod_cities.items():

            H2_need = d_use_cities[city] - prod
            d_cost_cities[city] = cost_prod(prod) + cost_import(D_DISTANCES_CITIES, city, H2_need, road_cost)

            #coût négatif possible ( ville excédentaire )
    return d_cost_cities