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
"""

import click
import datetime
import os
import sys

# Se aplicará MVC para el desarrollo del script

# Modelo: Obtener la lista de archivos
def obtener_archivos(ruta="."):
    archivos = os.listdir(ruta)
    # Solución estandar
    # archivos2 = []
    # for a in archivos:
    #     b = os.path.join(ruta, a)
    #     archivos2.append(b)
    # archivos = archivos2
    # Solución estilo Python
    archivos = [os.path.join(ruta, a) for a in archivos]


    lista_archivos = []
    for archivo in archivos:
        ts = os.path.getmtime(archivo)  # Fecha de modificación en timestamp
        d_archivo = {
            "nombre": archivo,
            "ext": os.path.splitext(archivo)[1],  # extensión
            "fecha": datetime.datetime.fromtimestamp(ts).isoformat(),  # fecha iso8601
            "peso": os.path.getsize(archivo)  # Tamaño en bytes
        }
        lista_archivos.append(d_archivo)

    return lista_archivos

def guarda_archivos_csv(lista_archivos, nom_arch):
    """
    Guarda la lista de archivos en nom_arch en formato csv.
    """
    da = open(nom_arch, "w")
    for arch in lista_archivos:
        da.write("{nombre},{ext},{peso},{fecha}\n".format(**arch))
    da.close()

# Vista: Imprimir la lista de archivos
def imprime_archivos(lista_archivos):
    print("-"*40)
    for arch in lista_archivos:
        # print("{:36} {:5} {:10} {:26}".format(arch["nombre"], arch["ext"], arch["peso"],
        print("{nombre:36} {ext:5} {peso:10} {fecha:26}".format(**arch))
        # **arch->(nombre="hola.py"),ext=".py",fecha="xx",peso=1234) 
    print("-"*40)


# Controlador: lsn()
@click.command()
@click.option("--arch", default="", help="Guarda la lista en NOMBRE en formato CSV")
@click.argument("ruta", default=".")
def lsn(arch, ruta):
    """
    Imprime la lista de archivo en la salida estándar de la carpeta
    proporcionada por el usuario.

    Si el usuario no proporciona ninguna, se imprimen los archivos de la
    carpeta actual.
    """
    lista = obtener_archivos(ruta)
    lista_ordenada = sorted(lista, key=lambda d: d["nombre"])

    if arch == "":
        imprime_archivos(lista_ordenada)
    else:
        guarda_archivos_csv(lista_ordenada, arch)

# Es para definri si el script es un script principal o un módulo
if __name__ == "__main__":
    lsn()


