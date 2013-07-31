import pyo
from abletonian import Abletonian, Scene, Clip

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty
from kivy.uix.textinput import TextInput

################################

audioServer = pyo.Server()
audioServer.boot()
audioServer.start()

loopdir = '/home/chrono/music/samples/drum loops/'

abletonian = Abletonian(4,4)

abletonian.scenes[0].addMasterClip(loopdir+'120bpm_16b_808beat.wav')
abletonian.scenes[0].addClip(loopdir+'120bpm_16b_808beat.wav', 1)
abletonian.scenes[0].addClip(loopdir+'120bpm_16b_panningfifths.aif', 2)
abletonian.scenes[0].addClip(loopdir+'120bpm_16b_pentatonicbells.wav', 3)


#################################

class GridButton(Button):

    def __init__(self, trackIndex, sceneIndex):
        super(GridButton, self).__init__(text='load')
        self.trackIndex = trackIndex
        self.sceneIndex = sceneIndex
        self.ti = TextInput(text='/home/chrono/music/samples/drum loops/', size_hint=(0.8,0.8), pos_hint={'x':0.1, 'y':0.1}, multiline=False)
        self.ti.bind(on_text_validate=self.on_textInput)
        self.pu = Popup(title='Scene %i, Track %i: Type path to file'%(self.sceneIndex, self.trackIndex), content=self.ti, size_hint=(0.8,0.2), pos_hint={'x':0.1, 'y':0.4})

    def on_press(self):
        if self.state=='down':
            print 'Down: ', self.trackIndex, self.sceneIndex
            self.pu.open()
        else:
            print 'Up: ', self.trackIndex, self.sceneIndex

    def on_textInput(self, textinput):
        if self.trackIndex==0:
            abletonian.scenes[self.sceneIndex].addMasterClip(textinput.text)
        else:
            abletonian.scenes[self.sceneIndex].addClip(textinput.text, self.trackIndex)


class SceneButton(ToggleButton):

    def __init__(self, sceneIndex):
        self.sceneIndex = sceneIndex
        super(SceneButton, self).__init__(text='Scene '+str(self.sceneIndex), group='Scenes')

    def on_press(self):
        if self.state=='down':
            print 'Down: ', self.sceneIndex
            abletonian.sceneGo(self.sceneIndex)
        else:
            print 'Up: ', self.sceneIndex
            abletonian.sceneStop(self.sceneIndex)


class AbletonianApp(App):

    def build(self):
        ntracks = 4
        nclips = 4
        root = FloatLayout()
        grid = GridLayout(rows=nclips, cols=ntracks, size_hint=(0.79,1.0))
        for j in range(nclips):
            for i in range(ntracks):
                grid.add_widget(GridButton(trackIndex=i, sceneIndex=j))
        sidebar = BoxLayout(orientation='vertical', size_hint=(0.19,1.0), pos_hint={'x':0.81, 'y':0.0})
        for j in range(nclips):
            sidebar.add_widget(SceneButton(sceneIndex=j))
        root.add_widget(grid)
        root.add_widget(sidebar)
        return root


if __name__ == '__main__':

    AbletonianApp().run()

