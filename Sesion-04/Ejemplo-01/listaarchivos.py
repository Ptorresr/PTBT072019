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
"""

import datetime
import os

# Se aplicará MVC para el desarrollo del script

# Modelo: Obtener la lista de archivos
def obtener_archivos():
    archivos = os.listdir()
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


# Vista: Imprimir la lista de archivos
def imprime_archivos(lista_archivos):
    print("-"*40)
    for arch in lista_archivos:
        # print("{:36} {:5} {:10} {:26}".format(arch["nombre"], arch["ext"], arch["peso"],
        print("{nombre:36} {ext:5} {peso:10} {fecha:26}".format(**arch))
        # **arch->(nombre="hola.py"),ext=".py",fecha="xx",peso=1234) 
    print("-"*40)

# Controlador: La función principal
def main():
    lista = obtener_archivos()
    lista_ordenada = sorted(lista, key=lambda d: d["nombre"])
    imprime_archivos(lista_ordenada)

# Es para definri si el script es un script principal o un módulo
print(__name__)
if __name__ == "__main__":
    main()


