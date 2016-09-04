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

camara = loader.loadModel('prueba.egg')
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

boton_confi=Base.find("**/boton_confi")
boton_confi.reparentTo(Base)

boton_foto=Base.find("**/boton_foto")
boton_foto.reparentTo(Base)

boton_galeria=Base.find("**/boton_galeria")
boton_galeria.reparentTo(Base)

dispback=Base.find("**/dispback")
dispback.reparentTo(Base)

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
boton_confi.setCollideMask(BitMask32.bit(0))
dispback.setCollideMask(BitMask32.bit(0))
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

    def fun_cam(self):

        if sys.platform == 'win32':
          # manually select the video mode
          if False:
            print str(PandaSystem.getVersionString())
            print "Choose a webcam"
            for o in range(WebcamVideo.getNumOptions()):
              option = WebcamVideo.getOption(o)
              print "Option %d, '%s' at %f fps" % (o, option.getName(), option.getFps())
           
            # ask the user which camera to use
            o = int(raw_input("option>"))
            option = WebcamVideo.getOption(o)
          else:
            # just use the option 0
            option = WebcamVideo.getOption(0)
         
          cursor = option.open()
         
          videoTexture = Texture('movie')
          cursor.setupTexture(videoTexture)
          # calculate the same as openCVTexture has as function
          videoTextureScale = Vec2(option.getSizeX()/float(videoTexture.getXSize()), option.getSizeY()/float(videoTexture.getYSize()))
         
          # under windows the webcam must be updated manually
          def updateVideo(task):
            if cursor.ready():
              cursor.fetchIntoTexture(0, videoTexture, 0)
            return task.cont
          taskMgr.add(updateVideo, 'updateVideo')

        elif sys.platform == 'linux2':
          # fallback in case something goes wrong (openCVTexture doesnt work under windows yet)
          videoTextureScale = (1,1)
         
          # use the tex-coordinates so the video fills the whole card
          videoTexture = OpenCVTexture()
          print "camera open", videoTexture.fromCamera()
          print "camera video resolution", videoTexture.getVideoWidth(), videoTexture.getVideoHeight()
          # get the texture scale
          videoTextureScale = videoTexture.getTexScale()
          if not videoTexture.getVideoWidth() or not videoTexture.getVideoHeight():
            print "invalid camera texture size", videoTexture.getVideoWidth(), videoTexture.getVideoHeight()
            sys.exit()
         
          # save the opencv video into a image
          

        # generate a card to show the texture on
        cardMaker = CardMaker('cardMaker')
        # define the card size

        cardMaker.setFrame(-2.5,2.5,-2.35,2.35)
        
        cardMaker.setUvRange(Point2(videoTextureScale[0],1.9), Point2(0,videoTextureScale[1]))

        # create a card and attach to render
        card = render.attachNewNode(cardMaker.generate())
        card.setTexture(videoTexture)
        card.setTwoSided(True)        card.setPos(-1.4,-2.24,0.3)

        tex = loader.loadTexture('princi.png')
        ts = TextureStage('ts')
        ts.setMode(TextureStage.MDecal)
        #ts.setColor(Vec4(1,0,0,1))
        card.setTexture(ts, tex)


    def toma_foto(self):

        camera = highgui.cvCreateCameraCapture(0)
        def get_image():
            im = highgui.cvQueryFrame(camera)
            return opencv.adaptors.Ipl2PIL(im) 	

        bandera=0

        while bandera<18:
            im = get_image()
            #pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
            #pygame.time.delay(int(10 ))
            bandera=bandera+1

        imagen=get_image()
        pg_img = pygame.image.frombuffer(imagen.tostring(), imagen.size, imagen.mode)
        pygame.image.save(pg_img,"alpha.jpeg")

camarita=Camara()
base.disableMouse()
base.camera.setPos(0,-25,0)
#base.enableMouse()

mat=Mat4(camera.getMat())
mat.invertInPlace()
base.mouseInterfaceNode.setMat(mat)
base.enableMouse()
run()
