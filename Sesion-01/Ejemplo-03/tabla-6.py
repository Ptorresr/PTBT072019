#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Imprimir la tabla del 6 en la salida estándar
"""
k = 6

print("Tabla del 6")
print("-" * 15)
for i in range(1, 11):
    print("{:2} x {} = {:2}".format(i, k, i*k))
print("-" * 15)
