# -*- coding: utf-8 -*-
import threading
from collections import deque
import copy

class Task(threading.Thread):
	def __init__(self):
		super(Task, self).__init__()

	def __del__(self):
		pass

	def run(self):
		self.mIsActive = True
		self.mNameSpace = deque([])
		self.taskMain()

	def notifySignal(self, cmd):
		self.mNameSpace.append(copy.deepcopy(cmd))