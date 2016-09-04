from Audio import Audio
from MusicRender import MusicRender
from GestorMusica import GestorMusica

class MusicApp:
    def __init__(self, device):

        self.ListaDeTracks = []
        self.menu_items = {}
        GM = GestorMusica()
        self.ListaDeTracks = GM.get_tracks()
        self.Player = Audio()
        self.renderer = MusicRender(self.ListaDeTracks)
        self.parent = device
        

    def activate(self, event):
        self.refresh(self.Player.get_current_index_song())
        event.add_action("centro",self.Play)
        event.add_action("aro_centro2",self.Siguiente)
        event.add_action("aro_centro4",self.Anterior)        
        event.add_action("aro_centro1",self.vol_up)
        event.add_action("aro_centro3",self.vol_down)
        event.add_action("boton_izq1",self.quit)
        #event.add_action("aro_centro3",self.)

    def refresh(self, indice):
        self.renderer.refresh_gui(indice)
        self.parent.repaint()

    def Play(self):
        indice = self.Player.get_current_index_song()
        self.Player.play_pause()
        self.refresh(indice)

    def quit(self):
        self.parent.launch("menu")

    def Stop(self):
        indice = self.Player.get_current_index_song()
        self.Player.stop()
        self.refresh(indice)

    def Seek(self,time):
        print "Seek"

    def Forward(self):        
        print "Forward"
        self.Seek(self.TimeElapsed()+5)
    
    def Backward(self):
        print "Backward"
        self.Seek(self.TimeElapsed()-5)

    def Siguiente(self):
        indice = self.Player.get_current_index_song()
        self.Player.siguiente()
        self.refresh(indice)

    def Anterior(self):
        indice = self.Player.get_current_index_song()
        self.Player.atras()
        self.refresh(indice)

    def TimeElapsed(self):
        self.Player.get_time_elapsed()

    def Length(self):
        return 0

    def vol_up(self):
        self.Player.volume_up()

    def vol_down(self):
        self.Player.volume_down()


