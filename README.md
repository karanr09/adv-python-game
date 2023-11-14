# adv-python-game
Bocconi Advanced Python Course - Exam Work

Presentation:
The Memory Grid Game project offers an engaging and interactive platform for users to exercise and improve their memory skills in a fun and challenging environment. It serves as a testament to the fusion of classic memory games with modern programming techniques, aiming to provide an enjoyable and stimulating gaming experience.

Supposed Background:
The background presents a grid where buttons change color briefly. The player's task is to recall and click these colored buttons within a set time limit.

Input Data in the Program (Variables Used):
•	self.num: Number of buttons changing color
•	self.cols, self.lines: Grid size - columns and rows
•	self.num_buttons: Total number of buttons in the grid
•	self.sequence: Sequence of colored buttons
•	self.current_sequence: User-selected sequence of buttons
•	self.colors: Colors used (purple, white, red)
•	self.time_limit: Time limit to display colored buttons
•	self.turn: Counter for game turns

Expected Output of the Program:
•	Display a sequence of buttons that briefly change color to purple.
•	Manage user clicks, altering button colors based on correctness (purple for correct, red for incorrect).
•	Adjust game difficulty based on user performance (changing button count, time limit, or grid size).
Typical User of the Program:
The typical user might be someone seeking a memory-based challenge or casual gaming experience. This game appeals to those interested in memory exercises or seeking a straightforward yet engaging game to test memory skills or enjoy a simple gaming experience.



The function of the back end:
1.	Initialization:
•	Set initial parameters.
•	Prepare the game environment.
2.	Start Game:
•	Begin a new game.
•	Call the function 3.
•	Call the function 4 after the function 3 it’s done.
3.	Generate Sequence:
•	Call function 8.
•	Create a grid structure based on columns and rows.
•	Randomly select button indices to create a sequence for the game.
4.	Display Sequence:
•	Show the sequence by changing the color of the selected buttons to purple.
•	Activate a timer to reset the button colors after a set time and wait the setted time.
5.	On Button Click:
•	If a valid game button (not already colored) is clicked:
a)	Add the button's index to the current sequence.
b)	Change the button color based on correctness: purple for correct, red for incorrect.
c)	If it’s red wait a second then stop the game and call 7.
d)	Check if the current sequence length matches the number of buttons in the sequence to win and advance to 6.


6.	Increase Difficulty:
•	Randomly choose an option to increase game difficulty: increase number of buttons, decrease display time, or modify the grid structure.
•	Adjust game parameters based on the random choice.
7.	Display End Game:
•	Present an end game window with choices to restart the game or return to the menu.
8.	Reset Colors:
•	Return all button colors to white after the time limit for sequence display elapses.


