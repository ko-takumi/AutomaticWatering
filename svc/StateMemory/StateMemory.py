# -*- coding: utf-8 -*-
import sqlite3

# 実際にはraspberryPiのフォルダを指定する
DEF_DBNAME = 'db/TEST.db'

class StateMemory():
	mInstance = None
	mSwStatus = False
	mDb = None
	def __new__(self):
		if self.mInstance == None:
			self.mInstance = super(StateMemory, self).__new__(self)
			self.mDb = sqlite3.connect(DEF_DBNAME)

		return self.mInstance

	def get(self):
		tmp = self.mSwStatus
		self.mSwStatus = False
		return tmp

StateMemory()