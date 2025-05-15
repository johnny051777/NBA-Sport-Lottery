from nba_api.live.nba.endpoints import scoreboard, playbyplay
import json

# 取得今日比賽資訊
sb = scoreboard.ScoreBoard()
games = sb.get_dict()["scoreboard"]["games"]

print(json.dumps(games[1],indent=4))
