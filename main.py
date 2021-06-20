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


def choose_plural(nam):
    var = ['бал', 'бала', 'балов']
    n = nam % 10
    n2 = nam % 100
    if nam in range(21, 100000, 10) and n2 != 11 or nam == 1:
        return var[0]
    elif n in range(2, 5) and nam not in range(5, 21) and n2 not in range(12, 15):
        return var[1]
    else:
        return var[2]


def calculate_balls(sex, exercise, result):
    ind = json_file[sex][0].index(exercise)
    for i in json_file[sex]:
        if i[ind] == result:
            return i[0]


def calculate_balls_needs(balls, age, sex):
    balls_needs = int(json_file['sport_test_normativ'][sex][age][2]) - int(balls)
    return balls_needs


def find_exercise_need(balls_needs, exercise, sex):
    for i in range(1, len(json_file[sex])):
        if json_file[sex][i][0] == str(balls_needs):
            exercise_need = json_file[sex][i][json_file[sex][0].index(exercise)]
            while exercise_need == '\u2013':
                i -= 1
                exercise_need = json_file[sex][i][json_file[sex][0].index(exercise)]
            # print(exercise_need)
            return exercise_need


def shows_the_remaining_exercises(balls_needs):
    if data['exercise'] == 'run_10_10':
        if data['sex'] == 'man':
            push_ups_need = find_exercise_need(balls_needs, 'push_ups', 'man')
            pull_ups_need = find_exercise_need(balls_needs, 'pull_ups', 'man')
            crying_need = find_exercise_need(balls_needs, 'crying', 'man')
            exercise_needs_text = f"[color=#9ACD32]Отжимания:[/color] {push_ups_need}\n" \
                                  f"[color=#9ACD32]Подтягивания:[/color] {pull_ups_need}\n" \
                                  f"[color=#9ACD32]Гиря:[/color] {crying_need}"
        else:
            push_ups_need = find_exercise_need(balls_needs, 'push_ups', 'women')
            press_need = find_exercise_need(balls_needs, 'press', 'women')
            exercise_needs_text = f"[color=#9ACD32]Отжимания:[/color] {push_ups_need}\n" \
                                  f"[color=#9ACD32]Пресс:[/color] {press_need}"
    else:
        if data['sex'] == 'man':
            run_need = find_exercise_need(balls_needs, 'run_10_10', 'man')
        else:
            run_need = find_exercise_need(balls_needs, 'run_10_10', 'women')
        exercise_needs_text = f"[color=#9ACD32]Пробежать 10 по 10 за[/color]: {run_need}"
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
            exercise_ind = json_file[data['sex']][0].index(data['exercise'])
            self.ti.values = [i[exercise_ind] for i in json_file[data['sex']][1:] if i[exercise_ind] != '\u2013']

    def view_result(self):
        try:
            balls_rez = calculate_balls(data['sex'], data['exercise'], data['result'])
            balls_needs_rez = calculate_balls_needs(balls_rez, data['age'], data['sex'])
            if balls_needs_rez <= 0:
                balls_norm = json_file['sport_test_normativ'][data['sex']][data['age']][2]
                self.rez.text = f'[color=#32CD32]ПОЗДРАВЛЯЕМ!\n[/color]' \
                                f'Вы набрали\n' \
                                f'[color=ff3333]{balls_rez}[/color]\n' \
                                f'{choose_plural(int(balls_rez))}'
                self.rez_2.text = f'Вам необходимо набрать\n' \
                                  f'[color=ff3333]{balls_norm}[/color]\n' \
                                  f'{choose_plural(int(balls_norm))}'
            else:
                self.rez.text = f"Вы набрали\n" \
                                f"[color=ff3333]{balls_rez}[/color]\n" \
                                f"{choose_plural(int(balls_rez))}"
                self.rez_2.text = f"Вым еще необходимо:\n" \
                                  f"[color=ff3333] {balls_needs_rez} [/color] {choose_plural(int(balls_needs_rez))}\n" \
                                  f"[color=3333ff] Упражнения:[/color] \n" \
                                  f"{shows_the_remaining_exercises(balls_needs_rez)}"
        except (ValueError, TypeError, KeyError):
            self.rez.text = '[color=ff3333]ВВЕДИТЕ КОРЕКТНЫЕ ДАННЫЕ![/color]'
            self.rez_2.text = ''

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
