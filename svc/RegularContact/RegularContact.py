# -*- coding: utf-8 -*-
import Task
import time
from RegularContact.LINENotify import LINENotify
from StateMemory.API_StateMemory import API_StateMemory


class RegularContact(Task.Task):
    mLINENotify		= None
    mAPI_StateMemory	= None
    
    def __init__(self):
        super(RegularContact, self).__init__()
        self.mLINENotify = LINENotify.LINENotify()
        self.mAPI_StateMemory = API_StateMemory()

    def taskMain(self):
        while(True):
            print("RegularContact...")

            if len(self.mNameSpace) > 0:
                print("RegularContact CMD: ", self.mNameSpace.popleft())

            time.sleep(1)

            #水やり判定結果取得
            isWater, reason = self.mAPI_StateMemory.getDisWater()
            if reason == 0:
                #湿度判定で水やった
                print()
                self.mLINENotify.execute()
            elif reason == 0:
                #時間判定で水やった
                print()
                self.mLINENotify.execute()
            elif reason == 0:
                #手動判定で水やった
                print()
                self.mLINENotify.execute()
            else:
                #水やらなくていいよ
                print()
                self.mLINENotify.execute()

            #水量取得
            waterRmaining = self.mAPI_StateMemory.getWaterRemaining()
            if waterRmaining <= 50:
                #水量が50%切った
                print()
                self.mLINENotify.execute()
            elif waterRmaining == 0:
                #水量が0%切った
                print()
                self.mLINENotify.execute()
            else:
                #水量は十分
                print()
                self.mLINENotify.execute()

            #土壌湿度取得
            humidity = self.mAPI_StateMemory.getHumidity()
