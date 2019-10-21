# -*- coding: utf-8 -*-
from WaterMonitoring import WaterMonitoring
from WateringJudge import WateringJudge
from RegularContact import RegularContact
from PumpControl import PumpControl
from SwitchMonitoring import SwitchMonitoring

import time

# 定義
WATERING_TIME = 10

class AutomaticWatering(object):
	mWateringJudge		= None
	mWaterMonitoring	= None
	mPumpControl		= None

	mRegularContact		= None
	mSwitchMonitoring	= None

	def __init__(self):
		# インスタンス化
		#	水やり判定
		#	水切れ判定
		#	ポンプ操作
		self.mWateringJudge		= WateringJudge.WateringJudge()
		self.mWaterMonitoring	= WaterMonitoring.WaterMonitoring()
		self.mPumpControl		= PumpControl.PumpControl()

		# スレッド生成
		#	定期連絡
		#	スイッチ監視
		self.mRegularContact = RegularContact.RegularContact()
		self.mRegularContact.create()
		self.mRegularContact.execute()

		self.mSwitchMonitoring = SwitchMonitoring.SwitchMonitoring()
		self.mSwitchMonitoring.create()
		self.mSwitchMonitoring.execute()

		return

	def execute(self):
		# 異常判定は全て各クラス内で処理しているため、無視する
		while(True):
			# 水切れ監視
			self.mWaterMonitoring.execute()

			# 水やり判定
			#	水槽は異常ないか
			#		異常の場合
			#			処理抜け
			#		異常ない場合
			#			水やり不要な場合
			#				処理抜け
			#			水やり実施
			isNormal = self.mWaterMonitoring.isShortfall()
			if(isNormal == False):
				# 水槽が異常時は以後続けない
				continue

			isJudge = self.mWateringJudge.isExecute()
			if(isJudge == False):
				# 水が必要ではない
				continue

			# 水やり
			self.mPumpControl.execute(WATERING_TIME)

			time.sleep(10)

		return
