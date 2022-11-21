class Client:
    clients = []
    client =[]
    def __init__(self, name, id, age, game, seat, ticket):
        self.name = name
        self.id = id
        self.age = age
        self.game = game
        self.seat =seat
        self.ticket = ticket
        

    
    def mostrarClient(self):
        print(f'''*****************RECEIP********************
NAME: {self.name}
ID: {self.id}
SEAT: {self.seat}
GAME: {self.game}
TICKET: {self.ticket}
''')