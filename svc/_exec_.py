# -*- coding: utf-8 -*-
import AutomaticWatering
from StateMemory import API_StateMemory

if __name__ == '__main__':

	API_StateMemory.API_StateMemory()

	# 水やり本体実施
	automaticWatering = AutomaticWatering.AutomaticWatering()
	automaticWatering.execute()
	