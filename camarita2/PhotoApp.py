from GuiHandler import GuiHandler
import cairo
import math
import os
import mimetypes

def get_image_files(directorio):

    image_list = []
    lista = os.listdir(directorio)
    
    for arch in lista:
        path = directorio + "/" + arch
        if os.path.isdir(path):
            get_image_files(directorio + "/" + arch)
        else:
            filetype = mimetypes.guess_type(path)
            if filetype[0] and "png" in filetype[0]:
                image_list.append(path)

    return image_list
    
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

class PhotoApp(GuiHandler):    
    __ImageDir = "data/images"

    def __init__(self, device):        
        GuiHandler.__init__(self)

        self.set_title("Album")
        self.set_function_2_name("")
        self.set_function_3_name("")

        self.parent = device
        
        self.selected_index = 0
        self.offset = 0
        self.thumb_height = 120
        self.thumb_width = 160
        
        self.hpadding = (self.width - self.thumb_width * 2)/3
        self.vpadding = ((self.height - self.top_margin * 2)  - self.thumb_height * 2)/3
        
        self.thumb_viewer = True
        
    def activate(self, events):
        self.image_list = get_image_files(PhotoApp.__ImageDir)
        self.image_list.sort()
        self.refresh_gui()
        events.add_action("boton_izq", self.move_left)
        events.add_action("boton_der", self.move_right)
        events.add_action("boton_arriba", self.move_up)
        events.add_action("boton_abajo", self.move_down)
        events.add_action("boton_centro", self.change_mode)
        events.add_action("boton_galeria", self.quit)

    def refresh(self):
        self.refresh_gui()
        self.parent.repaint()

    def move_left(self):
        self.selected_index = (len(self.image_list) + self.selected_index - 1) % len(self.image_list)
        self.offset = self.selected_index / 4
        self.refresh()

    def move_right(self):
        self.selected_index = (len(self.image_list) + self.selected_index + 1) % len(self.image_list)
        self.offset = self.selected_index / 4
        self.refresh()

    def move_up(self):
        if self.thumb_viewer:
            self.selected_index = (len(self.image_list) + self.selected_index - 2) % len(self.image_list)
            self.offset = self.selected_index / 4
            self.refresh()

    def move_down(self):
        if self.thumb_viewer:
            self.selected_index = (len(self.image_list) + self.selected_index + 2) % len(self.image_list)
            self.offset = self.selected_index / 4
            self.refresh()
        else:
            os.remove(self.image_list[self.selected_index])
            self.image_list = get_image_files(PhotoApp.__ImageDir)
            self.image_list.sort()
            if len(self.image_list) == self.selected_index :
                self.selected_index = 0
            self.refresh()
            

    def change_mode(self):
        self.thumb_viewer = not self.thumb_viewer
        self.refresh()

    def quit(self):
        self.parent.launch("Fotografia")

    def refresh_gui(self):
    
        if self.thumb_viewer:
            self.set_function_1_name("")
        else:
            self.set_function_1_name("Galery")
                
        GuiHandler.refresh_gui(self)
        
        text = "Image " + str(self.selected_index + 1) + " of " + str(len(self.image_list))
        self.cr.set_font_size(18) 
        bounds = self.cr.text_extents(text)
        self.cr.move_to(self.width/2.0 - (bounds[2]/2.0), self.height - 45)
        self.cr.text_path(text)
        self.cr.set_source_rgb(1, 1, 1)
        
        self.cr.fill()
        
        if self.thumb_viewer:
            aux_list = self.image_list[self.offset * 4: 4 * self.offset + 4]
            k = 0
            for j in range(2):
                for i in range(2):
                    if k < len(aux_list):
                        self.cr.set_source_surface(self.draw_image_thumbnail(aux_list[k]), 
                                                   self.hpadding * (i + 1) + self.thumb_width * i, 
                                                   self.top_margin + self.vpadding * (j + 1) + self.thumb_height * j)
                        self.cr.paint()
                        k += 1
        
        else:
            self.cr.set_source_surface(self.draw_image(self.image_list[self.selected_index]), 30 , self.top_margin + 5)
            self.cr.paint()
                    

        self.surface.write_to_png(self.get_output())
        
    def draw_image(self, image_path):
    
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
        
        image = cairo.ImageSurface.create_from_png(image_path)

        context.transform(get_transformation_matrix(drawer_width, drawer_height, image.get_width(), image.get_height()))
        
        context.set_source_surface(image, 0, 0)
        context.paint()

        return surface
    
    def draw_image_thumbnail(self, image_path):
        
        surface  = cairo.ImageSurface (cairo.FORMAT_ARGB32, self.thumb_width, self.thumb_height)
        context = cairo.Context(surface)
        
        corner = 5
        padding = 3
        
        context.move_to(padding,padding + corner)
        context.arc(corner + padding, corner + padding, corner, math.pi, -.5 * math.pi)
        context.line_to(self.thumb_width - corner - padding, padding)
        context.arc(self.thumb_width - corner - padding, corner + padding, corner, -.5 * math.pi, 0)
        context.line_to(self.thumb_width - padding , self.thumb_height - corner - padding)
        context.arc(self.thumb_width - corner - padding, self.thumb_height - corner - padding, corner, 0, .5 * math.pi)
        context.line_to(corner + padding, self.thumb_height - padding)
        context.arc(corner + padding, self.thumb_height - corner - padding, corner, .5 * math.pi, math.pi)
        context.line_to(padding, self.thumb_height - corner - padding)
        context.close_path()
        
        if self.image_list[self.selected_index] == image_path:
            context.set_source_rgba(.8, .21, .21, .2)
            context.fill_preserve()
            context.set_source_rgba(.8, .2, .2, .6)
            context.set_line_width(3)
            context.stroke()
        else:
            context.set_source_rgb(.05, .05, .05)
            context.fill_preserve()
            context.set_source_rgba(1, 1, 1, .4)
            context.set_line_width(3)
            context.stroke()

        context.rectangle(padding + corner, 
                          padding + corner, self.thumb_width - 2 * (corner + padding), 
                          self.thumb_height - 2 * (corner + padding))
        
        context.clip()
        context.new_path()
        
        image = cairo.ImageSurface.create_from_png(image_path)

        context.transform(get_transformation_matrix(self.thumb_width, self.thumb_height, image.get_width(), image.get_height()))
        
        context.set_source_surface(image, 0, 0)
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

    def delete_this_photo(self):
        pass

