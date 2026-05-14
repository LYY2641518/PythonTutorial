import requests as rq
url = "http://tqc.codejudger.com:3000/target/5205.json"
res = rq.get(url).json()
#◆程式須回傳新北市每一個地區的相關訊息:地區名稱、AQI指數、PM2.5指數、PM10指數、
newtaipei = [
    {f"地區 : {el["SiteName"]} ",f"AQI : {el["AQI"]} ",f"PM2.5 : {el["PM2.5"]} ",f"PM10 : {el["PM10"]} ",f"資料更新時間 : {el["PublishTime"]}" }
    for el in res 
    if el["County"]=="新北市"
    ]
print(newtaipei)