class Games:
    partidos =[]
    def __init__(self,home_team, away_team, date, stadium_id, id):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium_id = stadium_id
        self.id = id

    def mostrarGames(self):
    
        return(f'''HOME TEAM: {self.home_team}
AWAY TEAM: {self.away_team}
DATE: {self.date}
STADIUM: {self.stadium_id}
ID: {self.id}

''')

    

            