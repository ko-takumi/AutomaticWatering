# -*- coding: utf-8 -*-
import AutomaticWatering
from StateMemory import StateMemory

if __name__ == '__main__':
	# シングルトン生成
	StateMemory.StateMemory()

	# 水やり本体実施
	automaticWatering = AutomaticWatering.AutomaticWatering()
	automaticWatering.execute()