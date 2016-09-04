# -*- coding: utf-8 -*-
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import sys
from GestorMusica import GestorMusica
import time


class musica (DirectObject.DirectObject):
    
    
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

        if len(self.ListaCanciones) > 0:
            
            self.Sound = loader.loadSfx(self.ListaCanciones[self.indice].get_file())
        else:
            self.status = "No Sound Founded"
            print "No se encontraron archivos de audio"

    def play(self):

        if self.status == "stop":
            self.Sound = loader.loadSfx(self.ListaCanciones[self.indice].get_file())
            self.Sound.setVolume(self.vol)
            self.Sound.setTime(self.musicTime)
            self.status = "playing"

        elif self.status== "playing":
            self.musicTime=self.Sound.getTime()
            self.Sound.stop()
            self.status= "pause" 

        elif self.status== "pause":
            self.Sound.setTime(self.musicTime)
            self.status= "playing"

         
    def volume_up(self):

        vol_status=self.Sound.getVolume()

        if vol_status<1:
            vol_status+=0.05
            self.Sound.setVolume(vol_status)
            print self.Sound.getVolume()


    def volume_down(self):

        vol_status=self.Sound.getVolume()
        if vol_status >= 0:
            vol_status -= 0.05
            self.Sound.setVolume(vol_status)
            print self.Sound.getVolume()


    def siguiente(self):
        try:
            self.status = "stop"
            self.musicTime = 0
            self.indice = self.indice + 1
            if self.indice > len(self.ListaCanciones)-1:
                    self.indice = 0
            self.vol = self.Sound.getVolume()
            if self.Sound.status() == 2:
                self.Sound.stop()
            time.sleep(1.0)
            self.play()
           
        except Exception:
            print "Error: " + str(Exception)
            pass

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
        self.play()
        

    def get_status_repro(self):
        return self.status



