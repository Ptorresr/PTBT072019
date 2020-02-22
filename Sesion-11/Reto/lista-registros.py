#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import modelomysql

def imprime_tablas(tablas):
    """
    Imprime la lista de tablas de la BD en la salida estándar
    """
    print()
    print("Lista de tablas")
    print("-"*20)
    for t in tablas:
        print("-", t[0])
    
def imprime_registros(registros):
    """
    Imprime la lista de registros de la tabla en la BD en la salida estándar
    """
    longitudes = []
    for r in registros:
        lr = [len(str(c)) for c in r]  # [len("id")->2, len("titulo")->6, ...]
        longitudes.append(lr)

    maximos = [ max(col) for col in zip(*longitudes)]

    formato = ""
    for m in maximos:
        formato += "{:"+str(m)+"} "

    print()
    print("-"*20)
    for r in registros:
        print(formato.format(*r))
    print("-"*20)
    

@click.command()
@click.argument("tabla", default="")
def lista_registros(tabla):
    """
    Imprime la lista de tablas disponibles en la BD
    """
    if tabla:
        # Imprime lista de registros de -tabla-
        registros = modelomysql.obtiene_registros(tabla)
        imprime_registros(registros)
    else:
        # Imprime la lista de tablas
        tablas = modelomysql.obtiene_tablas()
        imprime_tablas(tablas)


if __name__ == "__main__":
    lista_registros()
