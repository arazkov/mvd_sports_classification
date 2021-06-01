from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window
import json

Window.size = (480, 853)

data = {
    'stat': 0,
    'sex': 0,
    'age': 0,
    'exercise': 0,
    'result': 0
}


def calculate_balls(sex, exercise, result):
    if sex == 'male':
        json_file = 'balls_men.json'
    else:
        json_file = 'balls_women.json'
    with open(json_file, 'r') as js:
        balls = json.load(js)
    ind = balls['body'][0].index(exercise)
    for i in balls['body']:
        if i[ind] == result:
            return i[0]


def shows_the_remaining_exercises(balls, stat, sex):
    pass


class Container(BoxLayout):
    def select_params_to_view(self):
        if data['sex'] == 'male':
            self.exer.values = ["Бег", "Отжимания", "Подтягивания", "Гиря"]
            self.age.values = [
                'до 25 лет',
                'от 25 до 30 лет',
                'от 30 до 35 лет',
                'от 35 до 40 лет',
                'от 40 до 45 лет',
                'от 45 до 50 лет',
                'от 50 до 55 лет',
                '55 лет и старше']
        elif data['sex'] == 'female':
            self.exer.values = ["Бег", "Отжимания", "Прес"]
            self.age.values = [
                'до 25 лет',
                'от 25 до 30 лет',
                'от 30 до 35 лет',
                'от 35 до 40 лет',
                'от 40 до 45 лет',
                '45 лет и старше']
        if data['exercise'] == 'run_10_10':
            self.ti.input_filter = 'float'
        else:
            self.ti.input_filter = 'int'

    def view_result(self):
        try:
            self.rez.text = f"Вы набрали\n [color=ff3333]       {calculate_balls(data['sex'], data['exercise'], data['result'])}\n[/color] [color=3333ff][/color]    баллов"
        except ValueError:
            self.rez.text = 'ВВЕДИТЕ КОРЕКТНЫЕ ДАННЫЕ!'
        print(data)

    def qw(self, param):
        data.update(param)
        self.select_params_to_view()
        if all([data['stat'], data['sex'], data['age'], data['exercise'], data['result']]):
            self.view_resulte()


class MvdSportApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MvdSportApp().run()
