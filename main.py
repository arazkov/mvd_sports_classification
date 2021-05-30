from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
import json

Window.size = (480, 853)

data = {
    'stat': None,
    'sex': None,
    'age': None,
    'exercise': None,
    'result': None
}


def calculate_balls(exercise, result):
    with open('sport_data.json', 'r') as js:
        balls = json.load(js)
    ind = balls['body'][0].index(exercise)
    for i in balls['body']:
        if i[ind] == result:
            return i[0]


class Container(BoxLayout):
    def qw(self, param):
        data.update(param)
        if all([data['stat'], data['sex'], data['age'], data['exercise'], data['result']]):
            self.rez.text = f"Вы набрали\n [color=ff3333]       {calculate_balls(data['exercise'], data['result'])}\n[/color] [color=3333ff][/color]    баллов"


class MvdSportApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MvdSportApp().run()
