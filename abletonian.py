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

    def __init__(self, ntracks):
        self.clips = [None]*ntracks
        self.callbacks = []

    def addMasterClip(self, filename):
        self.master = Clip(filename)
        self.trig = self.master.player['trig']
        self.clips[0] = self.master

    def addClip(self, filename, trackIndex):
        clip = Clip(filename)
        #clip.followMaster(self.master)
        self.clips[trackIndex] = clip

    def go(self):
        for c in self.clips:
            if c:
                c.play()
                self.callbacks.append(pyo.TrigFunc(self.trig, c.play))

    def stop(self):
        self.callbacks = []
            

class Abletonian():

    def __init__(self, ntracks, nscenes):
        self.ntracks = ntracks
        self.nscenes = nscenes
        self.scenes=[Scene(ntracks) for i in range(nscenes)]
        self.current = None

    def sceneGo(self, sceneIndex):
        self.nextScene = self.scenes[sceneIndex]
        if self.current:
            self.current.stop()
            self.switchCallback = pyo.TrigFunc(self.current.master.player['trig'],self.switch)
        else:
            self.switch()

    def switch(self):
        self.nextScene.go()
        self.current = self.nextScene
        self.nextScene = None

    def sceneStop(self, sceneIndex):
        self.scenes[sceneIndex].stop()
        self.current = None

    def addScene(self, scene, sceneIndex):
        self.scenes[sceneIndex] = scene

    def addNewScene(self):
        self.scenes.append(Scene(self.ntracks))

