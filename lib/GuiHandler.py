#!/usr/bin/env python
'''Clase base para generar la Interfaz Grafica de Usuario'''

import OptionManager
import cairo
import math

class GuiHandler():
    ''' Genera el fondo de la GUI'''
    
    def get_output(self):
        return self.texture
    
    def set_function_1_name(self, func1):
        self.func1 = func1
    
    def set_function_2_name(self, func2):
        self.func2 = func2
        
    def set_function_3_name(self, func3):
        self.func3 = func3
    
    def set_title(self, title):
        self.title = title
    
    def get_title(self):
        return self.title
    
    def get_width(self):
        return self.width
        
    def get_height(self):
        return self.height
    
    def get_image_path(self):
        return "Screen.png"
    
    def refresh_gui(self):
        ''' Redibuja el listado de opciones'''
        self.paint_background()
        self.paint_foreground()
    
    def paint_background(self):
    
        # Fondo
        gradient = cairo.LinearGradient(0, 0, 0, self.height)
        
        gradient.add_color_stop_rgb(0, .36, .3, .62)
        gradient.add_color_stop_rgb(1, .65, .76, .68)
        
        self.cr.set_source(gradient)
        self.cr.rectangle(0, 0, self.width, self.height)
        self.cr.fill()
        
    def paint_foreground(self):
    
        # Barra de funciones
        self.cr.set_source_rgba(1, 1, 1, .4)
        self.cr.move_to(2, self.height)
        self.cr.line_to(2, self.height - 50)
        self.cr.arc(12, self.height - 50, 10, math.pi, -.5 * math.pi)
        self.cr.line_to(self.width - 12, self.height - 60)
        self.cr.arc(self.width - 12, self.height - 50, 10, -.5 * math.pi, 0)
        self.cr.line_to(self.width - 2, self.height)
        self.cr.close_path()
        self.cr.fill_preserve()
        
        gradient = cairo.LinearGradient(0, 0, self.width, 0)
        
        gradient.add_color_stop_rgba(0, 0, 0, 0, .4)
        gradient.add_color_stop_rgba(1, 1,1,1,.5)
        self.cr.set_line_width(3)
        self.cr.set_source(gradient)
        self.cr.stroke()
        
        # Segnal
        self.cr.set_line_width(2)
        for i in range(5):
            self.cr.move_to(10 + i * 10, 32)
            self.cr.line_to(10 + (i + 1) * 10, 32)
            self.cr.line_to(10 + (i + 1) * 10, 24 - i * 5)
            self.cr.line_to(10 + i * 10, 24 - i * 5)
            self.cr.close_path()
        
        self.cr.set_source_rgb(0,0.4, .9)
        self.cr.fill_preserve()
        self.cr.set_source_rgba(1,1,1,.3)
        self.cr.stroke()
        
        #Pila
        gradient = cairo.LinearGradient(self.width - 53, 0, self.width - 10, 0)
        gradient.add_color_stop_rgb(0, 0, .4, .9)
        gradient.add_color_stop_rgb(1, 0, .9, .4)
        self.cr.set_source(gradient)
        self.cr.move_to(self.width - 53, 25)
        self.cr.line_to(self.width - 50, 25)
        self.cr.line_to(self.width - 50, 30)
        self.cr.line_to(self.width - 10, 30)
        self.cr.line_to(self.width - 10, 10)
        self.cr.line_to(self.width - 50, 10)
        self.cr.line_to(self.width - 50, 15)
        self.cr.line_to(self.width - 53, 15)
        self.cr.close_path()
        self.cr.fill_preserve()
        self.cr.set_source_rgba(1,1,1,.3)
        self.cr.stroke()
        
        # Renderizado de titulo y nombre de funciones
        self.cr.set_source_rgb(1, 1, 1)
        self.cr.set_font_size(26) 
        
        bounds = self.cr.text_extents(self.title)
        self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 65)
        self.cr.text_path(self.title)
        self.cr.fill()
        
        self.cr.set_font_size(24)
        self.cr.set_source_rgb(0, 0, 0)
        
        bounds = self.cr.text_extents(self.func1)
        self.cr.move_to(10, self.height - 20)
        self.cr.text_path(self.func1)
        
        bounds = self.cr.text_extents(self.func2)
        self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), self.height - 20)
        self.cr.text_path(self.func2)
        
        bounds = self.cr.text_extents(self.func3)
        self.cr.move_to(self.width - 10 - bounds[2], self.height - 20)
        self.cr.text_path(self.func3)
        self.cr.fill()
        
    def state_changed(self, signal):
        ''' Establece una nueva seleccion
            param signal El identificador de la tecla presionada'''
            
        self.refresh_gui()
    
    def to_string(self):
        ''' Representa la lista de objetos que se debe de mostrar,
            en una cadena'''
            
        pass
        
    def truncate_text(self, text, width):
        
        aux = text
        i = 1
        while self.cr.text_extents(aux)[2] > width:
            aux = text[0: len(text) - i] + "..."
            i += 1
        
        return aux
        
    
    def __init__(self, texture_path):
        ''' Constructor'''
        
        self.title = "Prueba"
        self.func1 = "func1"
        self.func2 = "func2"
        self.func3 = "func3"
        self.scale = 3
        self.width = 128 * self.scale
        self.height = 160 * self.scale
        self.padding = 2
        self.top_margin = 75
        self.texture = texture_path
        
        self.surface = cairo.ImageSurface (cairo.FORMAT_ARGB32,
                                           self.width, self.height)
        
        self.cr = cairo.Context(self.surface)
        
   
