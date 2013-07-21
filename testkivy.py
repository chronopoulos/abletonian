from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.properties import NumericProperty


class Toggle(ToggleButton):
    step = NumericProperty()
    note = NumericProperty()
    def on_press(self):
        print 'Step, Note: ', self.step, self.note
        #abletonian.playScene(0)


class SceneButton(ToggleButton):
    sceneIndex = NumericProperty()
    def on_press(self):
        print 'Scene: ', self.sceneIndex


class KivyApp(App):

    def build(self):
        ntracks = 4
        nclips = 4
        root = FloatLayout()
        grid = GridLayout(rows=nclips, cols=ntracks, size_hint=(0.79,1.0))
        for j in range(nclips):
            for i in range(ntracks):
                grid.add_widget(Toggle(step=i,note=j))
        sidebar = BoxLayout(orientation='vertical', size_hint=(0.19,1.0), pos_hint={'x':0.81, 'y':0.0})
        for j in range(nclips):
            sidebar.add_widget(SceneButton(sceneIndex=j))
        root.add_widget(grid)
        root.add_widget(sidebar)
        return root


if __name__ == '__main__':
    KivyApp().run()
