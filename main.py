from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

Window.size = (480, 853)

data = {}

class Container(BoxLayout):
    def qw(self, param):
        data.update(param)
        self.rez.text = f"{data['stat'] if 'stat' in data else ''}\n{data['sex'] if 'sex' in data else ''}\n{data['age'] if 'age' in data else ''}\n{data['exersize'] if 'exersize' in data else ''}\n{data['rezult'] if 'rezult' in data else ''}"

class MvdSportApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MvdSportApp().run()
