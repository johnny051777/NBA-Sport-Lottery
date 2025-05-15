import json
import requests
import random
from fake_useragent import UserAgent

ua = UserAgent()
user_agent = ua.random
headers = {'user-agent': user_agent}
res = requests.get("https://www.sportslottery.com.tw/api/services/app/LiveGames/GetLiveOnAndRegister?isContainRegister=false", headers = headers)
#print(res.status_code) #顯示網頁回傳狀態
data = res.json()

#Test json file in local
#path = '2.json'
#with open(path,"rb") as f :
    #data = json.load(f)
    #print(data)   #讀取出來的資料型別為dict型

Game_data = data['result']['liveOn']

if len(Game_data) == 0:
    print("目前沒有任何賽事")
else:
    for i in range(len(Game_data)):
        Game_name = Game_data[i]['ln'][0]
        player_one_chinese = Game_data[i]['atn'][0]
        player_one_english = Game_data[i]['atn'][1]
        player_two_chinese = Game_data[i]['htn'][0]
        player_two_english = Game_data[i]['htn'][1]
        player_one_score = Game_data[i]['as'].get('10') #當局分數 ex:tennis 
        player_two_score = Game_data[i]['hs'].get('10') #當局分數 ex:tennis
        
        print("\n" + Game_name)
        print("{} : {}".format(player_one_chinese,player_two_chinese))
        for b in range(len(Game_data[i]['as'])):
            b = b + 1
            player_one_as = Game_data[i]['as'].get(str(b))
            if player_one_as == -1 :
                break
            else:
                player_two_hs = Game_data[i]['hs'].get(str(b))
                print("第{}局 {} : {}".format(b, player_one_as, player_two_hs))
        
        #網球
        if Game_data[i]['si'] == 445:
            print("{} : {}".format(player_one_score, player_two_score))
        
        #動畫連結
        #res1 = requests.get("https://h2h.sportslottery.com.tw/sportradar/zht/h2h.html?matchID={}".format(Game_data[i]['mi']), headers = headers)
        #if res1.status_code == 200:
        #   print(res1)
        
        ball_type = Game_data[i]['si']
        if ball_type == 441:
            time = Game_data[i]['ed']
            print("比賽進行時間：{}".format(time[21:23]))