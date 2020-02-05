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
"""

import click
import csv
import datetime
import os
import sys

# Definición de la clase Archivo
class Archivo:
    def __init__(self, nombre, ext, peso, fecha):
        self.nombre = nombre
        self.ext = ext
        self.peso = peso
        self.fecha = fecha

    def dict(self):
        """ Regresa la versión en diccionario de un objeto Archivo """
        return {
            "nombre":self.nombre,
            "ext":self.ext,
            "peso": self.peso,
            "fecha": self.fecha.isoformat()
        }

    def list(self):
        """ Regresa la versión en lista de un objeto Archivo """
        return [self.nombre, self.ext, self.peso, self.fecha]


# Se aplicará MVC para el desarrollo del script

# Modelo: Obtener la lista de archivos
def obtener_archivos(ruta="."):
    archivos = os.listdir(ruta)  # Obtiene la lista de nombres de archivos
    archivos = [os.path.join(ruta, a) for a in archivos]  # Se agrega la ruta

    lista_archivos = []
    for archivo in archivos:
        ts = os.path.getmtime(archivo)  # Fecha de modificación en timestamp
        obj_archivo = Archivo(
            archivo,
            os.path.splitext(archivo)[1],  # extensión
            os.path.getsize(archivo),  # Tamaño en bytes
            datetime.datetime.fromtimestamp(ts)  # fecha python
        )
        lista_archivos.append(obj_archivo)

    return lista_archivos  # Regresa una lista de objetos Archivo

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
        print("{nombre:36} {ext:5} {peso:10} {fecha:26}".format(**arch.dict()))
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
    lista = obtener_archivos(ruta)  # Regresa una lista de objetos Archivo
    lista_ordenada = sorted(lista, key=lambda o: o.nombre)

    if archcsv == "":
        imprime_archivos(lista_ordenada)  # Imprime lista de objetos Archivo
    else:
        guarda_archivos_csv(lista_ordenada, archcsv)  # Guarda lista de objetos

# Es para definri si el script es un script principal o un módulo
if __name__ == "__main__":
    lsn()


