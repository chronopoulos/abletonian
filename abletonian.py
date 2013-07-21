import pyo

class Clip():
    """
    This may not be necessary
    """

    def __init__(self, filename):
        self.player = pyo.SfPlayer(filename, speed=[1,1])

    def play(self):
        self.player.out()

    def setMaster(self):
        self.callback = pyo.TrigFunc(self.player['trig'], self.play)

    def followMaster(self, master):
        self.callback = pyo.TrigFunc(master.player['trig'], self.play)

class Scene():

    def __init__(self):
        self.clips = []
        self.callbacks = []

    def addMasterClip(self, filename):
        self.master = Clip(filename)
        self.trig = self.master.player['trig']
        self.clips.append(self.master)

    def addClip(self, filename):
        clip = Clip(filename)
        #clip.followMaster(self.master)
        self.clips.append(clip)

    def go(self):
        for c in self.clips:
            c.play()
            self.callbacks.append(pyo.TrigFunc(self.trig, c.play))

    def stop(self):
        self.callbacks = []
            

class Abletonian():

    def __init__(self):
        self.scenes=[]

    def addScene(self, scene):
        self.scenes.append(scene)

    def sceneGo(self, sceneIndex):
        self.scenes[sceneIndex].go()

    def sceneStop(self, sceneIndex):
        self.scenes[sceneIndex].stop()

