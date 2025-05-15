from nba_api.live.nba.endpoints import scoreboard, playbyplay
import json

# 取得今日比賽
games = scoreboard.ScoreBoard().get_dict()['scoreboard']['games']

print(json.dumps(games,indent=4))
