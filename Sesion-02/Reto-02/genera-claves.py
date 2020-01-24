#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Objetivo: Generar n claves de forma aleatoria, que deben tener al menos 1 
mayúscula, 1 minúscula y 1 dígito, con longitud m. n y m serán solicitados
al usuario, este úlutmo con un valor de 8 por defecto.

Además la clave deberá incluir cuando menos un símbolo ($#%&)
"""

import random


es_entero = False
# Leer el valor de n
while not es_entero:
    valor = input("Cuántas claves n= ")
    if valor.isdigit() == True and int(valor)>0:
        n = int(valor)
        es_entero = True
    else:
        print("Error, el valor no es un entero o no es mayor que cero")

    print("-" * 50)

# Leer el valor de m
m = 8
es_entero = False
while not es_entero:
    valor = input("Dame la longitus de la clave ({}) m= ".format(m))
    if valor.isdigit() == True and int(valor)>0:
        m = int(valor)
        es_entero = True
    elif valor == "":
        es_entero = True
    else:
        print("Error, el valor no es un entero o no es mayor que cero")

    print("-" * 50)

# Definiendo variable 
minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = minusculas.upper()
digitos = "1234567890"
r = m - 3  # Los caracteres faltantes
alf = minusculas + mayusculas + digitos
claves = []

# General n claves
for i in range(n):
    # General una clave
    clave = random.choice(minusculas)
    clave = clave + random.choice(mayusculas)
    clave = clave + random.choice(digitos)
    clave = clave + "".join(random.choices(alf, k=r))
    # clave -> list() -> clave_lista
    clave_lista = list(clave)  # str -> list
    # shuffle() <- clave_lista
    random.shuffle(clave_lista)
    # "".join(clave_lista) -> clave
    clave = "".join(clave_lista)  # list -> str
    claves.append(clave)

# Imprimir clave
for clave in claves:
    print(clave)

