# -*- coding: utf-8 -*-
import Task
import time
from RegularContact.LINENotify import LINENotify


class RegularContact(Task.Task):
	def __init__(self):
		super(RegularContact, self).__init__()

	def taskMain(self):
		while(True):
			print("RegularContact...")

			if len(self.mNameSpace) > 0:
				print("RegularContact CMD: ", self.mNameSpace.popleft())

			time.sleep(1)

	def func1(self):
		pass

	def stop(self):
		pass