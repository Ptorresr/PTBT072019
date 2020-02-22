#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Módulo encargado de realizar las operaciones a la base de datos MariaDB
"""

# Datos de conexión a la base de datos
BD = {
    "database":"Biblioteca",
    "host":"localhost",
    "user":"Biblioteca",
    "password":"Biblioteca"
}

# zona de imports
from mysql.connector import connect, Error


def conecta_bd():
    """
    Se conecta a la base de datos BD, regresa un conecto o None en caso
    de error.
    """
    try:
        conn = connect(**BD)  # host="localhost", database="Biblioteca", ...
    except Error as err:
        print(err)
        return None

    return conn

def obtiene_registros(tabla):
    """
    Obtiene la lista de registros de tabla y los regresa en forma de lista
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SELECT * FROM {}".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de campos y se agrega como primer posición en la
        # lista de resultados.
        registros = [[r[0].capitalize() for r in cur.description]]
        # Se obtiene la lista de resultados de la consulta SQL
        registros += cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def obtiene_tablas():
    """
    Obtiene la lista de tablas en la base de datos
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()
        # Se crea la consulta SQL
        sql = "SHOW TABLES"
        # Se ejecuta la consulta
        cur.execute(sql)
        # Se obtiene la lista de resultados de la consulta SQL
        registros = cur.fetchall()
        # Se cierra la BD
        conn.close()

        return registros
    else:
        # Si no hay conexión a la BD regresamos una lista vacía
        return []

def agrega_registro(tabla, campos):
    """
    Agrega un nuevo registro a -tabla- en la BD

    Regresa "" si no hay error, de lo contrario regrea un mensaje de error
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()

        # Crear la consulta SQL para insertar el registro
        sql = "INSERT INTO {} VALUES (null, %s, %s, %s, %s)".format(tabla)
        # Se ejecuta la consulta
        cur.execute(sql, campos)
        # Realizar la inserción de forma atómica
        conn.commit()
        # Se cierra la BD
        conn.close()

        return ""  # no hay error
    else:
        # Si no hay conexión a la BD regresamos una mensaje 
        return "Error: Problemas con la conexión a la BD"
    
def elimina_registro(tabla, id):
    """
    Elimina un registro con -id- de -tabla- en la BD

    Regresa True en caso borrar el registro exitosamente y False en caso
    contrario
    """
    # Se realiza la conexión a la base de datos
    conn = conecta_bd()
    if conn:
        # Se obtiene un cursor o indice a la base de datos
        cur = conn.cursor()

        # Crear la consulta SQL para insertar el registro
        sql = ""  # Completar la consulta SQL!
        # Se ejecuta la consulta
        cur.execute(sql)  # Así está bien o le falta algo?
        # Realizar la inserción de forma atómica
        conn.commit()  # Se tiene que hacer commit o no?
        # Se cierra la BD
        conn.close()

        return True  # no hay error
    else:
        # Si no hay conexión a la BD regresamos false
        return False
    
