# -*- coding: utf-8 -*-
import threading
from collections import deque

class Task(threading.Thread):
	mNameSpace = deque([])

	def __init__(self):
		super(Task, self).__init__()

	def __del__(self):
		pass

	def run(self):
		self.taskMain()

	def notifySignal(self, cmd):
		self.mNameSpace.append(cmd)