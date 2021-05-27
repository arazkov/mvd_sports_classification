from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
import json

Window.size = (480, 853)

data = {
    'stat': None,
    'sex': None,
    'age': None,
    'exersize': None,
    'rezult': None
    }


class Container(BoxLayout):
    def calculate_balls(self, exersize, rezult):
        with open('sport_data.json','r') as js:
            balls = json.load(js)
        ind = balls['body'][0].index(exersize)
        for i in balls['body']:
            if i[ind] == rezult:
                return i[0]


    def qw(self, param):
        data.update(param)
        if all([data['stat'], data['sex'], data['age'], data['exersize'], data['rezult']]):
            self.rez.text = f"Вы набрали\n [color=ff3333]       {self.calculate_balls(data['exersize'], data['rezult'])}\n[/color] [color=3333ff][/color]    баллов"

class MvdSportApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MvdSportApp().run()
