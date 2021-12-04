import numpy as np
import random
from random import seed
from random import randint


# la fonction Diviser Pour Mieux Régner
def DPMR(element, liste_triee):
    # condition d'arrêt de la fonction recursive
    if len(liste_triee)==1 :
        return 0
    
    # le milieu du tableau courant
    middle = len(liste_triee)//2

    # la fonction recursive fait une recherche dichotomique 
    if liste_triee[middle] >= element:
        return DPMR(element, liste_triee[:middle])
    else :
        return middle + DPMR(element, liste_triee[middle:])


if __name__ == '__main__':
    # initialiser le generateur des valeurs pour random
    # sert aussi pour avoir les m^émes valeurs à chaque execution
    seed(1)
    longueur_tableau = int(input('la longueur du tableau :'))
    valeur_min = int(input('la valeur min du tableau :'))
    valeur_max = int(input('la valeur max du tableau :'))

    tab = []

    # generer un tableau de longueur "longueur tableau" avec
    # des valeurs entre valeur_min et valeur_max
    for _ in range(longueur_tableau):
        tab.append(randint(valeur_min, valeur_max))

    # trier le tableau 
    tab.sort()

    # genérer un nombre aléatoire
    nombre_a_insere = random.randint(valeur_min,valeur_max)

    print('Le Tableau :',tab)
    print('Le nombre à inseré est: ',nombre_a_insere)

    # la fonction DPMR retourne l'index oû il fallai mettre nombre_a_inserer
    index = DPMR(nombre_a_insere, tab)

    # creer un nouveau tableu avec la nouvelle valeur ajouté
    new_tab = tab[:]
    new_tab.insert(index+1,nombre_a_insere)

    print('le tableu après l\'insertion :',new_tab)