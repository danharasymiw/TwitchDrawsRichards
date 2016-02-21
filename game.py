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
	
	def paint(self):
		if self.painting:
			half_brush_size = self.brush_size / 2
			self.frame[max(self.y - half_brush_size, 0) : min(self.y + half_brush_size, self.HEIGHT),
						max(self.x - half_brush_size, 0) : min(self.x + half_brush_size, self.WIDTH),
						:] = np.array(self.colour)[None, None, :]
			
	def move_up(self):
		if self.is_valid_y_movement(self.y - self.movement_amount):
			self.y -= self.movement_amount


	def move_down(self):
		if self.is_valid_y_movement(self.y + self.movement_amount):
			self.y += self.movement_amount


	def move_left(self):
		if self.is_valid_x_movement(self.x - self.movement_amount):
			self.x -= self.movement_amount


	def move_right(self):
		if self.is_valid_x_movement(self.x + self.movement_amount):
			self.x += self.movement_amount


	def is_valid_x_movement(self, x):
		half_brush_size = self.brush_size / 2
		return half_brush_size <= x <= self.WIDTH - half_brush_size


	def is_valid_y_movement(self, y):
		half_brush_size = self.brush_size / 2
		return half_brush_size <= y  <= self.HEIGHT - half_brush_size


	def change_size(self, size):
		if Commands.MIN_BRUSH_SIZE <= size <= Commands.MAX_BRUSH_SIZE:
			self.movement_amount = size - 1
			self.brush_size = size

	def reset(self):
		print ('resetting')
		self.clear_board()
		self.change_size(Commands.DEFAULT_BRUSH_SIZE)
		self.x = 200
		self.y = 200

	def clear_board(self):
		self.frame = np.zeros((self.HEIGHT, self.WIDTH, 3))
		self.frame[:,:,:] = np.array([1, 1, 1])[None, None, :]
		print ('clearing the board')
