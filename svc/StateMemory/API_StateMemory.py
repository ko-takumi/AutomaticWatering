# -*- coding: utf-8 -*-
from StateMemory import DBManipulation

class API_StateMemory(object):
	mInstance = None
	mDbCtrl = False
	def __new__(self):
		if self.mInstance == None:
			self.mInstance = super(API_StateMemory, self).__new__(self)
			self.mDbCtrl = DBManipulation.DBManipulation()
		return self.mInstance

	################################
	# 通知メソッド
	################################
	# 水やり実施と理由の通知
	def notifyDisWater(self, reason):
		result = self.mDbCtrl.setWateringLog(reason)
		if result == False:
			print("[Error] notifyDisWater.")
			return False
		return True

	# 土壌湿度の通知
	def notifyHumidity(self, value):
		result = self.mDbCtrl.setHumidityLog(value)
		if result == False:
			print("[Error] notifyWaterRemaining.")
			return False
		return True

	# 残水量の通知
	def notifyWaterRemaining(self, value):
		result = self.mDbCtrl.setWaterRemainingLog(value)
		if result == False:
			print("[Error] notifyWaterRemaining.")
			return False
		return True

	################################
	# 取得メソッド
	################################
	# 水やり実施と理由の取得
	def getDisWater(self):
		isWater = True
		reason = "xxxxx"
		return isWater, reason

	# 土壌湿度の取得
	def getHumidity(self):
		value = 0.0
		return value

	# 残水量の取得
	def getWaterRemaining(self):
		value = 0.0
		return value

API_StateMemory()
