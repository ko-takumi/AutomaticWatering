# -*- coding: utf-8 -*-
import Task
import time

class SwitchMonitoring(Task.Task):
	def __init__(self):
		super(SwitchMonitoring, self).__init__()

	def taskMain(self):
		while(True):
			print("SwitchMonitoring...")

			if len(self.mNameSpace) > 0:
				print("SwitchMonitoring CMD: ", self.mNameSpace.popleft())

			time.sleep(1)

	def func1(self):
		pass

	def stop(self):
		pass