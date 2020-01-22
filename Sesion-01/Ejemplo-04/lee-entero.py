#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Lee un valor entero desde la entrada estándar e imprime el valor si
corresponder a un entero, si no vuelve a solicitar una nueva entrada.
"""
es_entero = False

while not es_entero:
    valor = input("Dame un entero menor o igual a 100:")
    if valor.isdigit() == True and int(valor)<=100:
        valor = int(valor)
        print(valor, type(valor))
        es_entero = True
    else:
        print("Error, el valor no es un entero")

    print("-" * 50)
