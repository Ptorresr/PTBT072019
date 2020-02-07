#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Descripción:

Imprimir la lista de archivos de la carpeta actual representando cada archivo
como un diccionario.

Para cada archivo incluir nombre, extensión, fecha de creación o modificación y tamaño en bytes.

Hacer uso de funciones

Imprimir la lista de archivos ordenada alfabéticamente con base al nombre

Reto:
    Imprimir la lista de archivos en orden alfabético sin importar las
    mayúsculas y minúsuclas.

Deberá poder imprimir la lista de archivos de la carpeta indicada por el
usuario en la línea de parámetros.

listaarchivos.py [carpeta]

Refactoriza el código para hacer uso del módulo Click

Agregar la opción --arch NOMBRE para guardar la lista de archivos en el archivo
NOMBRE en formato CSV.

Refactoriza el script para que haga uso del módulo CSV
---
Refactorizar para usar objetos Archivo() en lugar de diccionarios para
representar un archivo. POO (Programación Orientada a Objetos)
---
Refactorizar el script para imprimir la lista de todos los archivos de todas las carpetas
usando recursión basada en objetos.
---
RETO-02

Modificar el script la.py y modelo.py para que cuando se imprima la lista de archivos en la
salida estándar también se imprima al final de la lista el total de bytes que ocupa esa
carpeta incluyendo el tamaño de los archivos de todas las subcarpetas.
---
"""

import click
import csv
import datetime

import modelo

def guarda_archivos_csv(lista_archivos, nom_arch):
    """
    Guarda la lista de archivos en nom_arch en formato csv.
    """
    with open(nom_arch, "w") as da:
        csv_writer = csv.writer(da)
        for arch in lista_archivos:
            csv_writer.writerow(arch.list())

# Vista: Imprimir la lista de archivos
def imprime_archivos(lista_archivos):
    """ Imprime la lista de objetos archivo en la salida estándar """
    print("-"*40)
    for arch in lista_archivos:
        print("{nombre:36} {peso:10} {fecha:26}".format(**arch.dict()))
    print("-"*40)


# Controlador: lsn()
@click.command()
@click.option("--csv", "archcsv", default="", help="Guarda la lista en NOMBRE en formato CSV")
@click.argument("ruta", default=".")
def lsn(archcsv, ruta):
    """
    Imprime la lista de archivo en la salida estándar de la carpeta
    proporcionada por el usuario.

    Si el usuario no proporciona ninguna, se imprimen los archivos de la
    carpeta actual.
    """
    carpeta = modelo.Carpeta(ruta)
    lista = carpeta.obtener_archivos(ordenar="nombre")  # Regresa una lista de objetos Archivo

    if archcsv == "":
        imprime_archivos(lista)  # Imprime lista de objetos Archivo
    else:
        guarda_archivos_csv(lista, archcsv)  # Guarda lista de objetos

# Es para definri si el script es un script principal o un módulo
if __name__ == "__main__":
    lsn()


