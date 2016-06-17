#coding: utf-8

from random import random

import model

class BlockFreeController:

	def __init__(self, parent):
		self.parent = parent
		self.block = False

	def update(self):
		block_s = self.parent.block_s

		if(self.block == False):
			pos = ( int(random() * (self.parent.size[0] / block_s)) * block_s , int(random() * (self.parent.size[1] / block_s)) * block_s )
			self.block = model.BlockFree(False, pos)

			# while(self.block.collidelist(self.parent.stage_blocks) != -1):
			# 	pos = ( int(random() * (self.parent.size[0] / block_s)) * block_s , int(random() * (self.parent.size[1] / block_s)) * block_s )
			# 	self.block = model.BlockFree(False, pos)

		if(self.block != False):
			self.block.paint(self.parent.screenBuffer)