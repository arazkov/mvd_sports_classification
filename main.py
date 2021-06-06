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

with open('exercises_balls.json', 'r') as js:
    json_file = json.load(js)


def calculate_balls(sex, exercise, result):
    ind = json_file[sex][0].index(exercise)
    for i in json_file[sex]:
        if i[ind] == result:
            return i[0]


def calculate_balls_needs(balls, age, sex):
    balls_needs = int(json_file['sport_test_normativ'][sex][age][2]) - int(balls)
    return balls_needs


def shows_the_remaining_exercises(balls_needs):
    if balls_needs <= 0:
        exercise_needs_text = 'ПОЗДРАВЛЯЕМ!'
    elif data['exercise'] == 'run_10_10':
        if data['sex'] == 'man':
            for i in json_file['man']:
                if i[0] == str(balls_needs):
                    exercise_needs_text = f"Отжимания {i[2]}\n Подтягиваня {i[1]}\n Гиря {i[3]}"
        else:
            for i in json_file['women']:
                if i[0] == str(balls_needs):
                    exercise_needs_text = f"Отжимания {i[1]}\n Пресс {i[2]}"
    else:
        if data['sex'] == 'man':
            for i in json_file['man']:
                if i[0] == str(balls_needs):
                    exercise_needs_text = f"Пробежать 10 по 10 за {i[4]}"
        else:
            for i in json_file['women']:
                if i[0] == str(balls_needs):
                    exercise_needs_text = f"Пробежать 10 по 10 за {i[3]}"
    return exercise_needs_text


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
        if data['sex'] and data['exercise']:
            try:
                exercise_ind = json_file[data['sex']][0].index(data['exercise'])
                self.ti.values = [i[exercise_ind] for i in json_file[data['sex']][1:] if i[exercise_ind] != '\u2013']
            except ValueError:
                self.rez.text = 'ВВЕДИТЕ КОРЕКТНЫЕ ДАННЫЕ!'

    def view_result(self):
        try:
            balls_rez = calculate_balls(data['sex'], data['exercise'], data['result'])
            balls_needs_rez = calculate_balls_needs(balls_rez, data['age'], data['sex'])
            self.rez.text = f"Вы набрали\n [color=ff3333]       {balls_rez}\n[/color] [color=3333ff][/color]    баллов"
            self.rez_2.text = f"Вым еще необходимо:\n         [color=ff3333] {balls_needs_rez} [/color] баллов\n{shows_the_remaining_exercises(balls_needs_rez)}"
        except:
            self.rez.text = 'ВВЕДИТЕ КОРЕКТНЫЕ ДАННЫЕ!'


    def qw(self, param):
        data.update(param)
        print(data)
        self.select_params_to_view()
        if all([data['stat'], data['sex'], data['age'], data['exercise'], data['result']]):
            self.view_result()


class MvdSportApp(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MvdSportApp().run()
