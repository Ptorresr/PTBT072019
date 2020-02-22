#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import modelomysql

@click.command()
@click.argument("tabla")
@click.argument("id")
def elimina_registro(tabla, id):
    """
    Elimina el registro con -id- de -tabla-
    """

    # Se hace uso de la función modelomysql.elimina_registro() que aún no
    # existe en el módulo modelmysql.py
    if modelomysql.elimina_registro(tabla, id):
        # Imprimir un mensaje al usuario a la salida estándar
        pass
    else:
        # Imprimir un mensaje de error
        pass

if __name__ == "__main__":
    elimina_registro()
