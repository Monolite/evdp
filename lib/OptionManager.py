#!/usr/bin/env python

from xml.dom import minidom

__xmldoc_path = 'res/'
__xmldoc_file_name = 'data/device.xml'
__texture_filename = 'textures/Screen.png'

def get_xmldoc_path():
    return __xmldoc_path

#def get_texture_filename():
#    return __xmldoc_path + __texture_filename

def get_option(option_name):
    ''' Obtiene una opcion determinada.
        param option_name El nombre de la opcion seleccionada
        return Un minidom.Element con el nombre especificado'''
    
    xmldoc = minidom.parse(__xmldoc_path + __xmldoc_file_name)
    opts = xmldoc.getElementsByTagName('Opcion')
    
    option = None
    
    for opt in opts:
        name = opt.getAttribute('name')
        if opt.getAttribute('name') == option_name:
            option = opt

    return option

def get_option_dict(path):
    ''' Obtiene un diccionario de las opciones del menu principal
        return Un diccionario de opciones'''
    
    xmldoc = minidom.parse(__xmldoc_path + __xmldoc_file_name)
    res_dict = {}
    opts = xmldoc.getElementsByTagName('Opcion')
    
    for opt in opts:
        name = opt.getAttribute('name')
        
        if opt.hasAttribute('function'):
            funct = opt.getAttribute('function')
        else:
            funct = 'Exception: Not implemented'
            
        if opt.hasAttribute('icon'):
            icon = path + opt.getAttribute('icon')
        else:
            icon = None
            
        res_dict[opts.index(opt)] = {'name': name.encode(),
                       'function': funct.encode(),
                       'icon': icon.encode()}

    return res_dict

def get_option_subtree(option):
    ''' Obtiene un diccionario de las opciones de algun elemento seleccionado
        param option_name El elemento seleccionado
        return Un listado de opciones'''
    
    arg_type = str(option.__class__)
    if 'str' in arg_type:
        aux = get_option(option)
        return get_option_subtree(aux)
    
    elif 'Element' in arg_type:    
        res_list = []
        elems = option.getElementsByTagName('Elemento')
        
        for elem in elems:
            name = elem.getAttribute('name')
            args = None
            if elem.hasAttribute('function'):
                funct = elem.getAttribute('function')
            else:
                funct = 'Exception: Not implemented'
                
            if elem.hasAttribute('args'):
                args = elem.getAttribute('args')
            
            if args:
                res_list.append((name.encode(), funct.encode(), args.encode()))
            else:
               res_list.append((name.encode(), funct.encode(), None))

        return res_list
    
if __name__ == '__main__':
    
    opcion = get_option("Utileria")
    
    print get_option_dict()
