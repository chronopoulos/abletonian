import pyo
from abletonian import Abletonian, Scene, Clip

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty

################################

audioServer = pyo.Server()
audioServer.boot()
audioServer.start()

loopdir = '/home/chrono/music/samples/drum loops/'

abletonian = Abletonian()

scene0 = Scene()
scene0.addMasterClip(loopdir+'120bpm_16b_808beat.wav')
scene0.addClip(loopdir+'120bpm_16b_daggadah.wav')
scene0.addClip(loopdir+'120bpm_16b_panningfifths.aif')
scene0.addClip(loopdir+'120bpm_16b_pentatonicbells.wav')
abletonian.addScene(scene0)



#################################

class Toggle(ToggleButton):
    track = NumericProperty()
    scene = NumericProperty()
    def on_press(self):
        if self.state=='down':
            print 'Down: ', self.track, self.scene
        else:
            print 'Up: ', self.track, self.scene

class SceneButton(ToggleButton):
    sceneIndex = NumericProperty()
    def on_press(self):
        if self.state=='down':
            print 'Down: ', self.sceneIndex
            abletonian.sceneGo(self.sceneIndex)
        else:
            print 'Up: ', self.sceneIndex
            abletonian.sceneStop(self.sceneIndex)


class KivyApp(App):

    def build(self):
        ntracks = 4
        nclips = 4
        root = FloatLayout()
        grid = GridLayout(rows=nclips, cols=ntracks, size_hint=(0.79,1.0))
        for j in range(nclips):
            for i in range(ntracks):
                grid.add_widget(Toggle(track=i,scene=j))
        sidebar = BoxLayout(orientation='vertical', size_hint=(0.19,1.0), pos_hint={'x':0.81, 'y':0.0})
        for j in range(nclips):
            sidebar.add_widget(SceneButton(sceneIndex=j))
        root.add_widget(grid)
        root.add_widget(sidebar)
        return root


if __name__ == '__main__':

    KivyApp().run()

