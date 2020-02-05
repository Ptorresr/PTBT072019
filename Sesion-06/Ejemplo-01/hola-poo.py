#!/usr/bin/env python
# -*- coding: utf-8

class Persona:
    def __init__(self, nom, edad, peso, genero):
        self.nombre = nom
        self.edad = edad
        self.peso = peso
        self.genero = genero

    def __str__(self):
        return "Hola soy {}".format(self.nombre)

    def dame_edad(self):
        """ Regresa la edad de la persona """
        if self.genero == "M":
            return self.edad
        else:
            return self.edad + 10

class ObjetoB:
    pass

def A():
    print("soy la función A")

A()

persona = Persona("Diana", 45, 90, "F")
objB = ObjetoB()

print(type(persona))
print(persona.nombre)
print(persona.edad)
print(persona.peso)
print(persona.genero)
print(persona)
print(persona.dame_edad())

