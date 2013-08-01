import pyo, sys
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

class ClipButton(Button):

    def __init__(self, trackIndex, sceneIndex):
        super(ClipButton, self).__init__(text='load')
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


class AddSceneButton(Button):

    def __init__(self, size_hint=(1.,1.), pos_hint={'x':0.,'y':0.}):
        super(AddSceneButton, self).__init__(text='Add\nScene', size_hint=size_hint, pos_hint=pos_hint)

    def on_press(self):
        newSceneRow = SceneRow(app.nscenes, app.ntracks)
        abletonian.addNewScene()
        app.scenerows.append(newSceneRow)
        app.grid.add_widget(newSceneRow)
        app.nscenes = len(app.scenerows)
        app.messageBox.text = 'Added New Scene'


class AddTrackButton(Button):

    def __init__(self, size_hint=(1.,1.), pos_hint={'x':0.,'y':0.}):
        super(AddTrackButton, self).__init__(text='Add\nTrack', size_hint=size_hint, pos_hint=pos_hint)

    def on_press(self):
        for scenerow in app.scenerows:
            scenerow.addTrack()
        app.ntracks += 1
        app.messageBox.text = 'Added New Track'

class SceneButton(ToggleButton):

    def __init__(self, sceneIndex, size_hint=(1.,1.), pos_hint={'x':0.,'y':0.}):
        self.sceneIndex = sceneIndex
        super(SceneButton, self).__init__(text='Scene '+str(self.sceneIndex), group='Scenes', size_hint=size_hint, pos_hint=pos_hint)

    def on_press(self):
        if self.state=='down':
            app.messageBox.text='Playing Scene '+str(self.sceneIndex)
            abletonian.sceneGo(self.sceneIndex)
        else:
            print 'Up: ', self.sceneIndex
            abletonian.sceneStop(self.sceneIndex)


class SceneRow(FloatLayout):

    def __init__(self, sceneIndex, ntracks):
        self.sceneIndex = sceneIndex
        self.ntracks = ntracks
        super(SceneRow, self).__init__()
        super(SceneRow, self).add_widget(SceneButton(sceneIndex, size_hint=(0.19,1.0)))
        self.trackBar = BoxLayout(orientation='horizontal', size_hint=(0.79,1.0), pos_hint={'x':0.21,'y':0.})
        for i in range(self.ntracks):
            self.trackBar.add_widget(ClipButton(trackIndex=i, sceneIndex=self.sceneIndex))
        super(SceneRow, self).add_widget(self.trackBar)

    def addTrack(self):
        self.ntracks += 1
        self.trackBar.add_widget(ClipButton(trackIndex=self.ntracks-1, sceneIndex=self.sceneIndex))


class AbletonianApp(App):

    def build(self):

        self.ntracks = 4
        self.nscenes = 4

        ds = 0.02

        gridWidth = 0.9
        gridHeight = 0.8

        self.root = FloatLayout()

        self.main = FloatLayout(size_hint=(1-ds*2,1-ds*2), pos_hint={'x':ds, 'y':ds})

        self.scenerows = []
        for i in range(self.nscenes):
            self.scenerows.append(SceneRow(i, self.ntracks))

        self.grid = BoxLayout(orientation='vertical', size_hint=(gridWidth-ds/2, gridHeight-ds/2), pos_hint = {'x':0.0,'y':1-gridHeight+ds/2})
        for scenerow in self.scenerows:
            self.grid.add_widget(scenerow)

        self.main.add_widget(self.grid)

        self.bottomBar = FloatLayout(size_hint=(gridWidth,1-gridHeight-ds/2), pos_hint={'x':0., 'y':0.})
        self.bottomBar.add_widget(AddSceneButton(size_hint=(0.19,1.)))
        self.messageBox = Label(text='Message Box', size_hint=(0.79,1.), pos_hint={'x':0.21, 'y':0.})
        self.bottomBar.add_widget(self.messageBox)

        self.main.add_widget(self.bottomBar)

        self.main.add_widget(AddTrackButton(size_hint=(1-gridWidth-ds,gridHeight-ds/2), pos_hint={'x':gridWidth+ds, 'y':1-gridHeight+ds/2}))

        self.root.add_widget(self.main)

        return self.root


if __name__ == '__main__':

    app = AbletonianApp()
    app.run()

