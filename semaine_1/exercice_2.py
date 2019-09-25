"""
1. Coder en Python l'algorithme <<tri par insertion>> pour trier un tableau A de taille n

2. Exécutez-le étape par étape et regardez les valeurs des variables i, j et cle et du tableau A[1 .. j-1]

3. Imprimez le nombre de fois que l'instruction i = i - 1 est exécutée pour les tableaux :
3.1     A = [2,1]
3.2     A = [3,2,1]
3.3     A = [4,3,2,1]
3.4     A = [5,4,3,2,1]
3.5     A = [6,5,4,3,2,1]
"""


def tri_insertion(A: list):
    """
    trie le tableau A
    :param A: tableau de int
    :return: A:liste le tableau trié
    """
    count = 0                                 # question 3

    ##### à coder #####

    for j in range(1, len(A)):
        i = j-1
        cle = A[j]
        while i >= 0 and A[i]>cle:
            A[i+1] = A[i]
            i = i-1
            count += 1

        A[i+1]=cle




    ##### fin code #####

    print("taille A :", len(A))                # question 3
    print("nombre d'execution :", count)         # question 3
    ######
    return A


if __name__ == "__main__":
    A: list = [2, 5, 4, 7, 9, 0, -1]    # question 1 et 2
    #A: list = [2, 1]                   # question 3.1
    #A: list = [3, 2, 1]                # question 3.2
    #A: list = [4, 3, 2, 1]             # question 3.3
    #A: list = [5, 4, 3, 2, 1]          # question 3.4
    #A: list = [6, 5, 4, 3, 2, 1]       # question 3.5

    A = tri_insertion(A)

    print()
    print("A trié =", A)
