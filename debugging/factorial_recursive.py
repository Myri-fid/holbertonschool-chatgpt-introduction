#!/usr/bin/python3
import sys

# Description de la fonction factorial
# La fonction calcule la factorielle d'un nombre entier n en utilisant la récursion.
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Vérification si un argument est passé au script
if len(sys.argv) < 2:
    print("Erreur : Veuillez fournir un argument pour calculer la factorielle.")
    sys.exit(1)  # Arrête le programme si aucun argument n'est fourni

# Récupère l'argument et le convertit en entier
try:
    f = factorial(int(sys.argv[1]))
    print(f)
except ValueError:
    print("Erreur : L'argument fourni n'est pas un entier valide.")

