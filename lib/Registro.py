#!/usr/bin/env python
''' Abstraccion de registro de llamadas telefonicas'''

import Util
import time

class Registro:
    ''' Clase que representa un registro de llamada Realizada,
        Recibida o Perdida.'''

    ESTADOS = ('REALIZADA', 'RECIBIDA', 'PERDIDA')
    
    __tagRegistro = 'Registro'
    __tagTelefono = 'Telefono'
    __tagEstado = 'Estado'
    __tagTimeStamp = 'Tiempo'

    def get_tag_registro():
        ''' Obtiene la etiqueta que especifica a un Registro.
            return La etiqueta del nodo Registro.'''
        
        return Registro.__tagRegistro
    get_tag_registro = staticmethod(get_tag_registro)

    def get_tag_telefono():
        ''' Obtiene la etiqueta que especifica al Telefono de un Registro.
            return La etiqueta del nodo Telefono.'''
        
        return Registro.__tagTelefono
    get_tag_telefono = staticmethod(get_tag_telefono)

    def get_tag_estado():
        ''' Obtiene la etiqueta que especifica al Estado de un Registro.
            return La etiqueta del nodo Estado'''
        
        return Registro.__tagEstado
    get_tag_estado = staticmethod(get_tag_estado)

    def get_tag_time_stamp():
        ''' Obtiene la etiqueta que especifica al Estado de un Registro.
            return La etiqueta del nodo TimeStamp'''
        
        return Registro.__tagTimeStamp
    get_tag_time_stamp = staticmethod(get_tag_time_stamp)
    
    def get_info(self):
        res = None
        date_time = str(time.ctime(self.timestamp))
        if self.nombre:
            res = [None, self.telefono, date_time, self.nombre]
        else:
            res = [None, self.telefono, date_time]
        
        return res;

    def set_estado(self, estado):
        ''' Establece el Estado de un Registro.
            param estado El Estado del Registro.'''
        
        if estado in Registro.ESTADOS:
            self.estado = estado

    def set_telefono(self, telefono):
        ''' Establece el Telefono de un Registro.
            param telefono El Telefono del Registro.'''
        
        self.telefono = telefono

    def set_nombre(self, nombre):
        ''' Establece el Nombre de un Registro.
            param nombre El Nombre del Registro.'''
        
        self.nombre = nombre

    def get_estado(self):
        ''' Obtiene el Estado de un Registro.
            return El Estado del Registro.'''
        
        return self.estado

    def get_telefono(self):
        ''' Obtiene el Telefono de un Registro.
            return El telefono del Registro.'''
        
        return self.telefono

    def get_nombre(self):
        ''' Obtiene el Nombre de un Registro.
            return El nombre de la persona registrada.'''
        
        return self.nombre

    def get_time_stamp(self):
        ''' Obtiene el tiempo en el que se registro la llamada.
            return Dia y hora en que se hizo el registro.'''
        
        return self.timestamp

    def get_id(self):
        ''' Obtiene el Identificador de un Registro.
            return Identificador del Registro'''
        
        return self.ident

    def __repr__(self):
        ''' Representa la informacion de un Registro.
            return Representacion de la instancia.'''
        
        cadena = ''

        if not self.nombre == None:
            cadena += 'Nombre: ' +  self.nombre + ' '

        cadena += Registro.__tagTelefono + ": " + self.get_telefono()
        cadena += " "
        cadena += Registro.__tagEstado + ": " + self.get_estado()
        cadena += " " + time.ctime(self.timestamp)
        cadena += " " + self.get_id()
        return cadena

    def toxml(self):
        ''' Representa la informacion de un Registro en una estructura XML
            return La representacion xml.'''
        
        xml = '<' + Registro.__tagRegistro + ' id="' + self.ident + '">'

        xml += '<' + Registro.__tagTelefono + '>'
        xml += self.get_telefono()
        xml += '</' + Registro.__tagTelefono + '>'

        xml += '<' + Registro.__tagEstado + '>'
        xml += self.get_estado()
        xml += '</' + Registro.__tagEstado + '>'

        xml += '<' + Registro.__tagTimeStamp + '>'
        xml += str(self.get_time_stamp())
        xml += '</' + Registro.__tagTimeStamp + '>'

        xml += '</' + Registro.__tagRegistro + '>'
        return xml 

    def __init__(self, telefono, estado, timestamp, ident):
        ''' Constructor de Registro.
            param telefono El telefono del Registro.
            param estado El estado del Registro.
            param timestamp El tiempo en que se creo el Registro.
            param id El identificador del Registro.'''
        
        self.telefono = telefono
        self.estado = estado
        self.nombre = None

        if timestamp ==  None:
            self.timestamp = time.time()
        else:
            self.timestamp = timestamp

        if ident == None:
            self.ident = Util.generate_id()
        else:
            self.ident = ident
