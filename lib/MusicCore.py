
class MusicCore:

    def Play(self, file):
        print "play"

    def Stop(self):
        print "Stop"

    def Seek(self,time):
        print "Seek"

    def Forward(self):        
        print "Forward"
        self.Seek(self.TimeElapsed()+5)
    
    def Backward(self):
        print "Backward"
        self.Seek(self.TimeElapsed()-5)

    def TimeElapsed(self):
        print "Tiempo Transcurrido"

    def Length(self):
        return 0
        print "Regresa el tiempo total de la cancion"
