from nba_api.live.nba.endpoints import scoreboard, boxscore, playbyplay
import json


class Fetch_Score:
    
    def __init__(self):
        self.games = scoreboard.ScoreBoard()
        self.game_dict = self.games.get_dict()
    
    
    def score_information(self):
        p_score_home= []
        p_score_away= []
        
        for game in self.game_dict['scoreboard']['games']:
            home_name=game['homeTeam']['teamTricode']
            away_name=game['awayTeam']['teamTricode']
            for period in game['homeTeam']['periods']:
                p_score_home.append(period['score'])
            for period in game['awayTeam']['periods']:
                p_score_away.append(period['score'])
            
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
