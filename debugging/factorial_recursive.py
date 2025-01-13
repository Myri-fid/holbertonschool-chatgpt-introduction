#!/usr/bin/python3
import sys

def factorial(n):
    """
    Fonction pour calculer le factoriel d'un nombre entier.

    Description : 
        Cette fonction utilise une approche récursive pour calculer le 
        factoriel d'un nombre entier positif n. Le factoriel de n (noté n!) 
        est le produit de tous les entiers de 1 à n.

    Paramètres :
        n (int) : Le nombre entier pour lequel nous voulons calculer le 
                  factoriel.

    Retour :
        int : Le factoriel de n. Si n est égal à 0, la fonction retourne 1 
              (par convention, 0! = 1).
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Vérification de l'argument passé via la ligne de commande
f = factorial(int(sys.argv[1]))

# Affichage du résultat du calcul du factoriel
print(f)

