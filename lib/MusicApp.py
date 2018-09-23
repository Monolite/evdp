from Audio import Audio
from MusicRender import MusicRender

class MusicApp:
    def __init__(self, device):
        self.track_list = None
        self.menu_items = {}
        self.player = Audio()
        self.renderer = MusicRender()
        self.parent = device
        self.index = 0
        
    def set_track_list(self, track_list):
        self.index = 0
        if track_list and len(track_list) > 0:
            self.stop()
            self.track_list = track_list
        else:
            self.track_list = None
        
    def activate(self, event):
        if self.track_list and len(self.track_list) > 0:
            self.refresh()
            event.add_action("centro",self.play)
            event.add_action("aro_centro2",self.next_track)
            event.add_action("aro_centro4",self.previous_track)        
            event.add_action("aro_centro1",self.vol_up)
            event.add_action("aro_centro3",self.vol_down)
            event.add_action("boton_izq1",self.quit)
        else:
            print "No hay musica cargada"
            self.quit()

    def refresh(self):
        self.renderer.set_track(self.track_list[self.index])
        self.renderer.refresh_gui()
        self.parent.repaint()

    def play(self):
        self.player.load_track(self.track_list[self.index].get_file())
        self.refresh()
        self.player.play_pause()

    def quit(self):
        self.parent.launch("menu")

    def stop(self):
        self.player.stop()

    def Seek(self,time):
        print "Seek"

    def next_track(self):
        temp = self.player.get_status()
        self.player.stop()
        self.index = (len(self.track_list) + self.index + 1) % len(self.track_list)
        if temp == "playing":
            self.play()
        self.refresh()

    def previous_track(self):
        temp = self.player.get_status()
        self.player.stop()
        self.index = (len(self.track_list) + self.index - 1) % len(self.track_list)
        if temp == "playing":
            self.play()
        self.refresh()
        

    def get_time_elapsed(self):
        self.player.get_time_elapsed()

    def vol_up(self):
        self.player.volume_up()

    def vol_down(self):
        self.player.volume_down()


