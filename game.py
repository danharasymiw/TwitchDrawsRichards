import numpy as np
import Commands

class Game:
	WIDTH = 640
	HEIGHT = 480

	painting = True
	colour = [0, 0, 0]
	brush_size = 10
	movement_amount = 10
	x = 0
	y = 0
	
	prev_x = x
	prev_y = y
	prev_brush_size = brush_size
	prev_colour = colour
	
	
	def paint(self):
		# redo last painting instruction to draw over cursor
		print 'prev x', self.prev_x, 'prev y', self.prev_y
		print 'x', self.x, 'y', self.y
		prev_half_brush_size = self.prev_brush_size / 2
		self.frame[max(self.prev_y - prev_half_brush_size, 0) : min(self.prev_y + prev_half_brush_size, self.HEIGHT),
						max(self.prev_x - prev_half_brush_size, 0) : min(self.prev_x + prev_half_brush_size, self.WIDTH),
						:] = np.array(self.prev_colour)[None, None, :]
		
		if self.painting:
			half_brush_size = self.brush_size / 2
			self.frame[max(self.y - half_brush_size, 0) : min(self.y + half_brush_size, self.HEIGHT),
						max(self.x - half_brush_size, 0) : min(self.x + half_brush_size, self.WIDTH),
						:] = np.array(self.colour)[None, None, :]
						
		# top and bottom of cursor
		self.frame[max(self.y - 1, 0) : min(self.y + 1, self.HEIGHT),
					max(self.x - half_brush_size, 0) : min(self.x + half_brush_size, self.WIDTH),
					:] = np.array((0, 1, 1))[None, None, :]
		self.frame[max(self.y - half_brush_size, 0) : min(self.y + half_brush_size, self.HEIGHT),
					max(self.x - 1, 0) : min(self.x + 1, self.WIDTH),
					:] = np.array((1, 1, 0))[None, None, :]
		
		
			
			
	def move_up(self, amount):
		while amount > 0:
			print 'amount', amount
			if self.is_valid_y_movement(self.y - self.movement_amount):
				self.set_previous_brush()
				self.y -= self.movement_amount
				amount -= 1
				self.paint()

	def move_down(self, amount=1):
		while amount > 0:
			if self.is_valid_y_movement(self.y + self.movement_amount):
				self.set_previous_brush()
				self.y += self.movement_amount
				amount -= 1
				self.paint()

	def move_left(self, amount=1):
		while amount > 0:
			if self.is_valid_x_movement(self.x - self.movement_amount):
				self.set_previous_brush()
				self.x -= self.movement_amount
				amount -= 1
				self.paint()


	def move_right(self, amount=1):
		while amount > 0:
			if self.is_valid_x_movement(self.x + self.movement_amount):
				self.set_previous_brush()
				self.x += self.movement_amount
				amount -= 1
				self.paint()

	def is_valid_x_movement(self, x):
		half_brush_size = self.brush_size / 2
		return 0 <= x <= self.WIDTH


	def is_valid_y_movement(self, y):
		half_brush_size = self.brush_size / 2
		return 0 <= y  <= self.HEIGHT


	def change_size(self, size):
		if Commands.MIN_BRUSH_SIZE <= size <= Commands.MAX_BRUSH_SIZE:
			self.movement_amount = size - 1
			self.set_previous_brush()
			self.brush_size = size
			self.paint()
			
	def change_colour(self, colour):
		self.set_previous_brush()
		self.colour = colour
		self.paint()

	def set_previous_brush(self):
		self.prev_x = self.x
		self.prev_y = self.y
		self.prev_brush_size = self.brush_size
		self.prev_colour = self.colour
		

	def reset(self):
		print ('resetting')
		self.clear_board()
		self.change_size(Commands.DEFAULT_BRUSH_SIZE)
		self.x = self.WIDTH / 2
		self.y = self.HEIGHT / 2
		
		self.prev_x = self.x
		self.prev_y = self.y
		self.prev_brush_size = self.brush_size
		self.prev_colour = self.colour
		self.paint()		

	def clear_board(self):
		self.frame = np.zeros((self.HEIGHT, self.WIDTH, 3))
		self.frame[:,:,:] = np.array([1, 1, 1])[None, None, :]
		print ('clearing the board')
		
	
		
