from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App
from kivy.core.window import Window

Window.size = (480, 853)

class Container(Accordion):
    pass

class MvdSportApp(App):
    def build(self):
        #my_title = ["Статус", "Пол", "Возраст", "Упражнения", "Результат"]
        #root = Accordion(orientation='vertical')

        #for x in my_title:
            #item = AccordionItem(title=x)
            #if my_title.index(x) == 0:
                #item.add_widget(btn1)
                #root.add_widget(item)
            #elif my_title.index(x) == 1:
                #item.add_widget(Label(text='Very big content\n' * 10))
                #root.add_widget(item)
            #elif my_title.index(x) == 2:
                #item.add_widget(Label(text='Very big content\n' * 10))
                #root.add_widget(item)
            #elif my_title.index(x) == 3:
                #item.add_widget(Label(text='Very big content\n' * 10))
                #root.add_widget(item)
            #else:
                #item.add_widget(Label(text='Very big content\n' * 10))
                #root.add_widget(item)
        #return root
        return Container()

if __name__ == '__main__':
    MvdSportApp().run()
