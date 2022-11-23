import pandas as pd

db_cout_transport = pd.read_csv("couttransport.csv", sep=";")

def cout(distance : int, masse : int, moyen = "moyen"):
    """
    moyen : "bas", "moyen", "haut" -> type de scénario du plus au moins ambitieux en terme de cout
    distance : int, en km 
    masse : int, en tonnes/jour
    """
    i, j, h = 0, 0, 1
    types = "camions"

    if moyen == "moyen":
        h = 2
    elif moyen == "haut":
        h = 3

    if 1 <= distance < 10:
        j = 0
    elif 10 <= distance < 100:
        j = 1
    elif 100 <= distance < 1000:
        j = 2
    elif 1000 <= distance < 10000:
        j = 3
    else:
        j = 3
        types = "bateau"

    if 0 <= masse < 1:
        i = 1
    elif 1 <= masse < 10:
        i = 2
    elif 10 <= masse < 100:
        i = 3
    elif 100 <= masse < 1000:
        i = 4

    if i >= 3:
        types = "pipelines"


    cout_parkg = float(".".join(db_cout_transport.iloc[i, 3*j + h].split(",")))
    return cout_parkg, int(cout_parkg * masse * 1000), types


def cout_par_kg(masse, période):
    """ 
    masse : int en kg
    période : ENTREE: string in "jour", "année"  -> UTILISATION: jour
    """
    
    if période == "année":
        masse = masse / 365
    

    prixparkg_H2 = 5

    zone_dimport = {'Espagne': ["BarMar"], 'Lyon': ['Projet Backbone - réutilisation'], }
    #[nom, type d'import, ]

    cout = masse * prixparkg_H2

    return cout


def print_cout(distance, masse, moyen = "moyen"):
    parkg, total, typ = cout(distance, masse, moyen)
    print("Cout par kg transporté : ", parkg, "$", "avec des ", typ)
    print("Cout total : ", total, "$")

print_cout(distance = 188, masse = 15)