#!/usr/bin/env python
''' Clase base de Interfaz Grafica de Usuario'''

from GuiHandler import GuiHandler
import cairo

class ListRenderer(GuiHandler):
    ''' Permite manipular la GUI del dispositivo'''
    
    def set_list(self, options, item):
        self.options = options
        self.selected_item = item
    
    def refresh_gui(self):
        ''' Redibuja el listado de opciones'''
        GuiHandler.refresh_gui(self)
        
        # Creacion del menu de opciones
        for y in range(len(self.options)):
        
            if self.options[y] == self.selected_item:
                self.cr.set_source_rgba(0.1, .1, .1, .6)
            else:
                self.cr.set_source_rgba(1, 1, 1, .4)
            
            self.cr.rectangle(0 , y * self.option_height + self.padding + self.top_margin, 
                              self.option_width, self.option_height)
            self.cr.fill()
            
            if self.options[y] == self.selected_item:
                self.cr.set_source_rgb(1,1,1)
            else:
                self.cr.set_source_rgb(0,0,0)

            if 'tuple' in str(type(self.options[y])):
                
                self.cr.set_font_size(20)
                
                self.cr.move_to(10, (y+1) * (self.option_height) - 8 * self.padding + self.top_margin)
                
                text = self.truncate_text(self.options[y][0], self.width - 12)
                self.cr.text_path(text)
                self.cr.fill()
                
            elif 'instance' in str(type(self.options[y])):
                self.cr.set_font_size(18)
                info = self.options[y].get_info()
                
                self.cr.move_to(10, (y+1) * (self.option_height) - 16 * self.padding + self.top_margin)
                
                if len(info) == 3:
                    text = self.truncate_text(info[1], self.width - 12)
                elif len(info) == 4:
                    text = self.truncate_text(info[3], self.width - 12)
                else:
                    text = self.truncate_text(info[0], self.width - 12)
                self.cr.text_path(text)
                self.cr.fill()
                
                self.cr.set_font_size(14)
                self.cr.move_to(20, (y+1) * (self.option_height) - 4 * self.padding + self.top_margin)
                
                if len(info) > 2:
                    text = self.truncate_text(info[2], self.width - 12)
                else:
                    text = self.truncate_text(info[1], self.width - 12)
                self.cr.text_path(text)
                
                self.cr.fill()
            else:
                
                self.cr.set_font_size(20)
                
                self.cr.move_to(10, (y+1) * (self.option_height) - 8 * self.padding + self.top_margin)
                
                text = self.truncate_text(self.options[y], self.width - 12)
                self.cr.text_path(text)
                self.cr.fill()
            
        
        self.surface.write_to_png(self.get_output())
    
    def __init__(self, config):
        ''' Constructor'''
        
        GuiHandler.__init__(self, config.dynamic_texture_path)
        
        self.option_height = 18 * self.scale
        self.option_width = self.width
        self.func1 = ""
        self.func2 = "Seleccionar"
        self.func3 = ""
        self.selected_item = None
        self.list_size = 6
        self.options = None
   
