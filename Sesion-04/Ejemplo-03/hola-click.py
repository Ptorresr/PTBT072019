#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click

@click.command()
@click.argument("nombre")
def hola(nombre):
    """
    Imprime un saludo a -nombre-
    """
    print("Hola {}".format(nombre))


if __name__ == "__main__":
    hola()
