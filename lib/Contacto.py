#!/usr/bin/env python
''' Abstraccion de Contactos'''

import Util

class Contacto:
    ''' Clase que representa un Contacto.'''
    __tagContacto = 'Contacto'
    __tagNombre = 'Nombre'
    __tagTelefono = 'Telefono'

    def get_tag_contacto():
        ''' Obtiene la etiqueta que especifica a un Contacto.
            return La etiqueta del nodo Contacto.'''
        return Contacto.__tagContacto
    get_tag_contacto = staticmethod(get_tag_contacto)
    
    def get_tag_nombre():
        ''' Obtiene la etiqueta que especifica el Nombre de un Contacto.
            return La etiqueta del nodo Nombre.'''
        return Contacto.__tagNombre
    get_tag_nombre = staticmethod(get_tag_nombre)
    
    def get_tag_telefono():
        ''' Obtiene la etiqueta que especifica el Telefono de un Contacto.
            return La etiqueta del nodo Telefono.'''
        return Contacto.__tagTelefono
    get_tag_telefono = staticmethod(get_tag_telefono)
    
    def set_nombre(self, nombre):
        ''' Establece el Nombre de un Contacto.
            param nombre El Nombre del Contacto.'''
        self.nombre = nombre
    
    def set_telefono(self, telefono):
        ''' Establece el Telefono de un Contacto.
            param telefono El Telefono del Contacto.'''
        self.telefono = telefono
    
    def get_nombre(self):
        ''' Obtiene el Nombre de un Contacto.
            return Nombre del contacto.'''
        return self.nombre
    
    def get_telefono(self):
        ''' Obtiene el Telefono de un Contacto.
            return Telefono del contacto.'''
        return self.telefono
        
    def get_info(self):
        return [self.nombre, self.telefono]
    
    def get_id(self):
        ''' Obtiene el Identificador de un Contacto.
            return Identificador del contacto.'''
        return self.ident
    
    def __repr__(self):
        ''' Representa la informacion de un Contacto.
            return Cadena representativa de la instancia.'''
        cadena = Contacto.__tagNombre + ": " + self.get_nombre()
        cadena += " "
        cadena += Contacto.__tagTelefono + ": " + self.get_telefono()
        cadena += " " + self.get_id()
        return cadena
    
    def toxml(self):
        ''' Representa la informacion de un Contacto en una estructura XML.'''
        xml = '<' + Contacto.__tagContacto + ' id="' + self.ident + '">'
        xml += '<' + Contacto.__tagNombre + '>'
        xml += self.get_nombre()
        xml += '</' + Contacto.__tagNombre + '>'
        
        xml += '<' + Contacto.__tagTelefono + '>'
        xml += self.get_telefono()
        xml += '</' + Contacto.__tagTelefono + '>'
        xml += '</' + Contacto.__tagContacto + '>'
        return xml 
    
    def __init__(self, nombre, telefono, ident):
        ''' Constructor de Contacto.
            param nombre    El Nombre del Contacto.
            param telefono  El Telefono del Contacto.
            param id        El identificador del Contacto o None si no se.
                            ha asignado alguno y debe de ser creados.'''
        
        if ident == None:
            self.ident = Util.generate_id()
        else:
            self.ident = ident
        
        self.nombre = nombre
        self.telefono = telefono
    
