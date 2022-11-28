from cliente import Client

class VIP(Client):
    totalBuy = []
    def __init__(self, name, id, age, game, stadium_id, stadium, seat_row, column_row, ticket,  asistence, confirmation, clientBuy):
        super().__init__(name, id, age, game, stadium_id, stadium, seat_row, column_row, ticket, asistence)
        self.confirmation = confirmation
        self.clientBuy = clientBuy



    def mostrarClient(self):
        super().mostrarClient()
        print(f'CONFIRMATION CODE: {self.confirmation}')
    
    
