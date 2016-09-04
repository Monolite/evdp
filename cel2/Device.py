from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import OptionManager
from MusicApp import MusicApp
from EventDispatcher import EventDispatcher
from MainMenu import MainMenu
from PhotoApp import PhotoApp
from CameraApp import CameraApp

class Device:
    def __init__(self):
        self.model = loader.loadModel('device.egg')
        self.model.reparentTo(render)

        self.base = self.model.find("**/base")
        
        self.base.setHpr(0, 90, 0)
        
        self.screen = self.base.find("**/pantalla")
        print self.screen.getPos()
        print self.screen.getHpr()        
        self.apps = {}
        self.events = EventDispatcher(self, "Sony Ericsson W200")
        
        self.apps["menu"] = MainMenu(self)
        self.apps["Album Fotografico"] = PhotoApp(self)
        #self.apps["Camara"] = CameraApp(self)
        self.apps["Reproductor de Audio"] = MusicApp(self)

        self.launch("menu")
        
    def run(self):
        #print "I'm in a race and I'm winning"
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
            self.apps[app_name].activate(self.events)
            self.repaint()
        else:
            print "unknown command: " + app_name



device = Device()
#print base.camera.getPos()
base.disableMouse()
base.camera.setPos(0,-10,0)


mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()
device.run()


