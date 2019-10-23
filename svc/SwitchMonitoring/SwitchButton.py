# -*- coding: utf-8 -*-
Def_SW_PIN = 14

class SwitchButton(object):
	def __init__(self):
		pass

	def __del__(self):
		pass

	def get(self):
		# =======>
		# TODO: ここで、スイッチ状態を取得する
		# 下記暫定コード
		# <======
		strA = input()
		if strA is "1":
			return True
		else:
			return False 