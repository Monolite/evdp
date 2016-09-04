#!/usr/bin/env python
# -*- coding: utf-8 -*-
''' Permite manipular la GUI del reproductor de musica'''

from GuiHandler import GuiHandler
import OptionManager
from Track import Track
import random

class MusicRender(GuiHandler):
    ''' Permite manipular la GUI del reproductor de musica'''

    
    def refresh_gui(self,indice):

        self.selected_index = indice    
        
        
        GuiHandler.refresh_gui(self)
        
        # Fondo fantoche
        for i in range(16):
            for j in range(14):
                red = random.uniform(.6, 1) 
                green = random.uniform(.6, 1) 
                blue = random.uniform(.6, 1) 
                self.cr.set_source_rgba(red, green, blue, .2)
                self.cr.move_to(self.scale * i * 8, self.top_margin + self.scale * j * 8)
                self.cr.line_to(self.scale * i * 8, self.top_margin + self.scale * (j + 1) * 8)
                self.cr.line_to(self.scale * (i + 1) * 8, self.top_margin + self.scale * (j + 1) * 8)
                self.cr.line_to(self.scale * (i + 1) * 8, self.top_margin + self.scale * j * 8)
                self.cr.close_path()
                self.cr.fill()
        
        # Renderizado de los atributos del track en reproduccion
        if len(self.playlist)>0:
            if self.playlist[self.selected_index]:
                track = self.playlist[self.selected_index]
                self.cr.set_source_rgb(0, 0, 0)
                
                self.cr.set_font_size(36)
                text = self.truncate_text(track.get_artist(), self.width - 10)
                bounds = self.cr.text_extents(text)
                self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 150)
                self.cr.text_path(text)
                
                self.cr.set_font_size(28)
                text = self.truncate_text(track.get_track_name(), self.width - 10)
                bounds = self.cr.text_extents(text)
                self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 200)
                self.cr.text_path(text)
                
                self.cr.set_font_size(24)
                text = self.truncate_text(track.get_album(), self.width - 10)
                bounds = self.cr.text_extents(text)
                self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), 230)
                self.cr.text_path(text)
                
                self.cr.fill()
            
        else:
            print "No hay archivos de audio"    
        
        self.surface.write_to_png(OptionManager.get_texture_filename())
    
    
    def __init__(self, playlist):
        ''' Constructor'''
        
        GuiHandler.__init__(self)
        
        self.title = self.truncate_text("Reprod. de Musica", self.width)
        self.selected_index = 0
        self.playlist = playlist
        self.refresh_gui(0)

