# -*- coding: utf-8 -*-
import Task
import time
from DataManagement import SwitchData
from . import SwitchButton
from . import define

class SwitchMonitoring(Task.Task):
	mSwitchList = []
	def __init__(self):
		super(SwitchMonitoring, self).__init__()
		print("SwitchMonitoring[", self, "] : Create.")
		self.mSwitchList.append(SwitchButton.SwitchButton())
		self.switchData = SwitchData.SwitchData()

	def __del__(self):
		print("SwitchMonitoring[", self, "] : Delete.")

	def taskMain(self):
		while(True):
			print("SwitchMonitoring...")

			# スイッチ状態を取得する
			for swObj in self.mSwitchList:
				swStatus = swObj.get()
				if swStatus is True:
					self.switchData.notifyON()

			if len(self.mNameSpace) > 0:
				cmd = self.mNameSpace.popleft()
				print("SwitchMonitoring CMD: ", cmd)

				if cmd == define.SM_CMD_STOP:	# 終了コマンド
					self.stop()
					return
				else:
					print("error.", cmd)

			if self.mIsActive == False:
				return

			time.sleep(1)

	def func1(self):
		pass

	def kill(self):
		self.mIsActive = False
