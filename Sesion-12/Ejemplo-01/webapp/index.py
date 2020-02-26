#!/usr/bin/env python
# -*- coding: utf-8 -*-

from bottle import route, run, static_file, request, post

import modelo

HOST = "localhost"
PORT = 8000

# Agregar ruta y vista para atender peticiones de archivos estáticos
@route("/static/<ruta:path>")
def estaticos(ruta):
    """ Atiene la petición de archivos estáticos """
    return static_file(ruta, root="static")

# Agregar ruta y vista para atender petición raíz /
@route("/")
def inicio():
    """ Atienen la petición GET / <- HTTP """
    # Leer el contenido de la plantilla html
    with open("formulario.html") as da:
        html_inicio = da.read()

    return html_inicio

# Agregar ruta y vista para atender petición raíz / con datos POST

@post("/")
def inicio_post():
    """ Procesa la petición POST /  <- HTTP """
    email = request.forms.get("email")
    clave = request.forms.get("clave")

    modelo.guarda_usuario(email, clave)

    usuario = modelo.obtiene_usuario(email)  # (email, clave)

    # Leer el contenido de la plantilla html
    with open("formulario_resp.html") as da:
        html_resp = da.read()

    # Agrega data a la plantilla html
    html_resp = html_resp.format(email=usuario[0], clave=usuario[1])

    return html_resp
# Agregar la data a la plantilla html


if __name__ == "__main__":
    # Inicializa el servidor de la aplicación web
    run(host=HOST, port=PORT, debug=True, reloader=True)
