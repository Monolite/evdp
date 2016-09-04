# -*- coding: utf-8 -*-
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import sys
from GestorMusica import GestorMusica
from direct.task import Task
import time


class Audio(DirectObject.DirectObject):
    def __init__(self):
        self.musicTime= 0           # es el instante de una cancion en segundos
        self.status = "stop"      # el estado inicial del reproductor
        self.indice=0
        self.vol = 0.5
        self.ListaCanciones = []

        self.cargarMusica()

    def cargarMusica(self):
        
        GM = GestorMusica()
        self.ListaCanciones = GM.get_tracks()

        if len(self.ListaCanciones) > 0:        #significa que al menos se encontró un archivo de audio en los directorios
            self.accept('escape',sys.exit)
            self.Sound = loader.loadSfx(self.ListaCanciones[self.indice].get_file())
            taskMgr.add(self.checking,'musica')
        else:
            self.status = "No Sound Founded"
            print "No se encontraron archivos de audio"

    def play_pause(self):

        if self.status == "stop":
            self.Sound = loader.loadSfx(self.ListaCanciones[self.indice].get_file())
            self.Sound.setVolume(self.vol)
            self.Sound.setTime(self.musicTime)
            self.status = "playing"

        elif self.status == "playing":
            self.musicTime = self.Sound.getTime()
            self.Sound.stop()
            self.status = "pause" 

        elif self.status == "pause":
            self.Sound.setTime(self.musicTime)
            self.status = "playing"

    def stop(self):
        if self.status == "playing":
            self.status = "stop"
            self.Sound.stop()
         
    def volume_up(self):
        if self.Sound.getVolume() < 1:
            self.Sound.setVolume(self.Sound.getVolume() + 0.05)

    def volume_down(self):
        if self.Sound.getVolume() >= 0:
            self.Sound.setVolume(self.Sound.getVolume() - 0.05)

    def siguiente(self):
        self.status = "stop"
        self.musicTime = 0
        self.indice = self.indice + 1
        if self.indice > len(self.ListaCanciones)-1:
            self.indice = 0
        self.vol = self.Sound.getVolume()
        if self.Sound.status() == 2:
            self.Sound.stop()
        time.sleep(1.0)
        self.play_pause()

    def atras(self):
        self.status = "stop"
        self.musicTime = 0
        self.indice = self.indice -1
        if self.indice < 0 :
            self.indice = len(self.ListaCanciones) - 1
        self.vol = self.Sound.getVolume()
        if self.Sound.status() == 2:
            self.Sound.stop()
        time.sleep(1.0)
        self.play_pause()

    def get_status_repro(self):
        return self.status

    def get_time_elapsed(self):
        return self.Sound.getTime()

    def checking(self,task):
    #checa si termina una canción
    #para continuar con la siguiente
    #de la lista
        if self.Sound.status() == 1 and self.status == "playing":       #el canal está en silencio y el status está en tocando por lo que debe
            self.siguiente()                                            #reproducirse la siguiente canción
        return Task.cont      
      
    def get_current_index_song(self):
        return self.indice
    

#music=musica()
#run()


