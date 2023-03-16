from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MainMenu(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        #self.orientation = "vertical"

        self.add_widget(Button(text="Start game", on_release=self.start_game))
        self.add_widget(Button(text="Options", on_release=self.show_options))
        self.add_widget(Button(text="Quit", on_release=self.quit))

    def start_game(self, instance):
        # Code to start the game goes here
        pass

    def show_options(self, instance):
        # Code to show the options menu goes here
        pass

    def quit(self, instance):
        # Code to quit the game goes here
        pass

class MainMenuApp(App):
    def build(self):
        return MainMenu()

if __name__ == "__main__":
    MainMenuApp().run()
