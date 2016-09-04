from MainMenuRenderer import MainMenuRenderer
import OptionManager

class MainMenu():
    def __init__(self, device):
        self.parent = device
        self.menu_items = {}
        self.selected_index = 0
        self.renderer = MainMenuRenderer(self)

    def activate(self, events):
        self.renderer.refresh(self)
        events.add_action("aro_centro4", self.move_left)
        events.add_action("aro_centro2", self.move_right)
        events.add_action("aro_centro1", self.move_up)
        events.add_action("aro_centro3", self.move_down)
        events.add_action("centro", self.execute)
        events.add_action("boton_izq1", self.quit)
        
    def quit(self):
        self.parent.launch("init")

    def refresh(self):
        self.renderer.refresh(self)
        self.parent.repaint()

    def move_left(self):
        self.selected_index = (self.selected_index - 1) % len(self.menu_items)
        self.refresh()

    def move_right(self):
        self.selected_index = (self.selected_index + 1) % len(self.menu_items)
        self.refresh()

    def move_up(self):
        self.selected_index = (self.selected_index - 3) % len(self.menu_items)
        self.refresh()

    def move_down(self):
        self.selected_index = (self.selected_index + 3) % len(self.menu_items)
        self.refresh()

    def execute(self):
        self.parent.launch(self.menu_items[self.selected_index]["Opcion"]["name"])

