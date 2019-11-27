# -*- coding: utf-8 -*-
import requests

class LINENotify():
    def __init__(self):
        
        url = 'https://notify-api.line.me/api/notify'
        access_token = 'Token'
        headers = {'Authorization':'Bearer' + access_token}
        
        pass
    
    def execute(self):
        #message = 'hoge'
        #payload = {'message':message}
        #r = requests.post(url, headers=headers, params=payload,)
        
        pass