# -*- coding: utf-8 -*-

class API_StateMemory():
	mInstance = None
	mSwStatus = False
	def __new__(self):
		if self.mInstance == None:
			self.mInstance = super(API_StateMemory, self).__new__(self)
		return self.mInstance

	################################
	# 通知メソッド
	################################
	# 土壌湿度の通知
	def notifyHumidity(self, value):
		return True

	# 水やり実施と理由の通知
	def notifyDisWater(self, reason):

		return True

	# 残水量の通知
	def notifyWaterRemaining(self, value):

		return True

	################################
	# 取得メソッド
	################################
	# 土壌湿度の取得
	def getHumidity(self):
		value = 0.0
		return value

	# 水やり実施と理由の取得
	def getDisWater(self):
		isWater = True
		reason = "xxxxx"
		return isWater, reason

	# 残水量の取得
	def getWaterRemaining(self):
		value = 0.0
		return value

API_StateMemory()