from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject
from CameraApp import CameraApp
import OptionManager
from EventDispatcher import EventDispatcher
from PhotoApp import PhotoApp
import datetime


class Device:
    def __init__(self):
        self.model = loader.loadModel('finepixr.egg')
        self.model.reparentTo(render)

        self.base = self.model.find("**/Base_cam")
        self.base.reparentTo(render)
        self.base.setHpr(0, -90, 0)

        base.disableMouse()
        base.camera.setPos(0, -20, 0)        
        mat = Mat4(camera.getMat())
        mat.invertInPlace()
        base.mouseInterfaceNode.setMat(mat)
        base.enableMouse()

        self.screen = self.base.find("**/pantalla")
        self.screen.reparentTo(self.base)
        
        self.apps = {}
        self.events = EventDispatcher(self, "Fujifilm Finepix 470")
        self.apps["Album Fotografico"] = PhotoApp(self)
        self.apps["Fotografia"]= CameraApp(self)
        self.screen.setTexture(loader.loadTexture(OptionManager.get_texture_filename()), 1)

        self.launch("Album Fotografico")

    def run(self):
        print "I'm in a race and I'm winning"
        print datetime.datetime.now()
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
            self.apps[app_name].activate(self.events)
            self.repaint()
        else:
            print "unknown command: " + app_name

device = Device()
device.run()
