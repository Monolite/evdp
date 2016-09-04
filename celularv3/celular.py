from pandac.PandaModules import *
from direct.task import Task
import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.showbase import DirectObject
import sys

cara = loader.loadModel('cel_ultimo.egg')
cara.reparentTo(render)
#cara.setPos(10,80,0)

base1=cara.find("**/base")
base1.reparentTo(render)



boton_der=base1.find("**/boton_der")
boton_der.reparentTo(base1)

boton_der1=base1.find("**/boton_der1")
boton_der1.reparentTo(base1)

boton_izq=base1.find("**/boton_izq")
boton_izq.reparentTo(base1)

boton_izq1=base1.find("**/boton_izq1")
boton_izq1.reparentTo(base1)

centro=base1.find("**/centro")
centro.reparentTo(base1)


aro_centro1=base1.find("**/aro_centro1")
aro_centro1.reparentTo(base1)



aro_centro2=base1.find("**/aro_centro2")
aro_centro2.reparentTo(base1)

aro_centro3=base1.find("**/aro_centro3")
aro_centro3.reparentTo(base1)

aro_centro4=base1.find("**/aro_centro4")
aro_centro4.reparentTo(base1)

boton1=base1.find("**/boton1")
boton1.reparentTo(base1)

boton2=base1.find("**/boton2")
boton2.reparentTo(base1)

boton3=base1.find("**/boton3")
boton3.reparentTo(base1)

boton4=base1.find("**/boton4")
boton4.reparentTo(base1)

boton5=base1.find("**/boton5")
boton5.reparentTo(base1)

boton6=base1.find("**/boton6")
boton6.reparentTo(base1)

boton7=base1.find("**/boton7")
boton7.reparentTo(base1)

boton8=base1.find("**/boton8")
boton8.reparentTo(base1)

boton9=base1.find("**/boton9")
boton9.reparentTo(base1)

botona=base1.find("**/botona")
botona.reparentTo(base1)

botonb=base1.find("**/botonb")
botonb.reparentTo(base1)

botonc=base1.find("**/botonc")
botonc.reparentTo(base1)

pantalla=base1.find("**/pantalla")
pantalla.reparentTo(base1)





boton1.setCollideMask(BitMask32.bit(0))
boton2.setCollideMask(BitMask32.bit(0))
boton3.setCollideMask(BitMask32.bit(0))
boton4.setCollideMask(BitMask32.bit(0))
boton5.setCollideMask(BitMask32.bit(0))
boton6.setCollideMask(BitMask32.bit(0))
boton7.setCollideMask(BitMask32.bit(0))
boton8.setCollideMask(BitMask32.bit(0))
boton9.setCollideMask(BitMask32.bit(0))
botona.setCollideMask(BitMask32.bit(0))
botonb.setCollideMask(BitMask32.bit(0))
botonc.setCollideMask(BitMask32.bit(0))
boton_der.setCollideMask(BitMask32.bit(0))
boton_der1.setCollideMask(BitMask32.bit(0))
boton_izq.setCollideMask(BitMask32.bit(0))
boton_izq1.setCollideMask(BitMask32.bit(0))
centro.setCollideMask(BitMask32.bit(0))
aro_centro1.setCollideMask(BitMask32.bit(0))
aro_centro2.setCollideMask(BitMask32.bit(0))
aro_centro3.setCollideMask(BitMask32.bit(0))
aro_centro4.setCollideMask(BitMask32.bit(0))



base1.setPos(0,5,1)
base1.setHpr(0,90,0)

class textura (DirectObject.DirectObject):
    
    def __init__(self):
        base.setBackgroundColor(0.1,0.2,0.4)
        base.camera.setPos(0,-5,1)

	self.title = OnscreenText(text="Escaparate Virtual",
                              style=1, fg=(0,0,0,1),
                              pos=(0.8,-0.95), scale = .07)
    	self.ekyeEventText = self.genLabelText("Mouse ON: E", 0)
    	self.dkeyEventText = self.genLabelText("Mouse OFF: D", 1)
        
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
	base1.setPos(0,0,0)

    def mouse_disable(self):
		
	base.disableMouse()
    

    def push1(self):
        
        print 'Boton1'
        
    
    def push3(self):
        
        print 'Boton3'
        
    def push2(self):
        print 'Boton2'


    def push5(self):
        
        print 'Boton5'
    def push4(self):
        print 'Boton4'
    
    def push6(self):
        
        print 'Boton6'
    
    def push7(self):
        
        print 'Boton7'
    
    def push8(self):
        
        print 'Boton8'
    
    def push9(self):
        
        print 'Boton9'
        
    def pusha(self):
        
        print 'Botona'
        
    def pushb(self):
        
        print 'Botonb'
        
    def pushc(self):
        
        print 'Botonc'
    def pushizq(self):
        print 'Boton izq'
    def pushizq1(self):
        print 'Boton izq1'
    def pushder(self):
        print 'Boton der'
    def pushder1(self):
        print 'Boton der1'
    def pushcentro(self):
        print 'Boton centro'
    def pusharo1(self):
	print 'Aro 1'
    def pusharo2(self):
	print 'Aro 2'
    def pusharo3(self):
	print 'Aro 3'
    def pusharo4(self):
	print 'Aro 4'   

    def click(self):
        if self.tempBotName == 'boton1':
            self.push1()
        if self.tempBotName == 'boton4':
            self.push4()
        if self.tempBotName == 'boton2':
            self.push2()
        if self.tempBotName == 'boton3':
            self.push3()
        if self.tempBotName == 'boton4':
            self.push4()
        if self.tempBotName == 'boton5':
            self.push5()
        if self.tempBotName == 'boton6':
            self.push6()
        if self.tempBotName == 'boton7':
            self.push7()
        if self.tempBotName == 'boton8':
            self.push8()
        if self.tempBotName == 'boton9':
            self.push9()
        if self.tempBotName == 'botona':
            self.pusha()
        if self.tempBotName == 'botonb':
            self.pushb()
        if self.tempBotName == 'botonc':
            self.pushc()
        if self.tempBotName == 'boton_izq':
            self.pushizq()
        if self.tempBotName == 'boton_izq1':
            self.pushizq1()
        if self.tempBotName == 'boton_der':
            self.pushder()
        if self.tempBotName == 'boton_der1':
            self.pushder1()
        if self.tempBotName == 'centro':
            self.pushcentro()
        if self.tempBotName == 'aro_centro1':
            self.pusharo1()
        if self.tempBotName == 'aro_centro2':
            self.pusharo2()
        if self.tempBotName == 'aro_centro3':
            self.pusharo3()
        if self.tempBotName == 'aro_centro4':
            self.pusharo4()
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


        #self.myTraverser.showCollisions(render)


    def colFun(self,entry):
        #print entry
        self.tempBotName = entry.getIntoNodePath().getParent().getName()
        #print self.tempBotName
    def outFun(self,entry):
        #print entry
        self.tempBotName = ''

    def update(self,task):

        if base.mouseWatcherNode.hasMouse():
            mpos=base.mouseWatcherNode.getMouse()
            self.pickerRay.setFromLens(base.camNode, mpos.getX(), mpos.getY())


        return Task.cont

        ## myTraverser.traverse(render)
        ## #assume for simplicity's sake that myHandler is a CollisionHandlerQueue
        ## if myHandler.getNumEntries() > 0:
            ## myHandler.sortEntries() #this is so we get the closest object
            ## pickedObj=myHandler.getEntry(0).getIntoNodePath()
            ## pickedObj=pickedObj.findNetTag('myObjectTag')
            ## if not pickedObj.isEmpty():
                ## handlePickedObject(pickedObj)

tex1=textura()
#base.oobe()
base.disableMouse()
#base.camera.hide()
run()
