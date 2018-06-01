#!/usr/bin/python
# -*- coding: utf-8 -*-

class user:

    def __init__(self,nombre,apellido):
        self.nombre=nombre
        self.apellido=apellido
    
    def serializable(self):
        return {'nombre':self.nombre, 'apellido':self.apellido}
