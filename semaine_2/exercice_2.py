"""
Objective : voir en pratique le temps d'exécution pour quelques complexités algorithmiques

1. Pour chaque fonction non implémentée dans le fichier exercice_2.py, l'implémenter de manière à respecter
en fonction de la taille d'entrée n la complexité respective

    1.1 comp_constant
    1.2 comp_lineaire
    1.3 comp_quadratique
    1.4 comp_cubique

L'algorithme n'a pas à résoudre un problème


2. Augmenter la taille du paramètre d'entrée n (5x, 25x, 50x, etc.) dans le main et relancer le programme
    2.1 Qu'est-ce qui se passe ?
    
3. Bonus : quel est la complexité de la fonction comp_x ?

"""

import timeit

import matplotlib.pyplot as plt


def comp_constant(n: int):
    """
    algorithme de complexité constant
    :param n: int taille de l'entrée
    :return: None
    """
    ##### à coder #####





    ##### fin code #####
    return


def comp_lineaire(n: int):
    """
    algorithme de complexité lineaire
    :param n: int taille de l'entrée
    :return: None
    """
    ##### à coder #####






    ##### fin code #####
    return


def comp_quadratique(n: int):
    """
    algorithme de complexité quadratique
    :param n: int taille de l'entrée
    :return: None
    """
    ##### à coder #####





    ##### fin code #####
    return


def comp_cubique(n: int):
    """
    algorithme de complexité cubique
    :param n: int taille de l'entrée
    :return: None
    """
    ##### à coder #####





    ##### fin code #####
    return


def comp_x(n: int):
    """
    algorithme de complexité x
    :param n: int taille de l'entrée
    :return: None
    """
    i: int = n
    while i > 1:
        i = i // 2

    return


def plot_time(x: list, y: list, func_name: list):
    """
    print execution time in function of entry size for each function
    :param x: list with test entry sizes
    :param y: list with execution times for each function
    :param func_name: list of tested functions
    :return: None
    """
    max_y = max([max(_y) for _y in y])
    fig, ax = plt.subplots(1)
    fig.set_size_inches(12.42, 7.68)

    for i in range(len(y)):
        ax.plot(x, y[i], linewidth=2, label=func_name[i])

    ax.set_ylim(0, max_y * 1.1)
    ax.set_xlabel('size (n)', fontsize=18)
    ax.set_ylabel('time (sec)', fontsize=18)
    ax.legend(fancybox=True, framealpha=0.5, fontsize=18)
    ax.set_title('Function execution time', fontsize=20)

    plt.grid(True, linestyle='--', linewidth=1)
    plt.show()


def run_tests(n_max: int, test_func: list):
    """
    function to run complexity tests
    :param n: entry size
    :param test_func: list of functions to test
    :return: None
    """

    X: list = [i for i in range(1, n_max + 1, 1)]  # n for the tests
    Y: list = []  # result time for each function

    for fname in test_func:
        y = []  # temp store for each function
        for n in X:
            # measure the function time
            r = timeit.timeit(fname + '(' + str(n) + ')', number=1, globals=globals())
            y.append(r)
        Y.append(y)
    plot_time(X, Y, test_func)


if __name__ == "__main__":
    n: int = 10  # taille d'entree

    #    algorithmes à measurer
    test_func: list = ['comp_constant', 'comp_lineaire', 'comp_quadratique', 'comp_cubique', 'comp_x']
    #    test_func = ['comp_constant', 'comp_lineaire', 'comp_quadratique']
    #    test_func = ['comp_constant', 'comp_lineaire', 'comp_x']

    run_tests(n, test_func)
