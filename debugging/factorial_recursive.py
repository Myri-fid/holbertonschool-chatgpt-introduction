#!/usr/bin/python3
import sys

def factorial(n):
    """
    Calculer la factorielle d'un nombre donné de manière récursive.

    Paramètres:
    n (int): Le nombre dont on veut calculer la factorielle.

    Retourne:
    int: La factorielle du nombre en entrée.
    """
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)

