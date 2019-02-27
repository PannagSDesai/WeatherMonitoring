import requests
from boltiot import Bolt
import time
import conf
import json
url='https://api.openweathermap.org/data/2.5/weather?q=Bangalore&appid=d6b235132831e446bcd3df18f84b4724'
json_data=requests.get(url).json()
weather = json_data['weather'][0]['id']
mybolt=Bolt(conf.API_KEY,conf.DEVICE_ID)

while True:
      response1=mybolt.isOnline()
      c=json.loads(response1)
      cc=c['success']
      print(weather)
      if cc!=1:
         print ("Error in retrieving information")
         break
      if weather==200:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'LOW')
         mybolt.digitalWrite(3,'LOW')
         mybolt.digitalWrite(4,'HIGH')
      if weather==202:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'LOW')
         mybolt.digitalWrite(3,'HIGH')
         mybolt.digitalWrite(4,'HIGH')
      if weather==500 or weather==501 or weather==502 or weather==503 or weather==504 or weather==511 or weather==520 or weather==521 or weather==522 or weather==523:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'HIGH')
         mybolt.digitalWrite(3,'HIGH')
         mybolt.digitalWrite(4,'HIGH')
      if weather==801 or weather==802 or weather==804:
         mybolt.digitalWrite(1,'HIGH')
         mybolt.digitalWrite(2,'HIGH')
         mybolt.digitalWrite(3,'HIGH')
         mybolt.digitalWrite(4,'HIGH')
      if weather==800:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'LOW')
         mybolt.digitalWrite(3,'LOW')
         mybolt.digitalWrite(4,'LOW')
      if weather==300 or weather==301 or weather==302 or weather==310 or weather==311 or weather==312 or weather==313 or weather==314 or weather==321:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'HIGH')
         mybolt.digitalWrite(3,'LOW')
         mybolt.digitalWrite(4,'LOW')   
      if weather==803:
         mybolt.digitalWrite(1,'HIGH')
         mybolt.digitalWrite(2,'HIGH')
         mybolt.digitalWrite(3,'LOW')
         mybolt.digitalWrite(4,'LOW')
      if weather==600 or weather==601 or weather==602 or weather==611 or weather==612 or weather==615 or weather==616 or weather==620 or weather==621 or weather==622:
         mybolt.digitalWrite(1,'LOW')
         mybolt.digitalWrite(2,'LOW')
         mybolt.digitalWrite(3,'HIGH')
         mybolt.digitalWrite(4,'LOW')
      if weather==701 or weather==711 or weather==721 or weather==731 or weather==740 or weather==751 or weather==761 or weather==762 or weather==771 or weather==781:
         mybolt.digitalWrite(1,'HIGH')
         mybolt.digitalWrite(2,'LOW')
         mybolt.digitalWrite(3,'LOW')
         mybolt.digitalWrite(4,'LOW')
      if weather==201 or weather==210 or weather==211 or weather==212 or weather==221 or weather==230 or weather==231 or weather==2323:
         mybolt.digitalWrite(1,'HIGH')
         mybolt.digitalWrite(2,'HIGH')
         mybolt.digitalWrite(3,'HIGH')
         mybolt.digitalWrite(4,'LOW')
      time.sleep(600)