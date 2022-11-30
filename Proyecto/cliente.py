class Client:
    clients = []
    clientBuy =[]
    def __init__(self, name, id, age, game, stadium_id, stadium, seat_row, column_row, ticket, asistencia):
        self.name = name
        self.id = id
        self.age = age
        self.game = game
        self.seat_row = seat_row
        self.column_row = column_row
        self.ticket = ticket
        self.stadium_id = stadium_id
        self.stadium = stadium
        self.asistencia = asistencia
        
        
        

    
    def mostrarClient(self):
        print(f'''
***************** ENTRANCE TICKET ********************
NAME: {self.name}
ID: {self.id}
SEAT: {self.seat_row}, {self.column_row}
GAME: {self.game}
STADIUM: {self.stadium}
TICKET: {self.ticket}
ASISTENCIA: {self.asistencia}''')

    def mostrar(self):
            print(f'''
    NAME: {self.name}
    ID: {self.id}
    SEAT: {self.seat_row}, {self.column_row}
    GAME: {self.game}
    STADIUM: {self.stadium}
    TICKET: {self.ticket}
    ASISTENCIA: {self.asistencia}
    TOTAL SPENT: {self.clientBuy}''')

