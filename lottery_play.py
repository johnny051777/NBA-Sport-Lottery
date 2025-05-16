
class lottery:
    
    #不讓分
    def noscore_team(homeScore , awayScore): 
        if homeScore > awayScore:
            return '主隊WIN'
        elif homeScore < awayScore:
            return '客隊WIN'
        elif homeScore == awayScore:
            return '平手'
        else:
            return 'Error' 
        
    # 勝分差
    def WIN_DE_score(homeScore , awayScore):
        W_L = abs(homeScore - awayScore)
        
        if W_L>=1 and W_L<=5:
            return '勝分差1~5 WIN'
        elif W_L>=6 and W_L<=10:
            return '勝分差6~10 WIN'
        elif W_L>=11 and W_L<=15:
            return '勝分差11~15 WIN'
        elif W_L>=16 and W_L<=20:
            return '勝分差16~20 WIN'
        elif W_L>=21 and W_L<=25:
            return '勝分差21~25 WIN'
        elif W_L>=26 and W_L<=30:
            return '勝分差26~30 WIN'
        elif W_L>30:
            return '勝分差30↑ WIN'
        else:
            return 'Error'