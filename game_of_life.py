from tkinter import *
from tkinter import font
import time

class GameOfLife(Frame):

	def __init__(self, main_frame):

		Frame.__init__(self, main_frame)
		self.main_frame = main_frame
		self.grid(row = 0, column = 0)

		self.horizontal_size = 25
		self.vertical_size = 25
		self.cells = []
		self.generate_next = True

		self.init_UI()

	def init_UI(self):	

		self.main_frame.title("Game of Life")

		# frame for title and line of instruction
		self.title_frame = Frame(self.main_frame)
		self.title_frame.grid(row = 0, column = 0, columnspan = 4)

		self.titleFont = font.Font(family="Verdana", size=16)
		title = Label(self.title_frame, text = "Conway's Game of Life", font = self.titleFont)
		title.pack(side = TOP)

		prompt = Label(self.title_frame, text = "Watch the cells come to life! Click the cells to create the starting configuration. Once you're ready, the press Start Game button!")
		prompt.pack(side = BOTTOM)