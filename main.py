from kivy.uix.boxlayout import BoxLayout
from kivy.app import App
from kivy.core.window import Window

Window.size = (480, 853)

#def qw():
        #stat = ''
        #sex = ''
        #age = ''
        #exersize = ''
        #rezult = f"{stat}\n{sex}\n{age}\n{exersize}"
        #return rezults
data = {}

class Container(BoxLayout):


    def qw(self, param):
        #self.stat = ''
        #self.sex = ''
        #self.age = ''
        #self.exersize = ''
        #self.rezult = f"{self.stat}\n{self.sex}\n{self.age}\n{self.exersize}"
        data.update(param)
        self.rez.text = f"{data['stat'] if data['stat'] else ''}\n{data['sex'] if 'sex' in data else ''}"
        #return self.rezult
        #pass

class MvdSportApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MvdSportApp().run()
