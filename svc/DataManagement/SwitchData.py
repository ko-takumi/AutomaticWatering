# -*- coding: utf-8 -*-

class SwitchData(object):
	mInstance = None
	mSwStatus = False

	def __new__(self):
		if self.mInstance == None:
			self.mInstance = super(SwitchData, self).__new__(self)
		return self.mInstance

	def notifyON(self):
		self.mSwStatus = True

	def get(self):
		tmp = self.mSwStatus
		self.mSwStatus = False
		return tmp

SwitchData()