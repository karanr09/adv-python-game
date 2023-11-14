from kivy.app import App
from screens.menu_screen import MenuScreen
from screens.game_screen import GameScreen
from screens.score_screen import ScoreScreen

class MemoryTileApp(App):
    def build(self):
        # This can be changed to load a different screen as the starting screen.
        return MenuScreen()

if __name__ == '__main__':
    MemoryTileApp().run()
