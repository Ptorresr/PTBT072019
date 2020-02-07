#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Se encarga de definir las clases para el manejo de archivos
"""

import datetime
import os

class Archivo:
    def __init__(self, ruta):
        """ Constructor de la clase Archivo """
        self.ruta = ruta
        self.peso = os.path.getsize(ruta)
        ts = os.path.getmtime(ruta)
        self.fecha = datetime.datetime.fromtimestamp(ts)  # fecha de tipo datetime

    def dict(self):
        """ Regresa la versión en diccionario de un objeto Archivo """
        return {
            "nombre":self.ruta,
            "peso": self.peso,
            "fecha": self.fecha.isoformat()
        }

    def list(self):
        """ Regresa la versión en lista de un objeto Archivo """
        return [self.ruta, self.peso, self.fecha]


class Carpeta:
    def __init__(self, ruta):
        """ Constructor de la clase Carpeta """
        self.ruta = ruta
        self.peso = 0  # El total de bytes ocupado por lo elementos de la carpeta
        ts = os.path.getmtime(ruta)
        self.fecha = datetime.datetime.fromtimestamp(ts)  # fecha de tipo datetime

    def obtener_archivos(self, ordenar=""):
        """
        Obtiene la lista de archivos de la carpeta
        """
        elementos = os.listdir(self.ruta)  # Obtiene la lista de nombres de archivos
        if ordenar == "nombre":
            elementos.sort()
        elementos = [os.path.join(self.ruta, a) for a in elementos]  # Se agrega la ruta

        lista_elementos = []
        for elemento in elementos:
            if os.path.isdir(elemento):
                carpeta = Carpeta(elemento)
                self.peso += carpeta.peso  # Acumulando los pesos
                lista_elementos.append(carpeta)
                lista_elementos += carpeta.obtener_archivos()  # Recursión a nivel objetos
            else:
                archivo = Archivo(elemento)
                # self.peso = self.peso + archivo.peso
                self.peso += archivo.peso  # Acumulando los pesos 
                lista_elementos.append(archivo)

        return lista_elementos # Regresa una lista de objetos Archivo

    def dict(self):
        """ Regresa la versión en diccionario de un objeto Archivo """
        return {
            "nombre":self.ruta,
            "peso": self.peso,
            "fecha": self.fecha.isoformat()
        }

    def list(self):
        """ Regresa la versión en lista de un objeto Archivo """
        return [self.ruta, self.peso, self.fecha]



