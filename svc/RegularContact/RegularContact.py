# -*- coding: utf-8 -*-
import Task
import time
from RegularContact.LINENotify import LINENotify
from StateMemory.API_StateMemory import API_StateMemory


class RegularContact(Task.Task):
	def __init__(self):
		super(RegularContact, self).__init__()

	def taskMain(self):
		while(True):
			print("RegularContact...")

			if len(self.mNameSpace) > 0:
				print("RegularContact CMD: ", self.mNameSpace.popleft())

			time.sleep(1)
			
			"水やり判定結果取得"
			isWater, reason = StateMemory.API_StateMemory.getDisWater()
			if reason == "温度":
                            "湿度判定で水やった"
                            print()
                            RegularContact.LINENotify.execute()
                        elif reason == "時間":
			    "時間判定で水やった"
			    print()
			    RegularContact.LINENotify.execute()
			elif reason == "手動":
                            "手動判定で水やった"
                            print()
                            RegularContact.LINENotify.execute()
                        else:
                            "水やらなくていいよ"
                            print()
                            RegularContact.LINENotify.execute()

                        "水量取得"
			waterRmaining = StateMemory.API_StateMemory.getWaterRemaining()
			if waterRmaining <= 50:
                        			"水量が50%切った"
                        			 print()
                            RegularContact.LINENotify.execute()
			elif waterRmaining == 0:
                        			"水量が0%切った"
                        			 print()
                            RegularContact.LINENotify.execute()
                        else:
                            "水量は十分"
                            print()
                            RegularContact.LINENotify.execute()
                            
                        "土壌湿度取得"
                        humidity = StateMemory.API_StateMemory.getHumidity()
