from pandac.PandaModules import *
from direct.task import Task
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
import direct.directbase.DirectStart

import sys


z550 = loader.loadModel("Z550.egg")
z550.reparentTo(render)

masca1=z550.find("**/MascarasZ550.005")
masca1.reparentTo(render)

masca2=masca1.find("**/MascarasZ550.003")
masca2.reparentTo(masca1)

masca21=masca2.find("**/Control.002")
masca21.reparentTo(masca2)


masca2.setCollideMask(BitMask32.bit(0))
masca21.setCollideMask(BitMask32.bit(0))

class Celular (DirectObject.DirectObject):
    
    def __init__(self):
        base.setBackgroundColor(0.1,0.2,0.4)
        self.title = OnscreenText(text="Escaparate Virtual",style=1, fg=(0,0,0,1),pos=(0.8,-0.95), scale = .07)
        
        
        self.accept('e',self.mouse_enable)
        self.accept('d',self.mouse_disable)
        self.accept('escape',sys.exit)
        self.accept('hola',self.colFun)
        self.accept('out',self.outFun)
	
	#self.accept('mouse1',self.click)
        self.tempBotName = ''
        self.collisionCreate()
        taskMgr.add(self.update, 'Update')
        
        alight = AmbientLight('alight')
        alight.setColor(VBase4(1, 1, 1, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)

   
        
         

    
    def genLabelText(self, text, i):
    	return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),align = TextNode.ALeft, scale = .05)  
  
  
    
    def mouse_enable(self):
        
        base.enableMouse()
        print cubierta.getPos()
	print base.camera.getPos()
        
             

    def mouse_disable(self):
        base.disableMouse()
        print cubierta.getPos()
	print base.camera.getPos()

    def collisionCreate(self):

        self.myTraverser = CollisionTraverser('trav')
        base.cTrav = self.myTraverser
        
        colHandler = CollisionHandlerEvent()

        ## colHandler.addInPattern('into-%in')
        colHandler.addInPattern('hola')
        colHandler.addAgainPattern('hola')
        colHandler.addOutPattern('out')


        self.pickerNode=CollisionNode('mouseRay')
        self.pickerNP=camera.attachNewNode(self.pickerNode)
        self.pickerNode.setIntoCollideMask(BitMask32.bit(0))
        self.pickerNode.setFromCollideMask(BitMask32.bit(0))
        self.pickerRay=CollisionRay()
        self.pickerNode.addSolid(self.pickerRay)
        self.myTraverser.addCollider(self.pickerNP, colHandler)

        self.pickerNP.show()


        self.myTraverser.showCollisions(render)


    def colFun(self,entry):
        #print entry
        self.tempBotName = entry.getIntoNodePath().getParent().getName()
        print self.tempBotName
    def outFun(self,entry):
        #print entry
        self.tempBotName = ''

    def update(self,task):

        if base.mouseWatcherNode.hasMouse():
            mpos=base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())


        return Task.cont



base.disableMouse()
base.camera.setPos(0,-20,0)
mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()

hola=Celular()

run()
