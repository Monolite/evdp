#!/usr/bin/env python
''' Documentacion del archivo'''

from GuiHandler import GuiHandler
import cairo

def get_transformation_matrix(width_a, height_a, width_b, height_b):

    scale_x = float(width_a) / width_b
    scale_y = float(height_a) / height_b
    translate_x = (width_a - width_b * scale_y) / 2.0
    translate_y = (height_a - height_b * scale_x) /2.0
    
    if(scale_y < scale_x):
        translate_y = (height_a - height_b * scale_y) / 2.0
        return cairo.Matrix(scale_y, 0, 0, scale_y, translate_x, translate_y)
    
    translate_x = (width_a - width_b * scale_x) / 2.0
    return cairo.Matrix(scale_x, 0, 0, scale_x, translate_x, translate_y)

class InitApp(GuiHandler):

    def __init__(self, device):
        self.parent = device
        GuiHandler.__init__(self)
        self.func3 = ""
        self.func2 = "Menu"
        self.func1 = "" 
        self.title = "Mi Celular"
        self.number = ""
    
    def paint_background(self):
        # Fondo
        image_path = "res/img/background.png"
        surface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.width, self.height)
        context = cairo.Context(surface)
        
        image = cairo.ImageSurface.create_from_png(image_path)

        context.transform(get_transformation_matrix(self.width, self.height, image.get_width(), image.get_height()))
        
        context.set_source_surface(image, 0, 0)
        context.paint()
        
        self.cr.set_source_surface(surface)
        self.cr.paint()
    
    def refresh_gui(self):
        GuiHandler.refresh_gui(self)
        self.surface.write_to_png(self.get_output())
    
    def refresh(self):
        self.refresh_gui()
        self.parent.repaint()
        
    def activate(self, events):
        self.refresh()
        
        events.add_action("centro", self.call_menu)

        events.add_action("aro_centro3", self.exec_contact_list)
        
        events.add_action("boton1", self.write_1)
        events.add_action("boton2", self.write_2)
        events.add_action("boton3", self.write_3)
        events.add_action("boton4", self.write_4)
        events.add_action("boton5", self.write_5)
        events.add_action("boton6", self.write_6)
        events.add_action("boton7", self.write_7)
        events.add_action("boton8", self.write_8)
        events.add_action("boton9", self.write_9)
        events.add_action("botonc", self.write_numb)
        events.add_action("botona", self.write_astrsk)
        events.add_action("botonb", self.write_0)

    def exec_contact_list(self):
        self.parent.launch("Lista de Contactos")
    
    def get_number(self):
        return self.number
    
    def call_menu(self):
        self.parent.launch("menu")
        
    def write_1(self):
        self.number = "1"
        self.parent.launch("Dial")
        
    def write_2(self):
        self.number = "2"
        self.parent.launch("Dial")
    
    def write_3(self):
        self.number = "3"
        self.parent.launch("Dial")
    
    def write_4(self):
        self.number = "4"
        self.parent.launch("Dial")
        
    def write_5(self):
        self.number = "5"
        self.parent.launch("Dial")
    
    def write_6(self):
        self.number = "6"
        self.parent.launch("Dial")
    
    def write_7(self):
        self.number = "7"
        self.parent.launch("Dial")
        
    def write_8(self):
        self.number = "8"
        self.parent.launch("Dial")
    
    def write_9(self):
        self.number = "9"
        self.parent.launch("Dial")
        
    def write_0(self):
        self.number = "0"
        self.parent.launch("Dial")
        
    def write_astrsk(self):
        self.number = "*"
        self.parent.launch("Dial")
    
    def write_numb(self):
        self.number = "#"
        self.parent.launch("Dial")

