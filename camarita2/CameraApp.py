from pandac.PandaModules import *
import direct.directbase.DirectStart
from direct.showbase import DirectObject
import array
import cairo
import math
from GuiHandler import GuiHandler
import Util
import time

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
    __ZoomStep = 0.03

    def __init__(self, device):
        GuiHandler.__init__(self)
        self.parent = device
        self.video_mode = False
        self.zoom = 0.0
    	self.texture = OpenCVTexture()
    	self.texture.fromCamera()
    	scale = self.texture.getTexScale()

    	self.card = CardMaker('webcam')
    	self.card.setFrame(-scale[0], scale[0], -scale[1], scale[1])
    	self.card.setUvRange(Point2(scale[0], 0), Point2(0, scale[1]))
        self.card = render.attachNewNode(self.card.generate())
        
        screen = self.parent.get_screen()
        self.card.reparentTo(screen.getParent())
        self.card.setTransform(screen.getTransform())
        
        self.card.setHpr(180,0, 180)

        self.card.setX(1.05)    #posicion izq-der
        self.card.setY(0.9)     #profundidad
        self.card.setZ(-0.31)    #altura

        self.card.setSz(1.65)   #altura
        self.card.setSx(3.1)   #
        self.card.setSy(2.5)
        self.card.hide()
        #screen.setTexture(self.texture, 1)
        

    def activate(self, events):
        self.toggle_view(True)
        events.add_action("boton_galeria", self.quit)
        events.add_action("boton_foto", self.shoot)
        events.add_action("boton_centro", self.cancel)
        events.add_action("zoom_in", self.zoom_in)
        events.add_action("zoom_out", self.zoom_out)
    
    def zoom_in(self):
        if self.zoom > CameraApp.__ZoomStep / 2:
            self.card.setTexScale(TextureStage.getDefault(), self.card.getTexScale(TextureStage.getDefault())[0] + CameraApp.__ZoomStep)
            offset = self.card.getTexOffset(TextureStage.getDefault())
            offset[0] = offset[0] - CameraApp.__ZoomStep / 2
            offset[1] = offset[1] - CameraApp.__ZoomStep / 2
            self.card.setTexOffset(TextureStage.getDefault(), offset[0], offset[1])
            self.zoom -= CameraApp.__ZoomStep

    def zoom_out(self):
        self.card.setTexScale(TextureStage.getDefault(), self.card.getTexScale(TextureStage.getDefault())[0] - CameraApp.__ZoomStep)
        offset = self.card.getTexOffset(TextureStage.getDefault())
        offset[0] = offset[0] + CameraApp.__ZoomStep / 2
        offset[1] = offset[1] + CameraApp.__ZoomStep / 2
        self.card.setTexOffset(TextureStage.getDefault(), offset[0], offset[1])
        self.zoom += CameraApp.__ZoomStep

    def shoot(self):
        if self.video_mode:
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
            print "Saving..."
            pic_path = CameraApp.__ImageDir + "/p" + Util.generate_id() + ".png"
            print pic_path
            self.cam_shot.write_to_png(pic_path)
            time.sleep(1)
            self.toggle_view(True)

            self.draw_screen_camera()
            self.parent.repaint()

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
        self.parent.launch("Album Fotografico")

    def toggle_view(self, video):
        self.video_mode = video
        if video:
            self.card.setTexture(self.texture)
            self.card.show()
            #self.parent.get_screen().show()
            self.parent.get_screen().hide()

        else:
            self.card.setTexture(self.texture)
            self.card.hide()
            self.parent.get_screen().show()

    def draw_screen_camera(self):
                # Fondo
        gradient = cairo.LinearGradient(0, 0, 0, self.height)
        
        #gradient.add_color_stop_rgb(0, 0, 0, 0)
        #gradient.add_color_stop_rgb(1, .4, .4, .4)
        
        #self.cr.set_source(gradient)
        self.cr.move_to(0, 0)
        self.cr.line_to(self.width, 0)
        self.cr.line_to(self.width, self.height)
        self.cr.line_to(0, self.height)
        self.cr.close_path()
        self.cr.fill()
    
