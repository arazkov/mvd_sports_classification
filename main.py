from kivy.uix.accordion import Accordion, AccordionItem
from kivy.app import App
from kivy.core.window import Window

Window.size = (480, 853)

class Container(Accordion):
    pass

class MvdSportApp(App):
    def build(self):
        return Container()

if __name__ == '__main__':
    MvdSportApp().run()
