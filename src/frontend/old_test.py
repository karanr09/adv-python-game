from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.progressbar import ProgressBar
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle

# Define the main menu screen
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10)

        # Status bar at the top
        layout.add_widget(Widget(size_hint_y=0.05))  # Placeholder for status bar

        # Add a label and a button to the layout
        layout.add_widget(Label(text='RACE', size_hint_y=0.2))
        button = Button(text='Start Race', size_hint_y=0.1)
        button.bind(on_press=self.start_race)
        layout.add_widget(button)

        # Add a progress bar at the bottom
        layout.add_widget(ProgressBar(max=100, value=25, size_hint_y=0.05))
        self.add_widget(layout)

    def start_race(self, instance):
        self.manager.current = 'game'


# Define the game screen
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')  # Main layout for this screen

        # Add a GridLayout for the game grid with spacing to create lines
        self.grid = GridLayout(cols=3, spacing=2, size_hint=(1, 0.8))
        with self.grid.canvas.before:
            Color(1, 1, 1, 1)  # Set the background to white for grid lines
            self.bg = Rectangle(size=(self.grid.width - self.grid.spacing[0] * 2,
                                      self.grid.height - self.grid.spacing[1] * 2),
                                pos=self.grid.pos)

        # Create a 3x3 grid of buttons
        for i in range(9):
            button = Button(background_color=(0, 0, 0, 1))  # Black squares
            button.bind(on_press=self.toggle_color)
            self.grid.add_widget(button)
        self.layout.add_widget(self.grid)

        # Add a back button to return to the main menu
        back_button = Button(text='Back to Main Menu', size_hint=(1, 0.2))
        back_button.bind(on_press=self.go_back)
        self.layout.add_widget(back_button)

        self.add_widget(self.layout)

    def toggle_color(self, instance):
        # Change the background color of the button to grey when pressed
        instance.background_color = (0.5, 0.5, 0.5, 1)

    def go_back(self, instance):
        # self.manager.transition = NoTransition()
        self.manager.current = 'menu'


# Define the screen manager
class MemoryGameApp(App):
    def build(self):
        Window.size = (360, 640)  # Typical phone screen size
        sm = ScreenManager()
        sm.add_widget(MainMenuScreen(name='menu'))
        sm.add_widget(GameScreen(name='game'))
        return sm


if __name__ == '__main__':
    MemoryGameApp().run()