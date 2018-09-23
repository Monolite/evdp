#!/usr/bin/env python
''' Permite gestionar los registros de llamadas a traves de un archivo 
    Registro.xml'''

from Registro import Registro
from GestorContactos import GestorContactos
from xml.dom import minidom
import os

class GestorRegistros:
    ''' Gestiona los Registros de Llamadas.'''
    
    __documento = 'res/xml/Registros.xml'
    
    def agregar_registro(registro):    
        ''' Registra un una nueva llamada.
            param registro Un objeto Registro.'''
        
        nuevo = minidom.parseString(registro.toxml())
        documento = minidom.parse(GestorRegistros.__documento)
        
        documento.firstChild.appendChild(nuevo.firstChild)
        GestorRegistros.__crear_documento(
                                documento.toxml('UTF-8').encode('utf8'))
    agregar_registro = staticmethod(agregar_registro)

    def __crear_documento(texto):
        ''' Genera un documento xml.
            param texto El texto que sera escrito en el documento xml.'''
            
        new_doc = open(GestorRegistros.__documento, 'w')
        new_doc.write(texto)
        new_doc.close()
    __crear_documento = staticmethod(__crear_documento)

    def __listar_registros():
        ''' Lista los registros establecidos en el archivo __documento.
            return Una lista no ordenada de instancias Registro.'''
            
        lista = []
        documento = minidom.parse(GestorRegistros.__documento)
        regs = documento.getElementsByTagName(Registro.get_tag_registro())
        contactos = GestorContactos()

        for reg in regs:

            ident = reg.getAttribute('id')

            estado = reg.getElementsByTagName(Registro.get_tag_estado())
            telefono = reg.getElementsByTagName(Registro.get_tag_telefono())
            timestamp = reg.getElementsByTagName(Registro.get_tag_time_stamp())

            reg_st = estado.item(0).firstChild.data
            reg_tel = telefono.item(0).firstChild.data
            reg_ts = float(timestamp.item(0).firstChild.data)

            cntc = contactos.get_contact_by_phone(reg_tel)

            reg = Registro(reg_tel.encode(), reg_st.encode(), reg_ts, ident.encode())

            if cntc:
                reg.set_nombre(cntc.get_nombre().encode())
            
            lista.append(reg)

        return lista
    __listar_registros = staticmethod(__listar_registros)

    def get_registros():
        ''' Enumera los Registros.
            return Una lista ordenada de instancias Registro.'''
            
        lista = GestorRegistros.__listar_registros()
        lista.sort(GestorRegistros.__ordenar_registros)
        return lista
    get_registros = staticmethod(get_registros)

    def get_logs_by_state(estado):
        ''' Obtiene el Registro cuyo estado sea el especificado.
            param estado El estado de registro que se desea enlistar.
            return Una lista de objetos Registro con el estado especificado.'''
            
        reg_list = GestorRegistros.get_registros()
        regs = []
        
        if estado in Registro.ESTADOS:
            for reg_aux in reg_list:
                if reg_aux.get_estado() == estado:
                    regs.append(reg_aux)

        return regs
    get_logs_by_state = staticmethod(get_logs_by_state)
    
    def get_log_by_id(ident):
        ''' Obtiene el Registro cuyo identificador sea el especificado.
            param id El identificador del registro que se desea obtener.
            return El Registro con el identificador especificado.'''
            
        reg_list = GestorRegistros.get_registros()
        reg = None

        for reg_aux in reg_list:
            if reg_aux.get_id() == ident:
                reg = reg_aux

        return reg
    get_log_by_id = staticmethod(get_log_by_id)

    def eliminar_registro(ident):
        ''' Elimina el registro cuyo identificador sea el especificado.
            param id El identificador del registro que se desea eliminar.'''
        
        reg_list = GestorRegistros.__listar_registros()
        reg = GestorRegistros.get_log_by_id(ident)

        if reg:
            xml = minidom.Document()
            root = xml.createElement("Registros")
            xml.appendChild(root)

            for reg_aux in reg_list:
                if not reg_aux.getId() == reg.get_id():
                    nuevo = minidom.parseString(reg_aux.toxml())
                    xml.firstChild.appendChild(nuevo.firstChild)

            GestorRegistros.__crear_documento(xml.toxml('UTF-8').encode('utf8'))
    eliminar_registro = staticmethod(eliminar_registro)

    def __ordenar_registros(reg_a, reg_b):
        ''' Permite comparar dos instancias Registro
            param a Un registro que se desea comparar.
            param b Otro registro a comparar.'''
        
        if reg_a.get_time_stamp() > reg_b.get_time_stamp():
            return 1
        elif reg_a.get_time_stamp() == reg_b.get_time_stamp():
            return 0
        else:
            return -1
    __ordenar_registros = staticmethod(__ordenar_registros)

    def __init__(self):
        ''' Constructor del Gestor de Registros.'''
        
        if not os.path.isfile(GestorRegistros.__documento):
            xml = minidom.Document()
            root = xml.createElement("Registros")
            xml.appendChild(root)
            GestorRegistros.__crear_documento(xml.toxml('UTF-8').encode('utf8'))

