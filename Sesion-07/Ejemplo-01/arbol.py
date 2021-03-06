#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir en la salida estándar un arbol de nivel N usando programación recursiva
"""

def imprime_arbol(n, i=1):
    """ Imprime un árbol de nuvel n """
    rama = "----"

    # condición de paro recursiva
    if i>n:
        return

    # imp rama izq
    imprime_arbol(n, i+1)
    if i == 1:
        print(rama)
    else:
        print("    "*(i-1) + rama)
    imprime_arbol(n, i+1)

def main():
    """ función principal """

    imprime_arbol(5)


if __name__ == "__main__":
    main()
