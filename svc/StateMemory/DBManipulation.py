# -*- coding: utf-8 -*-
import sqlite3
import os
import time

# 実際にはraspberryPiのフォルダを指定する
DEF_DBNAME = 'db/TEST.db'

# テーブル
DEF_WARTRING		= 'wateringLogs'		# 水やりTable
DEF_HUMIDTY			= 'HumidityLogs'		# 湿度Table
DEF_WATERREMAINING	= 'WaterRemainingLogs'	# 水残量Table

class DBManipulation(object):
	mDb = None
	mWateringIdMax = 0
	mHumidityIdMax = 0
	mWaterRemainingIdMax = 0

	def __init__(self):
		self.__prepareDb()

	def __del__(self):
		self.mDb.close()

	# Private
	# DB初期化
	def __prepareDb(self):
		isExistsFile = os.path.exists(DEF_DBNAME)
		if isExistsFile == False:
			self.mDb = sqlite3.connect(DEF_DBNAME)
			# 水やりログテーブル作成
			# 土壌湿度ログテーブル作成
			# 残水量ログテーブル作成
			self.__execSQL('''CREATE TABLE wateringLogs(id real, history text, reason INTEGER)''')
			self.__execSQL('''CREATE TABLE HumidityLogs(id real, history text, value INTEGER)''')
			self.__execSQL('''CREATE TABLE WaterRemainingLogs(id real, history text, value INTEGER)''')
			
		else:
			self.mDb = sqlite3.connect(DEF_DBNAME)
			self.mWateringIdMax			= self.__getIDMax(DEF_WARTRING)
			self.mHumidityIdMax			= self.__getIDMax(DEF_HUMIDTY)
			self.mWaterRemainingIdMax	= self.__getIDMax(DEF_WATERREMAINING)

	# Private
	# SQL実行
	def __execSQL(self, text):
		try:
			conect = self.mDb.cursor()
			conect.execute(text)
			self.mDb.commit()
		except:
			print("[Error] sql wite error.")
			return False
		return True

	# Private
	# 指定したtableの格納数取得
	def __getIDMax(self, table):
		sql = "SELECT count(*) FROM " + table
		conect = self.mDb.cursor()
		conect.execute(sql)
		count = conect.fetchall()[0][0]
		return int(count)

	# Public
	# 水やりログの格納
	def setWateringLog(self, reason):
		history = time.time()
		print(history)
		sql = "INSERT INTO {} VALUES ({}, '{}', {})".format(DEF_WARTRING, self.mWateringIdMax + 1, history, reason)
		result = self.__execSQL(sql)
		if result == False:
			print("[Error] __execSQL error.")
			return False

		self.mWateringIdMax += 1
		return True

	# Public
	# 湿度ログの格納
	def setHumidityLog(self, value):
		history = time.time()
		print(history)
		sql = "INSERT INTO {} VALUES ({}, '{}', {})".format(DEF_HUMIDTY, self.mHumidityIdMax + 1, history, value)
		result = self.__execSQL(sql)
		if result == False:
			print("[Error] __execSQL error.")
			return False

		self.mHumidityIdMax += 1
		return True

	# Public
	# 水残量ログの格納
	def setWaterRemainingLog(self, value):
		history = time.time()
		print(history)
		sql = "INSERT INTO {} VALUES ({}, '{}', {})".format(DEF_WATERREMAINING, self.mWaterRemainingIdMax + 1, history, value)
		result = self.__execSQL(sql)
		if result == False:
			print("[Error] __execSQL error.")
			return False

		self.mWaterRemainingIdMax += 1
		return True

