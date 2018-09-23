#!/usr/bin/env python
''' Abstraccion de los archivos de audio'''

import taglib

class Track:
    ''' Clase que representa un archivo de Musica.'''
    
    def get_artist(self):
        ''' Obtiene el artista de dicho Track
            return El artista del Track.'''

        return self.artista
    
    def get_file(self):
        ''' Obtiene nombre y ruta del archivo.
            return Ubicacion del track.'''

        return self.archivo
    
    def get_track_name(self):
        ''' Obtiene el Titulo del track.
            return El titulo del Track.'''

        return self.titulo
    
    def get_album(self):
        ''' Obtiene el album del track
            return El album del track'''

        return self.album
    
    def __repr__(self):
        ''' Representacion de los atributos del archivo de audio.
            return La informacion del Track.'''

        return self.get_track_name()
    
    def __init__(self, archivo):
        ''' Constructor de Track
            param archivo La ruta y nombre del archivo de audio.'''
    
        self.archivo = archivo

        arch = taglib.File(archivo)

        if 'ARTIST' in arch.tags:
            if len(arch.tags['ARTIST']) > 0:
                self.artista = arch.tags['ARTIST'][0]
            else:
                self.artista = 'UNKNOWN'
        else:
            self.artista = 'UNKNOWN'

        if 'TITLE' in arch.tags:      
            if len(arch.tags['TITLE']) > 0:
                self.titulo = arch.tags['TITLE'][0]
            else:
                self.titulo = 'UNKNOWN'
        else:
            self.titulo = 'UNKNOWN'

        if 'ALBUM' in arch.tags:
            if len(arch.tags['ALBUM']) > 0:
                self.album = arch.tags['ALBUM'][0]
            else:
                self.album = 'UNKNOWN'
        else:
            self.album = 'UNKNOWN'
        
        
        #arch = tagpy.FileRef(self.archivo)
        #my_tag = arch.tag()
        #self.artista = my_tag.artist
        #self.titulo = my_tag.title
        #self.album = my_tag.album

