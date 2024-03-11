from datetime import datetime, timedelta
import schedule
import time
# 初始化資料庫連線
import pymongo

# 設定本地 MongoDB 的連接地址
client = pymongo.MongoClient("mongodb://localhost:27017/")

# 選擇想要連接的資料庫
db=client.db

# 選擇想要連接的集合
collection=db.document


"""
# 網路連線
import urllib.request as request
import json
url="https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1"
with request.urlopen(url) as response:
    data=json.load(response) # 利用 json 模組處理 json 資料格式
# 取出活動名稱
activity = data[0]
title = activity["title"]
print(title)
"""

# 嘗試速度更快的寫法

import requests

def fetch_and_update():
    url = "https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=1"
    response = requests.get(url)
    data = response.json()

    # 直接取出第一筆資料的 title
    title = data[0]["title"]
    # print(title)


    # 取得當前時間
    current_time = datetime.now()

    # 在 mongoDB 插入一筆資料
    collection.insert_one({
        "activity":title,
        "date": current_time
    })


fetch_and_update()

# 以下為自動定時功能程式,如須使用請解除註解
# 並註解 54行 fetch_and_update()
'''
# 定義每天01:00:00(UTC+8)執行任務的函數
def job():
    print("Fetching and updating data...")
    fetch_and_update()
    print("Data fetched and updated successfully.")

# 設定每天01:00:00(UTC+8)執行任務
schedule.every().day.at("01:00:00").do(job)

# 主循環
while True:
    # 檢查是否有任務需要執行
    schedule.run_pending()
    time.sleep(1)
'''
