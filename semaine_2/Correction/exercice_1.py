"""
Objective : voir en pratique le temps d'exécution d'un algorithme en utilisant la méthode time de Python

1. Implementer la méthode  sum_of_n qui calcule la somme des n premiers nombres entiers

La méthode doit retourner la somme mais aussi le temps nécessaire à son calcul


2. Augmenter la taille du paramètre d'entrée n (10x, 100x, 1000x, etc.) et relancer le programme pour
voir comment le temps d'exécution change en fonction de la taille de l'entrée

3. Est-il possible d'améliorer ?
"""
import time

def sum_of_n(n: int):
    """
    algorithme pour calculer la somme des n premiers nombres
    ex.: n = 5 --> 1 + 2 + 3 + 4 + 5 = 15
    :param n: int taille de l'entrée
    :return: somme: int, temps: float
    """
    somme: int = 0
    temps: float = 0
    ##### à coder #####

    begin: float = time.time()
    for i in range(1, n+1):
        somme += i

    temps = time.time() - begin


    ##### fin code #####
    return somme, temps


if __name__ == "__main__":

    n: int = 1000000 # taille d'entree

    for i in range(5):
        print("La somme est %d. La fonction a pris %10.7f seconds" % sum_of_n(n))
