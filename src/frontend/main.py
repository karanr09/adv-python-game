from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle, RoundedRectangle, Line
from kivy.uix.popup import Popup
from kivy.uix.textinput import TextInput
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock

font1_path = r'C:\Users\Admin\Documents\Karan Uni\5th semester\Python\Project_KR\Arcade1.TTF'
font2_path = r'C:\Users\Admin\Documents\Karan Uni\5th semester\Python\Project_KR\Arcade2.TTF'

# Define the main menu screen
class MainMenuScreen(Screen):
    def __init__(self, **kwargs):
        super(MainMenuScreen, self).__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=10)

# SPACING
        layout.add_widget(Widget(size_hint_y=0.3))  

 # MEMORY GAME TITLE
        game_name = Label(text='MEMORY GAME', 
                          size_hint_y=0.01,
                          font_name=font1_path,
                          font_size=65)
        game_name.color = (0, 0, 0, 1)
        layout.add_widget(game_name)

# SPACING
        layout.add_widget(Widget(size_hint_y=0.03)) 

# Progress Bar
        progress_bar = ProgressBar(
            max=100, 
            size_hint=(1, 0.1),
            pos_hint={'center_x': 0.5},
        )
        layout.add_widget(progress_bar)

# SPACING
        layout.add_widget(Widget(size_hint_y=0.2)) 

# INFO BUTTON
        button_info = Button(
            text='Info',
            size_hint=(0.7, 0.3),
            background_color=((0.7, 0.7, 0.7, 1)),  # color for Info button
            color=(0, 0, 0, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_name=font1_path,
            font_size=40,
            on_press=self.show_info
        )
        layout.add_widget(button_info)
        

#ADDS A BORDER TO THE BUTTON
        with button_info.canvas.before:
            Color(0., 0., 0., 1)  # Set the background color
            setattr(button_info, 'border_line', Line(width=10))

        button_info.bind(pos=lambda instance, value: self.update_rect(instance), size=lambda instance, value: self.update_rect(instance))
        button_info.background_normal = ''  # Set normal background to an empty string
        button_info.background_down = ''

# SPACING
        #layout.add_widget(Widget(size_hint_y=0.01))

# HIGHSCORE DISPLAY
        player_scores = [
                {'name': 'Player1', 'score': 1000},
                {'name': 'Player2', 'score': 800},
                {'name': 'Player3', 'score': 600},
                ]

        highscores_label = Label(
            text='[b][u]HIGHSCORES[/u][/b]\n' + '\n'.join([f"{i + 1}. {player['name']} - {player['score']}" for i, player in enumerate(player_scores)]),
            font_size=25,
            color=(0, 0, 0, 1),
            markup=True,  # Enable markup to interpret '[b]' and '[u]'
            font_name=font2_path,
        )
        layout.add_widget(highscores_label)

# SPACE ADDER BETWEEN HIGHSCORE AND NAME 
        #layout.add_widget(Widget(size_hint_y=0.01))

# PLAYER NAME
        player_name_input = TextInput(
            hint_text='Enter player name',
            #hint_text_color = (0.7, 0.7, 0.7, 1),
            multiline=False,
            font_size=20,
            font_name=font2_path,
            size_hint=(0.9, 0.15),
            background_color=(0.7, 0.7, 0.7, 1),
            foreground_color=(0, 0, 0, 1), #font color
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            halign='center',
            
        )
        layout.add_widget(player_name_input)

# SPACE ADDER BETWEEN NAME AND PLAY 
        layout.add_widget(Widget(size_hint_y=0.2))

# PLAY BUTTON
        button_play = Button(
            text='Start game',
            size_hint=(0.7, 0.3),
            background_color=((0.7, 0.7, 0.7, 1)),  # Green color for Play button
            color=(0, 0, 0, 1),
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            font_name=font1_path,
            font_size=40,
        )

        #ADDS A BORDER TO THE BUTON
        with button_play.canvas.before:
            Color(0, 0, 0, 1)  # Set the background color
            setattr(button_play, 'border_line', Line(width=10))

        button_play.bind(pos=lambda instance, value: self.update_rect(instance), size=lambda instance, value: self.update_rect(instance))
        button_play.background_normal = ''  # Set normal background to an empty string
        button_play.background_down = ''

        button_play.bind(on_press=self.start_race)  # Bind to the start_race method
        layout.add_widget(button_play)


# SPACE ADDER AT BOTTOM 
        layout.add_widget(Widget(size_hint_y=0.5))

# ADDING LAYOUT TO SCREEN
        self.add_widget(layout)

    def show_info(self, instance):
        # Create the content for the pop-up
        content = BoxLayout(orientation='vertical', spacing=10, padding=10)

        # Add a Label with the desired text
        info_label = Label(
            text='Blablabla', 
            font_size=16,
            font_name = font1_path,
            color=(1, 1, 1, 1))
        content.add_widget(info_label)

        # Create the pop-up
        popup = Popup(
            title='Game Information',
            title_align = 'center',
            title_color = (1,1,1,1),
            title_font =font2_path,
            title_size = 25,
            separator_color = (1,1,1,1),
            content=content,
            size_hint=(None, None),
            size=(400, 300),
            auto_dismiss=True
        )

        with popup.canvas.before:
            Color(1, 1, 1)  # Set the background color of the popup
            border_width = 2  # Set the width of the border
            Line(rectangle=(popup.x, popup.y, popup.width, popup.height), width=border_width)

        popup.open()
    
    #RACE START

    def start_race(self, instance):
        self.manager.current = 'game'
    

    def update_rect(self, instance):
        # Update the Line coordinates based on the Button's position and size
        instance.border_line.rectangle = (
            instance.x,
            instance.y,
            instance.width,
            instance.height,
        )




# Define the game screen
class GameScreen(Screen):
    def __init__(self, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.layout = BoxLayout(orientation='vertical')  # Main layout for this screen

        cols = 3 #Chanege depending on difficulty
        
        # Add a GridLayout for the game grid with spacing to create lines
        self.grid = GridLayout(cols=cols, spacing=2, size_hint=(1, 0.8)) #modify the number of cols depending on the difficulty
        with self.grid.canvas.before:
            Color(1, 1, 1, 1)  # Set the background to white for grid lines
            self.bg = Rectangle(size=(self.grid.width - self.grid.spacing[0] * 2,
                                      self.grid.height - self.grid.spacing[1] * 2),
                                pos=self.grid.pos)

        # Create a Cols x Cols grid of buttons
        for i in range(cols*cols):
            tile = Button(background_color=(0, 0, 0, 1))  # Black squares
            tile.bind(on_press=self.check_tile)
            self.grid.add_widget(tile)
        self.layout.add_widget(self.grid)



# Main Menu Button
        button_layout = BoxLayout(orientation='horizontal', size_hint=(1, 0.2))
        back_button = Button(
            text='Main Menu',
            size_hint=(0.5, 1),
            font_name=font2_path,
            font_size = 30,
            )
        back_button.bind(on_press=self.go_back)

        button_layout.add_widget(back_button)


        labels_layout = BoxLayout(orientation='vertical', size_hint=(0.5, 1))

# Points Display
        self.player_points = 0 # Initialize player points
        self.points_label = Label(
            text=f'Points: {self.player_points}',
            size_hint=(1, 0.5),
            color = (0,0,0,1),
            font_name=font2_path,
        )
        labels_layout.add_widget(self.points_label)

# Lives Display and count
        self.player_lives = 3  # Initialize player lives
        self.lives_label = Label(
            text=f'Lives: {self.player_lives}',
            size_hint=(1, 0.5),
            color = (0,0,0,1),
            font_name=font2_path,
            )
        labels_layout.add_widget(self.lives_label)


# Add the labels layout to the button layout and the button layout to the main layout
        button_layout.add_widget(labels_layout)
        self.layout.add_widget(button_layout)
        self.add_widget(self.layout)
        

        self.correct_tile_indices = [0,3]

    def check_tile(self, instance):
        # Placeholder for the logic to check if the clicked tile is correct
        is_correct = (self.grid.children.index(instance) in self.correct_tile_indices)

        if is_correct:
            instance.background_color = (0, 1, 0, 1)  # Green for correct
            self.player_points += 1
            self.points_label.text = f'Points: {self.player_points}'
        else:
            instance.background_color = (1, 0, 0, 1)  # Red for incorrect
            self.player_lives -= 1
            self.lives_label.text = f'Lives: {self.player_lives}'

            #We can set the if lives == 0: then bla bla

            Clock.schedule_once(lambda dt: self.reset_tile_color(instance), 1)

    def reset_tile_color(self, instance):
        instance.background_color = (0, 0, 0, 1)

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
        Window.clearcolor = (1,1,1,1) #makes the background white
        return sm

   

if __name__ == '__main__':
    MemoryGameApp().run()

