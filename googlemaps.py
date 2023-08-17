import requests 
import json
import random
import time

j = 0
lottery_pool = []

while 1:
    time.sleep(2)
    # 這邊的連結不是Google Map商家的連結喔!我們明天再說這個連結是怎麼來的~
    url="https://www.google.com/maps/preview/review/listentitiesreviews?authuser=0&hl=zh-TW&gl=tw&pb=!1m2!1y3765760635254824349!2y1347822120135287225!2m2!1i10!2i"+ str(j) +"!3e1!4m5!3b1!4b1!5b1!6b1!7b1!5m2!1s3nPOYfOBG9Hn-QbTg4fQDw!7e81"
    j = j + 10 # 因為一頁評論最多有十條，連結規律是10、20、30...，所以一次要加10
    text = requests.get(url).text # 發送get請求 
    pretext = ')]}\'' # 取代特殊字元
    text = text.replace(pretext,' ') # 把字串讀取成json
    soup = json.loads(text) # 載入json檔

    review_list = soup[2] # 留言的位置

    if review_list is None:
        break
   
    for i in review_list:
        time.sleep(1)
        print("姓名: " + str(i[0][1]))
        print("時間: " + str(i[1]))
        print("星星數: " + str(i[4]))
        print("留言內容: " + str(i[3]))
        # 姓名: str(i[0][1])
        # 時間: str(i[1])
        # 星星數: str(i[4])
        # 留言內容: str(i[3])  
