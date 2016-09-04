from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject

import OptionManager

from GestorMusica import GestorMusica
from GestorContactos import GestorContactos
from GestorRegistros import GestorRegistros

from MusicApp import MusicApp
from EventDispatcher import EventDispatcher
from MainMenu import MainMenu
#from PhotoApp import PhotoApp
#from CameraApp import CameraApp
from ListApp import ListApp
from DialApp import DialApp
from InitApp import InitApp

class Device:
    def __init__(self):
        self.model = loader.loadModel('device.egg')
        self.model.reparentTo(render)
        
        self.base = self.model.find("**/base")
        
        self.base.setHpr(0, 90, 0)
        
        base.disableMouse()
        base.camera.setPos(0, -10, 0)
        mat = Mat4(camera.getMat())
        mat.invertInPlace()
        base.mouseInterfaceNode.setMat(mat)
        base.enableMouse()
        self.screen = self.base.find("**/pantalla")
        
        self.list_app = ListApp(self)
        self.music_app = MusicApp(self)
        self.dial_app = DialApp(self)
        
        self.apps = {}
        self.events = EventDispatcher(self, "Sony Ericsson W200")
        
        self.apps["init"] = InitApp(self)
        self.apps["Dial"] = self.display_dial_screen
        self.apps["menu"] = MainMenu(self)
        self.apps["Reproductor"] = self.play
        
        self.apps["Reproductor de Audio"] = self.display_list
        #self.apps["Camara"] = CameraApp(self)
        #self.apps["Album Fotografico"] = PhotoApp(self)
        self.apps["Llamadas"] = self.display_list
        self.apps["Contactos"] = self.display_list
        self.apps["Mensajes"] = self.display_list
        self.apps["Juegos"] = self.display_list
        self.apps["Utileria"] = self.display_list
        
        self.apps["Reproducir Todas"] = self.play
        self.apps["Lista de Albums"] = self.list_albums
        self.apps["Lista de Artistas"] = self.list_artists
        
        self.apps["Lista de Contactos"] = self.list_contacts
        self.apps["Dial Contact"] = self.dial_contact
        
        self.apps["Llamadas Perdidas"] = self.list_lost_calls
        self.apps["Llamadas Contestadas"] = self.list_answered_calls
        self.apps["Llamadas Marcadas"] = self.list_done_calls
        
        self.launch("init")
    
    def list_lost_calls(self, arg = None):
        manager = GestorRegistros()
        self.list_app.set_options(manager.get_logs_by_state("PERDIDA"))
        return self.list_app
        
    def list_answered_calls(self, arg = None):
        manager = GestorRegistros()
        self.list_app.set_options(manager.get_logs_by_state("RECIBIDA"))
        return self.list_app
        
    def list_done_calls(self, arg = None):
        manager = GestorRegistros()
        self.list_app.set_options(manager.get_logs_by_state("REALIZADA"))
        return self.list_app
    
    def dial_contact(self, arg = None):
        cntct = self.list_app.get_selected_option()[2]
        self.dial_app.write_number(cntct[1])
        return self.dial_app
    
    def list_contacts(self, arg = None):
        manager = GestorContactos()
        self.list_app.set_options(manager.get_contactos())
        return self.list_app
    
    def display_dial_screen(self, arg = None):
        self.dial_app.write_number(self.apps["init"].get_number())
        return self.dial_app
    
    
    def display_list(self, option):
        temp_list = OptionManager.get_option_subtree(option)
        self.list_app.set_options(temp_list)
        return self.list_app
        
    def list_albums(self, arg = None):
        manager = GestorMusica()
        temp_list = manager.get_albums()
        self.list_app.set_options(temp_list)
        return self.list_app
        
    def list_artists(self, arg = None):
        manager = GestorMusica()
        temp_list = manager.get_artists()
        self.list_app.set_options(temp_list)
        return self.list_app
        
    def play(self, arg = None):
        args = self.list_app.get_selected_option()
        print "args:" + str(args)
        if args:
            print args
            manager = GestorMusica()
            temp_list = None
            if args[2] == "all":
                temp_list = manager.get_tracks()
            if args[2] == "artist":
                temp_list = manager.get_tracks_by_artist(args[0])
            if args[2] == "album":
                temp_list = manager.get_tracks_by_album(args[0])
            
            if temp_list:
                self.music_app.set_track_list(temp_list)
                print "Music loading succesfull"
                return self.music_app
        return None
        
    def run(self):
        run()

    def get_model(self):
        return self.model

    def get_base(self):
        return self.base
        
    def get_screen(self):
        return self.screen
        
    def repaint(self):
        self.screen.getTexture().reload()

    def launch(self, app_name):
        if app_name in self.apps:
            self.events.clear()
            self.screen.setTexture(loader.loadTexture(
                                   OptionManager.get_texture_filename()), 1)
            
            if "instancemethod" in str(type(self.apps[app_name])):
                app = self.apps[app_name](app_name)
                if app:
                    app.renderer.set_title(app_name)
                    app.activate(self.events)
            else:
                print "Launching " + app_name
                self.apps[app_name].activate(self.events)
            self.repaint()
        else:
            print "unknown command: " + app_name

device = Device()
device.run()
