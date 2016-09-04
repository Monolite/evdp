# -*- coding: utf-8 -*-
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import sys
from GestorMusica import GestorMusica
from direct.task import Task
import time


class Audio(DirectObject.DirectObject):
    def __init__(self):
        self.music_time= 0           # es el instante de una cancion en segundos
        self.status = "stop"      # el estado inicial del reproductor
        self.indice=0
        self.vol = 0.5
        self.track_path = None
        self.sound = None
        
    def load_track(self, track_path):
        self.track_path = track_path
        
    def get_status(self):
        return self.status

    def play_pause(self):
        if self.status == "stop":        
            self.sound = loader.loadSfx(self.track_path)
            self.sound.setVolume(self.vol)
            self.sound.setTime(self.music_time)
            self.status = "playing"

        elif self.status == "playing":
            self.music_time = self.sound.getTime()
            self.sound.stop()
            self.status = "pause" 

        elif self.status == "pause":
            self.sound.setTime(self.music_time)
            self.status = "playing"

    def stop(self):
        self.status = "stop"
        if self.sound:
            self.sound.stop()
        self.music_time = 0
        time.sleep(0.25)
         
    def volume_up(self):
        if self.sound.getVolume() < 1:
            self.sound.setVolume(self.sound.getVolume() + 0.05)

    def volume_down(self):
        if self.sound.getVolume() >= 0:
            self.sound.setVolume(self.sound.getVolume() - 0.05)



