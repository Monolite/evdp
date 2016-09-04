from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject

class CameraApp():
    def __init__(self, device):
        self.parent = device
    	self.texture = OpenCVTexture() 
    	self.texture.fromCamera()
    	
        screen = self.parent.get_screen()        
        min, max = screen.getTightBounds() 
        print min , max
    	s1 = Point3(max - min)
    	print s1
    	scale = self.texture.getTexScale()

    	print "LOG camera resolution", self.texture.getVideoWidth(), self.texture.getVideoHeight()
    	print "LOG camera size", self.texture.getXSize(), self.texture.getYSize()
        print "LOG camera scale: ", scale
        
        print "LOG screen bounds: ", min, max
        print "LOG screen size: ", s1
#        print "LOG screen size: ", screen.getTexture().getXSize(), screen.getTexture().getYSize()

    	self.card = CardMaker('webcam')
    	self.card.setFrame(-scale[0], scale[0], -scale[1], scale[1])
    	self.card.setUvRange(Point2(scale[0], 0), Point2(0, scale[1]))
        self.card = render.attachNewNode(self.card.generate())
        self.card.reparentTo(screen.getParent())
        self.card.setTexture(self.texture)
        self.card.setTwoSided(True)
        
        print "LOG screen Pos: ", screen.getPos()
        print "LOG screen H: ", screen.getH()
        print "LOG screen P: ", screen.getP()
        print "LOG screen R: ", screen.getR()
        print "LOG screen Sx: ", screen.getSx()
        print "LOG screen Sy: ", screen.getSy()
        print "LOG screen Sz: ", screen.getSz()
        print "LOG screen NetTransform: ", screen.getNetTransform()
        print "LOG screen HPR: ", screen.getHpr()
        
        self.card.setTransform(screen.getTransform())
        min, max = self.card.getTightBounds() 
    	s2 = Point3(max - min)
    	
        self.card.setSx(screen.getSx() + (s1[0] - s2[0]))
        self.card.setSz(screen.getSz() + (s1[1] - s2[2])/2)
        self.card.setHpr(0, 90, 180)

        self.card.setX(-1.5)    #posicion izq-der
        self.card.setY(0)       #altura
        self.card.setZ(-1.2)    #profundidad

        self.card.setSz(2.5)
        self.card.setSx(4.5)
        self.card.setSy(2.5)

        print "LOG screen bounds: ", min, max
        print "LOG screen size: ", s2
        print "LOG video Pos: ", self.card.getPos()
        print "LOG video H: ", self.card.getH()
        print "LOG video P: ", self.card.getP()
        print "LOG video R: ", self.card.getR()
        print "LOG video Sx: ", self.card.getSx()
        print "LOG video Sy: ", self.card.getSy()
        print "LOG video Sz: ", self.card.getSz()
        print "LOG video getNetTransform: ", self.card.getNetTransform()
        print "LOG video HPR: ", self.card.getHpr()
        self.card.hide()
        
    def activate(self, events):
        self.card.show()
        #self.parent.get_screen().hide()
        events.add_action("boton_centro", self.quit)

    def quit(self):
        self.card.hide()
        #self.parent.get_screen().show()
        self.parent.launch("menu")

