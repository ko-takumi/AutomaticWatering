# -*- coding: utf-8 -*-
from WaterMonitoring import WaterMonitoring
from WateringJudge import WateringJudge
from StateMemory import StateMemory
from RegularContact import RegularContact
from PumpControl import PumpControl
from SwitchMonitoring import SwitchMonitoring

import time

# 定義
WATERING_TIME = 10

if __name__ == '__main__':
	# インスタンス化
	#	水やり判定
	#	水切れ判定
	#	ポンプ操作
	wateringJudge	= WateringJudge.WateringJudge()
	waterMonitoring	= WaterMonitoring.WaterMonitoring()
	pumpControl		= PumpControl.PumpControl()

	# スレッド生成
	#	定期連絡
	#	スイッチ監視
	regularContact = RegularContact.RegularContact()
	regularContact.create()
	regularContact.execute()

	switchMonitoring = SwitchMonitoring.SwitchMonitoring()
	switchMonitoring.create()
	switchMonitoring.execute()

	# シングルトン生成
	StateMemory.StateMemory()

	# 異常判定は全て各クラス内で処理しているため、無視する
	while(True):
		# 水切れ監視
		waterMonitoring.execute()

		# 水やり判定
		#	水槽は異常ないか
		#		異常の場合
		#			処理抜け
		#		異常ない場合
		#			水やり不要な場合
		#				処理抜け
		#			水やり実施
		isNormal = waterMonitoring.isShortfall()
		if(isNormal == False):
			# 水槽が異常時は以後続けない
			continue

		isJudge = wateringJudge.isExecute()
		if(isJudge == False):
			# 水が必要ではない
			continue

		# 水やり
		pumpControl.execute(WATERING_TIME)

		time.sleep(10)
