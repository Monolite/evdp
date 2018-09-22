from pandac.PandaModules import *
from direct.task import Task
from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
import sys

class EventDispatcher(DirectObject.DirectObject):
    def __init__ (self, device, title):
        self.actions = {}
        self.parent = device
        self.obj_name = ''

        base.setBackgroundColor(0.1, 0.2, 0.4)

        self.title = OnscreenText(text = title,
                              style = 1, fg = (0, 0, 0, 1),
                              pos = (0.8, -0.95), scale = .07)

        self.accept('escape', sys.exit)
        self.accept('mouse_enter', self.mouse_in)
        self.accept('mouse_leave', self.mouse_out)
        self.accept('mouse1', self.click)

        # crea un objeto capaz de detectar colisiones dentro del modelo
        traverser = CollisionTraverser('trav')
        base.cTrav = traverser

        # objeto que el mouse controla para provocar colisiones con otros objetos del modelo        
        self.ray = CollisionRay()

        obj_picker = CollisionNode('mouseRay')
        obj_picker.setIntoCollideMask(BitMask32.bit(0))
        obj_picker.setFromCollideMask(BitMask32.bit(0))
        obj_picker.addSolid(self.ray)

        obj_picker_parent = camera.attachNewNode(obj_picker)

        # menejador de las colisiones detectadas para el mouse
        mouse_events = CollisionHandlerEvent()
        mouse_events.addInPattern('mouse_enter')
        mouse_events.addAgainPattern('mouse_enter')
        mouse_events.addOutPattern('mouse_leave')

        # liga el manejador de colisiones con el objeto que las detecta
        traverser.addCollider(obj_picker_parent, mouse_events)

        # mustra el rayo sobre el objeto colisionado
        #traverser.showCollisions(render)

        taskMgr.add(self.update, 'Update')

    def mouse_in(self, entry):
        self.obj_name = entry.getIntoNodePath().getParent().getName()

    def mouse_out(self, entry):
        self.obj_name = ''

    def update(self, task):
        if base.mouseWatcherNode.hasMouse():
            mpos = base.mouseWatcherNode.getMouse()
            self.ray.setFromLens(base.camNode, mpos.getX(), mpos.getY())

        return Task.cont

    def click(self):
        if self.obj_name in self.actions:
            event = self.actions[self.obj_name]
            event()

    def add_action(self, name, event):
        base = self.parent.get_base()

        obj = self.parent.model.find("**/" + name)
        obj.setCollideMask(BitMask32.bit(0))

        self.actions[name] = event

    def clear(self):
        base = self.parent.get_base()
        for name in self.actions.keys():
            obj = self.parent.model.find("**/" + name)
            obj.setCollideMask(BitMask32(0))

        self.actions = {}

