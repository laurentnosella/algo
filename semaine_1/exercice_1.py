"""
1. Coder un algorithme pour calculer la moyenne d'un tableau en utilisant une boucle while

2. Modifier l'algorithme pour qu'il n'incrémente pas i
2.1 Est-ce qu'il finit ? Non, boucle infinie

3. Modifier l'algorithme initial pour qu'il divise la valeur par n dans la boucle au contraire de faire à la fin
3.1 Est-il correct ? Non, moy restera 0
"""

def moy_tableau_1(A: list):
    """
    calcule la moyenne d'un tableau en utilisant une boucle while
    :param A: tableau de réel
    :return: moy:float la moyenne
    """
    moy: float          # resultat
    n: int = len(A)     # taille du tableau
    somme: float = 0    # somme des valeurs du tableau
    i: int = 0
    ##### à coder #####

    while i < n:
        somme += A[i]
        i += 1

    ##### fin code #####
    moy = somme / n
    return moy

def moy_tableau_2(A: list):
    """
    calcule la moyenne d'un tableau en utilisant une boucle while
    :param A: tableau de réel
    :return: moy:float la moyenne
    """
    moy: float  # resultat
    n: int = len(A)  # taille du tableau
    somme: float = 0  # somme des valeurs du tableau
    i: int = 0
    ##### à coder #####


    while i < n:
        somme += A[i]


    ##### fin code #####
    moy = somme / n
    return moy



def moy_tableau_3(A: list):
    """
    calcule la moyenne d'un tableau en utilisant une boucle while
    :param A: tableau de réel
    :return: moy:float la moyenne
    """
    moy: float  # resultat
    n: int = len(A)  # taille du tableau
    i: int = 0
    ##### à coder #####

    while i<n:
        moy += A[i] / n
        i += 1



    ##### fin code ####
    return moy


if __name__ == "__main__":
    A: list = [3.5, 4.5, 2.0, 6.0]

    moy = moy_tableau_1(A)      # question 1.
    #moy = moy_tableau_2(A)     # question 2.
    #moy = moy_tableau_3(A)     # quesiton 3.

    print("moyenne =", moy)
