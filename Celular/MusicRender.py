#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Permite manipular la GUI del reproductor de musica'''

from GuiHandler import GuiHandler
import OptionManager
from Track import Track
import random

class MusicRender(GuiHandler):
    ''' Permite manipular la GUI del reproductor de musica'''
    
    def set_track(self, track):
        self.track = track
    
    def refresh_gui(self):

        GuiHandler.refresh_gui(self)
        
        # Fondo fantoche
        for i in range(16):
            for j in range(14):
                red = random.uniform(.6, 1) 
                green = random.uniform(.6, 1) 
                blue = random.uniform(.6, 1) 
                self.cr.set_source_rgba(red, green, blue, .2)
                self.cr.rectangle(self.scale * i * 8,
                                  self.top_margin + self.scale * j * 8,
                                  self.scale * 8, self.scale * 8)
                self.cr.fill()
        
        # Renderizado de los atributos del track en reproduccion
        if self.track:
            self.cr.set_source_rgb(0, 0, 0)
            
            self.cr.set_font_size(36)
            text = self.truncate_text(self.track.get_artist(), self.width - 10)
            bounds = self.cr.text_extents(text)
            self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 150)
            self.cr.text_path(text)
            
            self.cr.set_font_size(28)
            text = self.truncate_text(self.track.get_track_name(), self.width - 10)
            bounds = self.cr.text_extents(text)
            self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 200)
            self.cr.text_path(text)
            
            self.cr.set_font_size(24)
            text = self.truncate_text(self.track.get_album(), self.width - 10)
            bounds = self.cr.text_extents(text)
            self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 230)
            self.cr.text_path(text)
            
            self.cr.fill()
             
        
        self.surface.write_to_png(self.get_output())
    
    
    def __init__(self):
        ''' Constructor'''
        
        GuiHandler.__init__(self)
        self.title = self.truncate_text("Reprod. de Musica", self.width)
        self.func1 = "Previous"
        self.func2 = "Play/Pause"
        self.func3 = "Next"
        self.selected_index = 0
        self.track = None
        self.refresh_gui()

