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


def calculate_balls(sex, exercise, result):
    if sex == 'male':
        json_faile = 'balls_men.json'
    else:
        json_faile = 'balls_women.json'
    with open(json_faile, 'r') as js:
        balls = json.load(js)
    ind = balls['body'][0].index(exercise)
    for i in balls['body']:
        if i[ind] == result:
            return i[0]


class Container(BoxLayout):
    def qw(self, param):
        data.update(param)
        if data['sex'] == 'male':
            self.exer.values = ["Бег", "Отжимания", "Подтягивания", "Гиря"]
        elif data['sex'] == 'female':
            self.exer.values = ["Бег", "Отжимания", "Прес"]
        if all([data['stat'], data['sex'], data['age'], data['exercise'], data['result']]):
            try:
                if data['exercise'] == 'run_10_10':
                    self.ti.input_filter = 'float'
                else:
                    self.ti.input_filter = 'int'
                self.rez.text = f"Вы набрали\n [color=ff3333]       {calculate_balls(data['sex'], data['exercise'], data['result'])}\n[/color] [color=3333ff][/color]    баллов"
            except:
                self.rez.text = 'ВВЕДИТЕ КОРЕКТНЫЕ ДАННЫЕ!'


class MvdSportApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MvdSportApp().run()
