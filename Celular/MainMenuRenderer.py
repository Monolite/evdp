#!/usr/bin/env python
''' Clase que permite manipular el archivo Menu.svg'''

from GuiHandler import GuiHandler
import OptionManager
import cairo
import math
import os

class MainMenuRenderer (GuiHandler):
    def refresh(self, app):
        self.set_title(app.menu_items[app.selected_index]["Opcion"]["name"])
        GuiHandler.refresh_gui(self)
        
        padding = 4
        x = app.menu_items[app.selected_index]["x"] + self.image_size / 2.0
        y = app.menu_items[app.selected_index]["y"] + self.image_size / 2.0
        
        self.cr.arc(x, y, padding + self.image_size / 2, 0, math.pi * 2)
        
        gradient = cairo.RadialGradient(x , y , self.image_size / 8, x, y , self.image_size / 2)
        gradient.add_color_stop_rgba(0, .6, .9 , 0, .5)
        gradient.add_color_stop_rgba(1, 1, 1 , 0, .2)
        self.cr.set_source(gradient)
        self.cr.fill()
        
        k = 0
        for i in range(3):
            for j in range(3):
                
                path = OptionManager.get_xmldoc_path() + app.menu_items[k]["Opcion"]["icon"]
                
                if os.path.isfile(path):
                    
                    surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.image_size, self.image_size)
                    image = cairo.ImageSurface.create_from_png(path)
                    
                    if(k == app.selected_index):
                        scale = 1.25
                        translate = (self.image_size - scale * self.image_size) / 2.0
                        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, 200, 200)
                        image = cairo.ImageSurface.create_from_png(path)
                        context = cairo.Context(surface)
                        context.translate(translate, translate)
                        context.scale(scale, scale)
                        
                        context.set_source_surface(image, 0, 0)
                        
                        context.paint()
                        
                        self.cr.set_source_surface(surface, app.menu_items[k]["x"], app.menu_items[k]["y"])
                        self.cr.paint()
                    else:
                        surface = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.image_size, self.image_size)
                        image = cairo.ImageSurface.create_from_png(path)
                        self.cr.set_source_surface(image, app.menu_items[k]["x"], app.menu_items[k]["y"])
                        self.cr.paint_with_alpha(.3)
                k += 1
        
                
        self.surface.write_to_png(OptionManager.get_texture_filename())
    
    def __init__(self, app):
        ''' Constructor de MenuHandler'''

        GuiHandler.__init__(self)

        self.image_size = 108
        self.func1 = ""
        self.func2 = "Seleccionar"
        self.func3 = ""
        opciones = OptionManager.get_option_dict()
        padding = 15
        k = 0

        for i in range(3):
            for j in range(3):
                app.menu_items[k] = {"x": ((j+1) * padding + j * self.image_size), "y": (self.top_margin + padding + i * self.image_size), "Opcion" : opciones[k]}
                k = k + 1

        self.set_title(app.menu_items[app.selected_index]["Opcion"]["name"])
        self.refresh(app)
    
