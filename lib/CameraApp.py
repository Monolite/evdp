from panda3d.vision import WebcamVideo
from panda3d.core import MovieTexture, Texture, CardMaker, Point2
from direct.showbase.ShowBase import ShowBase
from direct.showbase import DirectObject
import array
import cairo
import math
from GuiHandler import GuiHandler
import Util

def get_transformation_matrix(width_a, height_a, width_b, height_b):

    scale_x = float(width_a) / width_b
    scale_y = float(height_a) / height_b
    translate_x = (width_a - width_b * scale_y) / 2.0
    translate_y = (height_a - height_b * scale_x) /2.0
    
    if(scale_y < scale_x):
        translate_y = (height_a - height_b * scale_y) / 2.0
        return cairo.Matrix(scale_y, 0, 0, scale_y, translate_x, translate_y)
    
    translate_x = (width_a - width_b * scale_x) / 2.0
    return cairo.Matrix(scale_x, 0, 0, scale_x, translate_x, translate_y)

class CameraApp(GuiHandler):
    __ImageDir = "data/images"
    
    def __init__(self, device):
        GuiHandler.__init__(self)
        self.func3 = "Si"
        self.func2 = ""
        self.func1 = "No"
        self.title = "Guardar?"
        self.parent = device
        self.video_mode = False
        
        option = WebcamVideo.get_option(0)
        self.texture = MovieTexture(option)
        self.texture.setKeepRamImage(True)
    	#self.texture = OpenCVTexture()
    	#self.texture.fromCamera()
    	scale = self.texture.getTexScale()
    	print scale
    	#self.texture = OpenCVTexture()
    	self.card = CardMaker('webcam')
    	self.card.setFrame(-scale[0], scale[0], -scale[1], scale[1])
    	self.card.setUvRange(Point2(scale[0], 0), Point2(0, scale[1]))
    	
        self.card = render.attachNewNode(self.card.generate())
        
        screen = self.parent.get_screen()    
        self.card.reparentTo(screen.getParent())
        self.card.setTransform(screen.getTransform())
    	
        self.card.setSx(0.49)
        self.card.setSz(0.394)
        self.card.setHpr(0, 270, 0)
        self.card.setPos(0.004, 0.335, 0.1)
        self.card.hide()

    def activate(self, events):
        self.toggle_view(True)
        events.add_action("boton_izq1", self.quit)
        events.add_action("centro", self.shoot)
        events.add_action("boton_der", self.shoot)
        events.add_action("boton_izq", self.cancel)

    def shoot(self):
        if self.video_mode:
            max = self.texture.getXSize() * self.texture.getYSize()
            data = array.array('B')
            data.fromstring(self.texture.getRamImageAs("BGR1").getData())

            img = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_ARGB32,
                       self.texture.getXSize(), self.texture.getYSize(),
                       self.texture.getXSize() * 4)

            self.cam_shot = cairo.ImageSurface(cairo.FORMAT_ARGB32,
                                               self.texture.getVideoWidth(),
                                               self.texture.getVideoHeight())

            ctx = cairo.Context(self.cam_shot)
            ctx.set_source_surface(img, 0 , 0)
            ctx.paint() 
            
            self.paint_background()
            self.cr.set_source_surface(self.draw_viewer(self.cam_shot), 30,
                                       self.top_margin + 5)
            self.cr.paint()
            self.paint_foreground()
            self.surface.write_to_png(self.get_output())
            self.parent.repaint()
            self.toggle_view(False)
        else:
            print "Saving..."
            pic_path = CameraApp.__ImageDir + "/p" + Util.generate_id() + ".png"
            print pic_path
            self.cam_shot.write_to_png(pic_path)
            self.toggle_view(True)

    def paint_scene(self):
        drawer_width = self.width - 60
        drawer_height = 2 * self.height / 3
        
        surface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.width, self.height)
        context = cairo.Context(surface)
        
        scale_x = float(self.width) / float(self.cam_shot.get_width())
        scale_y = float(self.height) / float(self.cam_shot.get_height())
        
        
        context.scale(scale_x, scale_y)
        
        context.set_source_surface(self.cam_shot, 0, 0)
        context.paint()
        
        return surface
        
    def cancel(self):
        self.cam_shot = None
        self.toggle_view(True)
        
    def draw_viewer(self, image_surface):
        drawer_width = self.width - 60
        drawer_height = 2 * self.height / 3
    
        surface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, drawer_width, drawer_height)
        context = cairo.Context(surface)
        
        context.rectangle(0, 0, drawer_width, drawer_height)
        context.set_source_rgba(.05, .05, .05, .8)
        context.fill()
        
        context.rectangle(1, 1, drawer_width - 2, drawer_height - 2)
        context.clip()
        context.new_path()
        
        context.transform(get_transformation_matrix(drawer_width, drawer_height, image_surface.get_width(), image_surface.get_height()))
        
        context.set_source_surface(image_surface, 0, 0)
        context.paint()

        return surface
    
    def paint_background(self):
        # Fondo
        gradient = cairo.LinearGradient(0, 0, 0, self.height)
        
        gradient.add_color_stop_rgb(0, 0, 0, 0)
        gradient.add_color_stop_rgb(1, .4, .4, .4)
        
        self.cr.set_source(gradient)
        self.cr.move_to(0, 0)
        self.cr.line_to(self.width, 0)
        self.cr.line_to(self.width, self.height)
        self.cr.line_to(0, self.height)
        self.cr.close_path()
        self.cr.fill()
    
    def quit(self):
        self.toggle_view(False)
        self.parent.launch("menu")

    def toggle_view(self, video):
        self.video_mode = video
        if video:
            #self.texture.fromCamera()
            self.card.setTexture(self.texture)
            print (self.texture.getVideoWidth(), self.texture.getVideoHeight())
            self.card.show()
            self.parent.get_screen().hide()
        else:
            #self.texture = OpenCVTexture()
            self.card.setTexture(self.texture)
            self.card.hide()
            self.parent.get_screen().show()

