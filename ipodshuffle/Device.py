from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import OptionManager
from EventDispatcher import EventDispatcher
from MusicApp import MusicApp

class Device:
    def __init__(self):
        self.model = loader.loadModel('Ipod.egg')
        self.model.reparentTo(render)

        self.base = self.model.find("**/Cubierta")
        self.base.reparentTo(render)
        #self.base.setHpr(0, 0, 0)
        #base.camera.setPos(0, -5, 0)

        self.events = EventDispatcher(self, "Ipod Shuffle")
        alight = AmbientLight('alight')
        alight.setColor(VBase4(1, 1, 1, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)
        self.apps = {}
        self.apps["Reproductor de Audio"] = MusicApp(self)
        self.launch("Reproductor de Audio")

    def run(self):
        print "I'm in a race and I'm winning"
        run()

    def get_model(self):
        return self.model

    def get_base(self):
        return self.base

    def launch(self, app_name):
        if app_name in self.apps:
            self.events.clear()
            self.apps[app_name].activate(self.events) 
        else:
            print "unknown command: " + app_name


base.disableMouse()
base.camera.setPos(0,-7,0)
mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()

device = Device()
device.run()
