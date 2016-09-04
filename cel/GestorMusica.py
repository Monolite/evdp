#!/usr/bin/env python
''' Clase que permite obtener y gestionar los archivos de musica'''

import os
import mimetypes
from Track import Track

class GestorMusica:
    ''' Clase que permite obtener una serie de tracks dentro del directorio
        especificado, asi como subdirectorios.'''
    
    basedir = "data/music"
    
    def __create_track_list(self, directorio):
        ''' Crea una lista de instancias Track que se encuentren dentro de
            la carpeta especificada
            param directorio El directorio que se examinara.'''
        lista = os.listdir(directorio)
        for arch in lista:
            path = directorio + "/" + arch
            if os.path.isdir(path):
                self.__create_track_list(directorio + "/" + arch)
            else:
                filetype = mimetypes.guess_type(path)
                if filetype[0] and "audio" in mimetypes.guess_type(path)[0]:
                    self.lista.append(Track(path))

    def get_tracks(self):
        ''' Obtiene una lista de instancias Track.
            return Una lista de Tracks'''
        return self.lista
		
    def get_tracks_by_artist(self, artist):
        ''' Obtiene una lista de instancias Track de un artista determinado
            param artist El artista de los tracks que se desean obtener
            return Una lista de Tracks'''
        lista = []
        
        for track in self.lista:
            if track.get_artist() == artist:
                lista.append(track)
        
        return lista
    
    def get_tracks_by_album(self, album):
        ''' Obtiene una lista de Tracks que pertenezcan al album especificado.
            param album El album que se desea obtener.
            return Una lista de instancias Track.'''
        
        lista = []
        
        for track in self.lista:
            if track.get_album() == album:
                lista.append(track)

        return lista
    
    def get_artistas(self):
        ''' Obtiene una lista de artistas de los distintos Tracks.
            return Una lista de Artistas.'''
    
        artistas = []
        
        for track in self.lista:
            art = track.get_artist()
            if not art in artistas:
                artistas.append(art)

        artistas.sort()
        return artistas
    
    def get_albums(self):
        ''' Obtiene una lista de albums de los distintos Tracks.
            return Una lista de Albums.'''
        albums = []
        
        for track in self.lista:
            alb = track.get_album()
            if not alb in albums:
                albums.append(alb)
        
        albums.sort()
        return albums
	
    def __init__(self):
        ''' Constructor de GestorMusica.'''
        
        self.lista  = []
        self.__create_track_list(GestorMusica.basedir)
		
if __name__ == "__main__":
    GM = GestorMusica()
    
    ARTS = GM.get_albums()
	
    for ART in ARTS:
        print ART + ": "
        
        LISTA = GM.get_tracks_by_album(ART)
        for TRACK in LISTA:
            print ">>> " + TRACK.get_track_name()
            print "$ " + TRACK.get_file()
#!/usr/bin/env python
