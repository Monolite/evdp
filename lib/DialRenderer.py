#!/usr/bin/env python
''' Documentacion del archivo'''

from GuiHandler import GuiHandler

class DialRenderer(GuiHandler):

    def __init__(self, config):
        GuiHandler.__init__(self, config.dynamic_texture_path)
        self.call_dialog = ""
        self.dialed_number = ""
        self.func3 = "Llamar"
        self.func2 = ""
        self.func1 = "Borrar" 
        self.title = ""
    
    def set_dialog(self, dialog):
        self.call_dialog = dialog
        
    def set_dialed_number(self, number):
        self.dialed_number = number
    
    def refresh_gui(self):
        self.title = ""
        GuiHandler.refresh_gui(self)
        self.cr.set_source_rgb(0, 0, 0)
        
        self.cr.set_font_size(36)
        text = self.truncate_text(self.call_dialog, self.width - 40)
        bounds = self.cr.text_extents(text)
        self.cr.move_to(15, self.top_margin + 30)
        self.cr.text_path(text)
        
        self.cr.set_font_size(28)
        text = self.truncate_text(self.dialed_number, self.width - 10)
        bounds = self.cr.text_extents(text)
        self.cr.move_to(self.width - bounds[2] - 20, 300)
        self.cr.text_path(text)
        
        self.cr.fill()
             
        self.surface.write_to_png(self.get_output())
