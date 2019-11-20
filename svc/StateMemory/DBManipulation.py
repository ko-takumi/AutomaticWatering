# -*- coding: utf-8 -*-
import sqlite3
import os

# 実際にはraspberryPiのフォルダを指定する
DEF_DBNAME = 'db/TEST.db'

class DBManipulation(object):
	mDb = None

	def __init__(self):
		isExistsFile = os.path.exists(DEF_DBNAME)
		if isExistsFile == True:
			self.mDb = sqlite3.connect(DEF_DBNAME)
			self.createDb()

		self.mDb = sqlite3.connect(DEF_DBNAME)

	def __del__(self):
		self.mDb.close()

	def createDb(self):
		pass