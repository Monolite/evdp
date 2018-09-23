#!/usr/bin/env python

from ListRenderer import ListRenderer

class ListApp:
    
    def get_selected_option(self):
        return self.selected_item
        
    def set_options(self, options):
        self.options = options
        self.selected_index = 0
        self.selected_item = None
        self.refresh()

    def select_next(self):
        ''' Selecciona siguiente opcion'''
        
        if self.selected_index < len(self.options) - 1:
            self.selected_index += 1
            if self.selector_pos + self.offset < len(self.options): 
                if self.selector_pos < (self.list_size - 1):
                    self.selector_pos += 1
                else:
                    self.offset += 1
        self.refresh()
        
    def select_previous(self):
        ''' Selecciona opcion anterior'''
        
        if self.selected_index > 0:
            self.selected_index -= 1
            if self.selector_pos + self.offset > 0: 
                if self.selector_pos > 1:
                    self.selector_pos -= 1
                else:
                    if self.offset > 0:
                        self.offset -= 1
        self.refresh()
        
    def activate(self, events):
        self.refresh()
        events.add_action("aro_centro1", self.select_previous)
        events.add_action("aro_centro3", self.select_next)
        events.add_action("boton_izq1", self.quit)
        events.add_action("centro", self.execute)
        
    def execute(self):
        item = self.options[self.selected_index]
        if 'instance' in str(type(item)):
            self.selected_item = ("Dial Contact", "Dial Contact", item.get_info())
        else:
            self.selected_item = self.options[self.selected_index]
        self.parent.launch(self.selected_item[1])
        
    def quit(self):
        self.parent.launch("menu")
        
    def refresh(self):
        aux_list = None
        
        if self.options:
            if len(self.options) > self.list_size:
                aux_list = self.options[self.offset : self.offset + self.list_size]
            else:
                aux_list = self.options
                
            self.renderer.set_list(aux_list, self.options[self.selected_index])
            self.renderer.refresh_gui()
            self.parent.repaint()
        
    def __init__(self, device, config):
        ''' Constructor'''
        
        self.parent = device
        self.selected_item = None
        self.offset = 0
        self.selector_pos = 0
        self.selected_index = 0
        self.list_size = 6
        self.renderer = ListRenderer(config)
