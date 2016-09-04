#!/usr/bin/env python
''' Documentacion del archivo'''

from DialRenderer import DialRenderer
from GestorRegistros import GestorRegistros
from Registro import Registro

class DialApp:
    
    def __init__(self, device):
        self.parent = device
        self.dialog = "Marcando..."
        self.number = ""
        self.renderer = DialRenderer()
        
    def refresh(self):
        self.renderer.set_dialog(self.dialog)
        self.renderer.set_dialed_number(self.number)
        self.renderer.refresh_gui()
        self.parent.repaint()
        
    def activate(self, events):
        self.refresh()
        events.add_action("boton_der", self.toggle)
        events.add_action("boton_izq", self.delete)
        events.add_action("boton_der1", self.delete)
        events.add_action("boton_izq1", self.quit)
        
        events.add_action("boton1", self.write_1)
        events.add_action("boton2", self.write_2)
        events.add_action("boton3", self.write_3)
        events.add_action("boton4", self.write_4)
        events.add_action("boton5", self.write_5)
        events.add_action("boton6", self.write_6)
        events.add_action("boton7", self.write_7)
        events.add_action("boton8", self.write_8)
        events.add_action("boton9", self.write_9)
        events.add_action("botonc", self.write_numb)
        events.add_action("botona", self.write_astrsk)
        events.add_action("botonb", self.write_0)
    
    def toggle(self):
        reg = Registro(self.number, "REALIZADA", None, None)
        manager = GestorRegistros()
        manager.agregar_registro(reg)
        self.dialog = "Llamando..."
        self.refresh()
    
    def quit(self):
        self.parent.launch("init")
    
    def delete(self):
        if len(self.number) > 2:
            self.number = self.number[0 : len(self.number) - 1]
        elif len(self.number) == 1:
            self.number = ""
        self.refresh()
        
    def write_number(self, number):
        self.number = number
        
    def write_1(self):
        self.number += "1"
        self.refresh()
        
    def write_2(self):
        self.number += "2"
        self.refresh()
    
    def write_3(self):
        self.number += "3"
        self.refresh()
    
    def write_4(self):
        self.number += "4"
        self.refresh()
        
    def write_5(self):
        self.number += "5"
        self.refresh()
    
    def write_6(self):
        self.number += "6"
        self.refresh()
    
    def write_7(self):
        self.number += "7"
        self.refresh()
        
    def write_8(self):
        self.number += "8"
        self.refresh()
    
    def write_9(self):
        self.number += "9"
        self.refresh()
        
    def write_0(self):
        self.number += "0"
        self.refresh()
        
    def write_astrsk(self):
        self.number += "*"
        self.refresh()
    
    def write_numb(self):
        self.number += "#"
        self.refresh()

        
