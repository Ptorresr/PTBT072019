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
@click.argument("tabla")
@click.argument("campos", nargs=-1)
def agrega_registro(tabla, campos):
    """
    Agrega un registro con -campos- a la -tabla-
    """

    # Nombre de tabla <- tabla
    # Lista de campos <- campos 
    # Insertar el registro en la tabla de la BD
    error = modelomysql.agrega_registro(tabla, campos)

    # Imprimir un mensaje al usuario a la salida estándar
    if error:
        print("Error: El registro no se ha agregado correctamente!")
    else:
        print("El registro se ha agregado de forma correcta!")


if __name__ == "__main__":
    agrega_registro()
