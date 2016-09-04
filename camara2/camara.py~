from pandac.PandaModules import *
from direct.task import Task
import direct.directbase.DirectStart
from pandac.PandaModules import WebcamVideo
from pandac.PandaModules import OpenCVTexture
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
from opencv import highgui 
import opencv
import pygame
import Image
from pygame.locals import *
import sys

camara = loader.loadModel('Camara2.egg')
camara.reparentTo(render)

Base=camara.find("**/Base_cam")
Base.reparentTo(render)



pantalla=Base.find("**/pantalla")
pantalla.reparentTo(Base)

boton_abajo=Base.find("**/boton_abajo")
boton_abajo.reparentTo(Base)

boton_arriba=Base.find("**/boton_arriba")
boton_arriba.reparentTo(Base)

boton_centro=Base.find("**/boton_centro")
boton_centro.reparentTo(Base)

boton_der=Base.find("**/boton_der")
boton_der.reparentTo(Base)

boton_izq=Base.find("**/boton_izq")
boton_izq.reparentTo(Base)

boton_encendido=Base.find("**/boton_encendido")
boton_encendido.reparentTo(Base)



boton_foto=Base.find("**/boton_foto")
boton_foto.reparentTo(Base)

boton_galeria=Base.find("**/boton_galeria")
boton_galeria.reparentTo(Base)



zoom_out=Base.find("**/zoom_out")
zoom_out.reparentTo(Base)

zoom_in=Base.find("**/zoom_in")
zoom_in.reparentTo(Base)

#pantalla.setCollideMask(BitMask32.bit(0))
boton_abajo.setCollideMask(BitMask32.bit(0))
boton_arriba.setCollideMask(BitMask32.bit(0))
boton_der.setCollideMask(BitMask32.bit(0))
boton_izq.setCollideMask(BitMask32.bit(0))
boton_centro.setCollideMask(BitMask32.bit(0))
boton_galeria.setCollideMask(BitMask32.bit(0))
boton_foto.setCollideMask(BitMask32.bit(0))
#boton_confi.setCollideMask(BitMask32.bit(0))
#dispback.setCollideMask(BitMask32.bit(0))
boton_encendido.setCollideMask(BitMask32.bit(0))
zoom_in.setCollideMask(BitMask32.bit(0))
zoom_out.setCollideMask(BitMask32.bit(0))


class Camara (DirectObject.DirectObject):
    
    def __init__(self):
        base.setBackgroundColor(0.1,0.2,0.4)
        #base.camera.setPos(0,-35,1)

	self.title = OnscreenText(text="Escaparate Virtual",
                              style=1, fg=(0,0,0,1),
                              pos=(0.8,-0.95), scale = .07)
    	
        
        self.accept('e',self.mouse_enable)
	self.accept('d',self.mouse_disable)
        self.accept('escape',sys.exit)
        self.accept('hola',self.colFun)
        self.accept('out',self.outFun)
        
        self.accept('mouse1',self.click)
        
        
        self.tempBotName = ''
        
        self.collisionCreate()
        taskMgr.add(self.update, 'Update')
   


    def genLabelText(self, text, i):
    	return OnscreenText(text = text, pos = (-1.3, .95-.05*i), fg=(1,1,1,1),
                        align = TextNode.ALeft, scale = .05)  
   
    def mouse_enable(self):
		
	base.enableMouse()
	camara.setPos(0,0,0)

    def mouse_disable(self):
		
	base.disableMouse()
    

    def push1(self):
        
        print Pantalla.getPos()
        

    def click(self):
        if self.tempBotName == 'boton_foto':
          
                self.toma_foto()
                
        if self.tempBotName == 'boton_encendido':
                self.fun_cam()
               
                

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
	#self.tempBotName = entry.getIntoNodePath().getName()
        #print self.tempBotName
    def outFun(self,entry):
        #print entry
        self.tempBotName = ''

    def update(self,task):

        if base.mouseWatcherNode.hasMouse():
            mpos=base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())


        return Task.cont



camarita=Camara()
base.disableMouse()
base.camera.setPos(0,-25,0)
#base.enableMouse()

mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()
run()
