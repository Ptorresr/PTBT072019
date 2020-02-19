#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, template

@route('/hello/<name>')
def hello(name):
    return template('<h1>Hello {{name}}!</h1>', name=name)

# Definir la ruta /
@route("/")
# Definir la función que atiene la ruta /
def index():
    name = "hola"
    return template('<h1>Bienvenido {{name}}!</h1>', name=name)
    # return "<h1>Bienvenido!</h1>"
    

run(host='localhost', port=8080)

