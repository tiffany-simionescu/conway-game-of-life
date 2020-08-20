from tkinter import *
from tkinter import font
import time
import webbrowser

# Add Pause functionality - can update during pause
# Update About this Algorithm below grid (talk about the founder, turing-completeness, etc)
# Add rules to the right of the grid - Eventually add to about.html (react app)
# Add Generation of Cells to the top of the grid

### Custom Features ###
# Create 4 presets
# a random cell configuration button
# Add additional cell properties, like color or size, and incorporate them into your visualization

class GameOfLife(Frame):

	def __init__(self, main_frame):

		Frame.__init__(self, main_frame)
		self.main_frame = main_frame
		self.grid(row = 0, column = 0)

		self.horizontal_size = 25
		self.vertical_size = 25
		self.cells = []
		self.generate_next = True
		self.pause = True

		self.init_UI()

	def init_UI(self):	

		self.main_frame.title("Game of Life")

		# frame for title and line of instruction
		self.title_frame = Frame(self.main_frame)
		self.title_frame.grid(row = 0, column = 0, columnspan = 4)

		self.titleFont = font.Font(family="Verdana", size=16)
		self.descriptionFont = font.Font(family="Verdana", size=12)

		title = Label(self.title_frame, text = "Conway's Game of Life", font = self.titleFont)
		title.pack(side = TOP)

		prompt = Label(self.title_frame, text = "Watch the cells come to life! Click the cells to create the starting configuration. Once you're ready, press the Play button!", 
		font = self.descriptionFont)
		prompt.pack(side = BOTTOM)

		# creates grid
		self.build_grid()

		# Game Rules
		self.rule_frame = Frame(self.main_frame)
		self.rule_frame.grid(row = 2, column = 3, columnspan = 4)

		rule_title = Label(self.rule_frame, text = "Rules", font = self.titleFont)
		rule_title.pack()

		rule_step_1 = Label(self.rule_frame, text = "1. This is rule one",
		font = self.descriptionFont)
		rule_step_1.pack()

		rule_step_2 = Label(self.rule_frame, text = "2. This is rule two",
		font = self.descriptionFont)
		rule_step_2.pack()

		rule_step_3 = Label(self.rule_frame, text = "3. This is rule three",
		font = self.descriptionFont)
		rule_step_3.pack()

### About this Algorithm 
		self.algo_frame = Frame(self.main_frame)
		self.algo_frame.grid(row = 4, column = 0, columnspan = 4)

		about_algorithm_title = Label(self.algo_frame, text = "About this Algorithm", font = self.titleFont)
		about_algorithm_title.pack(side = TOP)

		prompt = Label(self.algo_frame, text = "To learn more about this algorithm and how it works, click the About button!", 
		font = self.descriptionFont)
		prompt.pack()

		# About the Algorithm Button
		# Update about.html
		url = "about.html"
		new = 1
		def open_about():
			webbrowser.open(url,new=new)

		Btn = Button(self.algo_frame, text = "About", command = open_about)
		Btn.pack(side = BOTTOM)

		# Top Buttons
		### Reformat buttons
		self.play_button = Button(self.main_frame, text = "Play", command = self.start_game)
		self.play_button.grid(row = 1, column = 1, sticky = W)

		self.pause_button = Button(self.main_frame, text = "Pause", state = DISABLED, command = self.pause_game)
		self.pause_button.grid(row = 1, column = 2, sticky = W)

		self.stop_button = Button(self.main_frame, text = "Stop", state = DISABLED, command = self.stop_game)
		self.stop_button.grid(row =1 , column = 3, sticky = W)

	def build_grid(self):

		# creates new frame for grid of cells in game
		self.game_frame = Frame(
			self.main_frame, width = self.horizontal_size + 3, height = self.vertical_size + 3, borderwidth = 2, relief = SUNKEN)
		self.game_frame.grid(row = 2, column = 0, columnspan = 4)

		#instantiates buttons for choosing initial configuration
		self.cells = [[Button(self.game_frame, bg = "white", width = 2, height = 1) for i in range(self.horizontal_size + 2)] for j in range(self.vertical_size + 2)]
		# creates 2d array of buttons for grid
		for i in range(1, self.vertical_size + 1):
			for j in range(1, self.horizontal_size + 1):	
				self.cells[i][j].grid(row = i, column = j, sticky = W+E)
				self.cells[i][j]['command'] = lambda i=i, j=j:self.cell_toggle(self.cells[i][j])

	def start_game(self):

		self.disable_buttons()
		# creates list of buttons in grid to toggle
		buttons_to_toggle = []
		for i in range(1, self.vertical_size + 1):
			for j in range(1, self.horizontal_size + 1):
				coord = (i, j)
				# if cell dead and has 3 neighbors, add coordinate to list of coords to toggle
				if self.cells[i][j]['bg'] == "white" and self.neighbor_count(i, j) == 3:
					buttons_to_toggle.append(coord)
				# if cell alive and does not have 2 or 3 neighbors,, add coordinate to list of coords to toggle
				elif self.cells[i][j]['bg'] == "black" and self.neighbor_count(i, j) != 3 and self.neighbor_count(i, j) != 2:
					buttons_to_toggle.append(coord)

		# updates (toggles) the cells on the grid
		for coord in buttons_to_toggle:
			self.cell_toggle(self.cells[coord[0]][coord[1]])			

		# if self.generate_next:
		if self.generate_next:
			self.after(100, self.start_game)
		else:
			self.enable_buttons()

	def disable_buttons(self):

		if self.cells[1][1] != DISABLED:
			for i in range(0, self.vertical_size + 2):
				for j in range(0, self.horizontal_size + 2):
					self.cells[i][j].configure(state = DISABLED)

			self.stop_button.configure(state = NORMAL)
			self.play_button.configure(state = DISABLED)
			self.pause_button.configure(state = NORMAL)

	def enable_buttons(self):
		# resets game
		for i in range(0, self.vertical_size + 2):
			for j in range(0, self.horizontal_size + 2):
				self.cells[i][j]['bg'] = "white"
				self.cells[i][j].configure(state = NORMAL)

		self.stop_button.configure(state = DISABLED)
		self.play_button.configure(state = NORMAL)
		self.pause_button.configure(state = NORMAL)
		self.generate_next = True
		# Might need to change this
		self.pause = False

	def neighbor_count(self, x_coord, y_coord):
		count = 0
		for i in range(x_coord - 1, x_coord + 2):
			for j in range(y_coord - 1, y_coord + 2):
				if (i != x_coord or j != y_coord) and self.cells[i][j]['bg'] == "black":
					count += 1

		return count

	def cell_toggle(self, cell):
		if cell['bg'] == "white":
			cell['bg'] = "black"
		else:
			cell['bg'] = "white"

	### Create 4 presets for the game
	def preset(self):
		pass

	### Pause Button
	def pause_game(self):
		# Might need to change this
		self.pause = False

  # Stop button
	def stop_game(self):
		self.generate_next = False


if __name__ == '__main__':
	root = Tk()
	game = GameOfLife(root)
	root.mainloop()