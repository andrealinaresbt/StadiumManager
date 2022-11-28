class Games:
    partidos =[]
    seat =[]
    def __init__(self,home_team, away_team, date, stadium_id, stadium, capacity, id):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.stadium_id = stadium_id
        self.stadium = stadium
        self.id = id
        self.capacity = capacity
        self.seats = [[0 for i in range(self.capacity[1])] for _ in range(self.capacity[0])]
        self.ticketsSold = []
        self.attendance = []

    def mostrarGames(self):
    
        return(f'''HOME TEAM: {self.home_team}
AWAY TEAM: {self.away_team}
DATE: {self.date}
STADIUM: {self.stadium_id}
ID: {self.id}

''')

    def mostrarAsiento(self):
            rows = len(self.seats)
            columns = len(self.seats[0])
            print(f'''               GAME: {self.home_team} vs. {self.away_team}''')
            print(f'''               DATE: {self.date}
STADIUM: {self.stadium}''')
            
            print('___________________________________________________________')
            for column in range(columns):
                for row in range(rows):
                    if row == 0:
                        print('|', end= '')
                    print('T' if self.seats[(row)][(column)]== "O" else "A", end= " ")
                    if row == rows -1:
                        print('''|''')
            print('''              T: TAKEN , A: AVAILABLE.\n''')
            print('___________________________________________________________')

    

    

            