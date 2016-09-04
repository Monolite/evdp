#!/usr/bin/env python
''' Clase base de Interfaz Grafica de Usuario'''

from GuiHandler import GuiHandler
import cairo

class ListMenuApp(GuiHandler):
    ''' Permite manipular la GUI del dispositivo'''
    
    def get_image_path(self):
        return "Screen.png"
    
    def refresh_gui(self):
        ''' Redibuja el listado de opciones'''
        GuiHandler.refresh_gui(self)
        
        if len(self.options) > self.list_size:
            aux_list = self.options[self.offset : self.offset + self.list_size]
        else:
            aux_list = self.options
        
        # Creacion del menu de opciones
        for y in range(len(aux_list)):
                    
            if(self.selected_index == self.options.index(aux_list[y])):
                self.cr.set_source_rgba(0.1, .1, .1, .6)
            else:
                self.cr.set_source_rgba(1, 1, 1, .4)

            self.cr.move_to(0 , y * self.option_height + self.padding + self.top_margin)
            self.cr.line_to(self.option_width, y * self.option_height + self.padding + self.top_margin)
            self.cr.line_to(self.option_width, y * self.option_height + self.option_height + self.top_margin)
            self.cr.line_to(0, y * self.option_height + self.option_height + self.top_margin)
            self.cr.close_path()
            self.cr.fill()
            self.cr.set_font_size(20)
            self.cr.move_to(10, (y+1) * (self.option_height) - 8 * self.padding + self.top_margin)
            if(self.selected_index == self.options.index(aux_list[y])):
                self.cr.set_source_rgb(1,1,1)
            else:
                self.cr.set_source_rgb(0,0,0)
            self.cr.text_path(aux_list[y][0])
            self.cr.fill()
        
        self.surface.write_to_png(self.get_output())
                
    
    def select_next(self):
        ''' Selecciona siguiente opcion'''
        
        if self.selected_index < len(self.options) - 1:
            self.selected_index += 1
            if self.selector_pos + self.offset < len(self.options): 
                if self.selector_pos < (self.list_size - 1):
                    self.selector_pos += 1
                else:
                    self.offset += 1
        self.refresh()
        
    def select_previous(self):
        ''' Selecciona opcion anterior'''
        
        if self.selected_index > 0:
            self.selected_index -= 1
            if self.selector_pos + self.offset > 0: 
                if self.selector_pos > 1:
                    self.selector_pos -= 1
                else:
                    if self.offset > 0:
                        self.offset -= 1
        self.refresh()
    
    def activate(self, events):
        self.refresh()
        events.add_action("aro_centro1", self.select_previous)
        events.add_action("aro_centro3", self.select_next)
        events.add_action("boton_izq1", self.quit)
        
    def quit(self):
        self.parent.launch("menu")
        
    def refresh(self):
        self.refresh_gui()
        self.parent.repaint()
    
    def to_string(self):
        ''' Representa la lista de objetos que se debe de mostrar,
            en una cadena'''
            
        aux_list = self.options[self.offset : 
                                self.offset + len(self.list_items)]
        
        res = ""
        
        i = 0
        for item in aux_list:
            aux_s = "Item " + str(i) + ": " + str(item)
            if self.options.index(item) == self.selected_index:
                aux_s += " <<  index: " + str(self.selected_index)
            res += aux_s + '\012'
            i += 1
        
        return res
    
    def __init__(self, menu_options, device):
        ''' Constructor'''
        
        GuiHandler.__init__(self)
        
        self.parent = device
        
        self.offset = 0
        self.selector_pos = 0
        self.selected_index = 0
        self.list_size = 6
        
        self.option_height = 18 * self.scale
        self.option_width = self.width
        self.options = []
        
        if menu_options:
            self.options = menu_options
   
