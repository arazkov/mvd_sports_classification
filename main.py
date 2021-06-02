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
    with open('exercises_balls.json', 'r') as js:
        balls = json.load(js)
    ind = balls[sex][0].index(exercise)
    for i in balls[sex]:
        if i[ind] == result:
            return i[0]


def shows_the_remaining_exercises(balls, stat, sex):
    pass


class Container(BoxLayout):
    def select_params_to_view(self):
        exercise_list = ["Бег", "Отжимания", "Подтягивания", "Гиря"]
        age_list = [
                'до 25 лет',
                'от 25 до 30 лет',
                'от 30 до 35 лет',
                'от 35 до 40 лет',
                'от 40 до 45 лет',
                'от 45 до 50 лет',
                'от 50 до 55 лет',
                '55 лет и старше']
        if data['sex'] == 'man':
            self.exer.values = exercise_list
            self.age.values = age_list
        elif data['sex'] == 'women':
            self.exer.values = exercise_list[:2] + ["Прес"]
            self.age.values = age_list[:5] + ['45 лет и старше']
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
            self.view_result()


class MvdSportApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MvdSportApp().run()
