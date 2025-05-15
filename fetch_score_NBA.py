from nba_api.live.nba.endpoints import scoreboard, boxscore, playbyplay
import json

# 取得當日所有比賽
games = scoreboard.ScoreBoard()
games_dict = games.get_dict()

p_score_home= []
p_score_away= []

# 利用API傳回來的欄位，進行分析
for game in games_dict['scoreboard']['games']:
    home_name=game['homeTeam']['teamTricode']
    away_name=game['awayTeam']['teamTricode']
    for period in game['homeTeam']['periods']:
       p_home_score =  p_score_home.append(period['score'])
    for period in game['awayTeam']['periods']:
       p_away_score =  p_score_away.append(period['score'])
       
    home_score = game['homeTeam']['score']
    away_score = game['awayTeam']['score']
    
    
    print(f'{home_name} {home_score} vs {away_score} {away_name}')
    print(home_name)
    for idx,p in enumerate(p_score_home,start=1):
        print(f'第{idx}節: {p}分')
    p_score_home.clear()
    print('-'*20)
    print(away_name)
    for idx,p in enumerate(p_score_away,start=1):
        print(f'第{idx}節: {p}分')
    p_score_away.clear()
    
