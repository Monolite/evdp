from pandac.PandaModules import *
from direct.task import Task
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
import direct.directbase.DirectStart
from musica import musica
import sys

cara = loader.loadModel('Ipod.egg')
cara.reparentTo(render)

cubierta=cara.find("**/Cubierta")
cubierta.reparentTo(render)

clip=cubierta.find("**/Clip")
clip.reparentTo(cubierta)

anterior=cubierta.find("**/Control1")
anterior.reparentTo(cubierta)

mas=cubierta.find("**/Control2")
mas.reparentTo(cubierta)

menos=cubierta.find("**/Control3")
menos.reparentTo(cubierta)

siguiente=cubierta.find("**/Control4")
siguiente.reparentTo(cubierta)

play_pause=cubierta.find("**/play_pause")
play_pause.reparentTo(cubierta)




anterior.setCollideMask(BitMask32.bit(0))
siguiente.setCollideMask(BitMask32.bit(0))
mas.setCollideMask(BitMask32.bit(0))
menos.setCollideMask(BitMask32.bit(0))
play_pause.setCollideMask(BitMask32.bit(0))


class Ipod (DirectObject.DirectObject):
    
    def __init__(self):
        base.setBackgroundColor(0.1,0.2,0.4)
        self.title = OnscreenText(text="Escaparate Virtual",style=1, fg=(0,0,0,1),pos=(0.8,-0.95), scale = .07)
        
        
        self.accept('e',self.mouse_enable)
        self.accept('d',self.mouse_disable)
        self.accept('escape',sys.exit)
        self.accept('hola',self.colFun)
        self.accept('out',self.outFun)
	self.accept('c',self.cambiatex)
	self.accept('mouse1',self.click)
        self.tempBotName = ''
        self.collisionCreate()
        taskMgr.add(self.update, 'Update')
        
        alight = AmbientLight('alight')
        alight.setColor(VBase4(1, 1, 1, 1))
        alnp = render.attachNewNode(alight)
        render.setLight(alnp)

   
        
         

    def cambiatex(self):
	print 'entra a a funcion cambiar textura'
	cubierta.setTexture(loader.loadTexture('./textures/verde.jpg'),1)

    def genLabelText(self, text, i):
    	return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),align = TextNode.ALeft, scale = .05)  
    
    def click(self):
        if self.tempBotName=='Control1':
                pista.atras()
        if self.tempBotName=='Control2':
                pista.volume_up()
        if self.tempBotName=='Control3':
                pista.volume_down()
        if self.tempBotName=='Control4':
                pista.siguiente()
        if self.tempBotName=='play_pause':
                pista.play()
  	
    
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
    def outFun(self,entry):
        #print entry
        self.tempBotName = ''

    def update(self,task):

        if base.mouseWatcherNode.hasMouse():
            mpos=base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())


        return Task.cont


base.disableMouse()
base.camera.setPos(0,-5,0)
mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()

pista=musica()

