#!/usr/bin/env python
# -*- coding: utf-8 -*-

es_entero = False

# MVC = Model View Controller (Modelo Vista Controlador)

# Controlador
while not es_entero:
    valor = input("Dame un entero mayor que cero:")
    if valor.isdigit() == True and int(valor)>0:
        k = int(valor)
        es_entero = True
    else:
        print("Error, el valor no es un entero o no es mayor que cero")

    print("-" * 50)

# Modelo: Crear la lista de enteros
lista_num = []
for i in range(k):
    lista_num.append(i)

# Vista: Imprimir la lista de enteros
for n in lista_num:
    print(n)

