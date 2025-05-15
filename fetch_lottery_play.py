import requests
import json

params = {'sport': 'NBA',       # 選擇賽事
          'date': '2025-05-15', # 指定日期
          'mode': 'close'}      # close, open, both, all
headers = {'X-JBot-Token': 'FREE_FOR_TEST_20_TIMES_PER_DAY'}    # 填寫密鑰

url = 'https://api.sportsbot.tech/v2/odds'
res = requests.get(url, headers=headers, params=params)

# 取得JSON資料
data = res.json()

# 將JSON寫入檔案
with open('NBA_Lottery.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)