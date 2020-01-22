#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprime la tabla de multiplicar del número N, el valor de N se solicita
al usuario y se tiene que validar que el valor proporcionado por el usuario
sea un número entero y mayor que cero.

Tiempo estimado: 10 mins
"""
es_entero = False
k = 0

# MVC = Model View Controller (Modelo Vista Controlador)

# Controlador / Modelo
while not es_entero:
    valor = input("Dame un entero mayor que cero:")
    if valor.isdigit() == True and int(valor)>0:
        k = int(valor)
        es_entero = True
    else:
        print("Error, el valor no es un entero o no es mayor que cero")

    print("-" * 50)

# Vista: Se encarga de la salida
print("Tabla del {}".format(k))
print("-" * 15)
for i in range(1, 11):
    print("{:2} x {} = {:2}".format(i, k, i*k))
print("-" * 15)

