#!/usr/bin/env python
# -*- coding: utf-8

"""
Crear un archivos de texto, leer el contenido del archivo creado e imprimir en la
salida estándar.
"""

texto = """
Este es el contenido del archivo
---
Línea 1
Línea 2
Línea 3
---
"""

nom_arch = "hola.txt"

# Modelo ---
# Creamos un arcivo de texto en modo escritura (w - write)
da = open(nom_arch, "w")
da.write(texto * 2)
da.write(texto)
da.write("Última línea\n")
da.close()

# Leer un archivo de texto en modo lectura (r - read)
da = open(nom_arch)
texto_archivo = da.read()
da.close()

# Vista: ---
# Imprimir contenido
print(texto_archivo)


# Controlador
lineas = texto_archivo.splitlines()
print(lineas)
print(lineas[-1])

