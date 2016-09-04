from Audio import Audio
from GestorMusica import GestorMusica

class MusicApp:
    def __init__(self, device):

        self.ListaDeTracks = []
        self.menu_items = {}
        GM = GestorMusica()
        self.ListaDeTracks = GM.get_tracks()
        self.Player = Audio()
        self.parent = device
        

    def activate(self, event):

        event.add_action("play_pause",self.Play)
        event.add_action("Control4",self.Siguiente)
        event.add_action("Control1",self.Anterior)        
        event.add_action("Control2",self.vol_up)
        event.add_action("Control3",self.vol_down)

    def Play(self):
        indice = self.Player.get_current_index_song()
        self.Player.play_pause()


    def Stop(self):
        indice = self.Player.get_current_index_song()
        self.Player.stop()

    def Siguiente(self):
        indice = self.Player.get_current_index_song()
        self.Player.siguiente()


    def Anterior(self):
        indice = self.Player.get_current_index_song()
        self.Player.atras()


    def TimeElapsed(self):
        self.Player.get_time_elapsed()

    def Length(self):
        return 0

    def vol_up(self):
        self.Player.volume_up()

    def vol_down(self):
        self.Player.volume_down()


