#!/usr/bin/env python
''' Clase que permite gestionar los contactos de un celular.'''

from Contacto import Contacto
from xml.dom import minidom
import os

class GestorContactos:
    ''' Gestiona los contactos.'''
    
    __documento = 'res/xml/Contactos.xml'
    
    def agregar_contacto(contacto):
        ''' Registra un nuevo contacto.
            param contacto Un objeto Contacto a registrar.'''
        
        nuevo = minidom.parseString(contacto.toxml())
        doc = minidom.parse(GestorContactos.__documento)
        
        doc.firstChild.appendChild(nuevo.firstChild)
        GestorContactos.__crear_documento(doc.toxml('UTF-8').encode('utf8'))
    agregar_contacto = staticmethod(agregar_contacto)

    def __crear_documento(texto):
        ''' Genera un documento xml.
            param texto El texto que sera escrito en el documento xml.'''
        
        new_doc = open(GestorContactos.__documento, 'w')
        new_doc.write(texto)
        new_doc.close()
    __crear_documento = staticmethod(__crear_documento)

    def __listar_contactos():
        ''' Lista los contactos establecidos en el archivo __documento.
            return Una lista no ordenada de instancias Contacto.'''
        
        lista = []
        documento = minidom.parse(GestorContactos.__documento)
        cts = documento.getElementsByTagName(Contacto.get_tag_contacto())

        for cntc in cts:

            ident = cntc.getAttribute('id')

            nombre = cntc.getElementsByTagName(Contacto.get_tag_nombre())
            telefono = cntc.getElementsByTagName(Contacto.get_tag_telefono())

            cnom = nombre.item(0).firstChild.data
            ctel = telefono.item(0).firstChild.data

            lista.append(Contacto(cnom.encode(), ctel.encode(), ident.encode()))

        return lista
    __listar_contactos = staticmethod(__listar_contactos)

    def get_contactos():
        ''' Enumera los contactos que se han registrado.
            return Una lista de objetos Contacto.'''
        
        lista = GestorContactos.__listar_contactos()
        lista.sort(GestorContactos.__ordenar_contactos)
        return lista
    get_contactos = staticmethod(get_contactos)

    def get_contact_by_phone(telefono):
        ''' Obtiene el contacto cuyo telefono sea el especificado.
            param telefono El telefono del contacto que se desea obtener.
            return El contacto con el telefono especificado.'''
        
        lista = GestorContactos.get_contactos()
        cntc = None

        for contacto in lista:
            if contacto.get_telefono() == telefono:
                cntc = contacto

        return cntc
    get_contact_by_phone = staticmethod(get_contact_by_phone)

    def get_contact_by_id(ident):
        ''' Obtiene el contacto cuyo identificador sea el especificado.
            param id El identificador del contacto que se desea obtener.
            return El contacto con el identificador especificado.'''
        
        lista = GestorContactos.get_contactos()
        cntc = None

        for cont in lista:
            if cont.get_id() == ident:
                cntc = cont

        return cntc
    get_contact_by_id = staticmethod(get_contact_by_id)

    def eliminar_contacto(ident):
        ''' Elimina el contacto cuyo identificador sea el especificado.
            param id El identificador del contacto que se desea eliminar.'''
        
        lista = GestorContactos.__listar_contactos()
        cntc = GestorContactos.get_contact_by_id(ident)

        if cntc:
            xml = minidom.Document()
            root = xml.createElement("Contactos")
            xml.appendChild(root)

            for contacto in lista:
                if not contacto.getId() == cntc.getId():
                    nuevo = minidom.parseString(contacto.toXml())
                    xml.firstChild.appendChild(nuevo.firstChild)

            GestorContactos.__crear_documento(xml.toxml('UTF-8').encode('utf8'))
    eliminar_contacto = staticmethod(eliminar_contacto)

    def __ordenar_contactos(cont_a, cont_b):
        ''' Permite comparar dos instancias Registro
            param cont_a Un registro que se desea comparar.
            param cont_b Otro registro a comparar.'''
        
        if cont_a.get_nombre() > cont_b.get_nombre():
            return 1
        elif cont_a.get_nombre() == cont_b.get_nombre():
            return 0
        else:
            return -1
    __ordenar_contactos = staticmethod(__ordenar_contactos)

    def __init__(self):
        ''' Constructor del Gestor de Contactos'''
        
        if not os.path.isfile(GestorContactos.__documento): #Buscando
                                                            #documento existente
            xml = minidom.Document()
            root = xml.createElement("Contactos")
            xml.appendChild(root)
            GestorContactos.__crear_documento(xml.toxml('UTF-8').encode('utf8'))

