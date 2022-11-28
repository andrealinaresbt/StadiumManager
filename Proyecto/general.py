from cliente import Client

class General(Client):
   def __init__(self, name, id, age, game, stadium_id, stadium, seat_row, column_row, ticket,  asistence, confirmation):
        super().__init__(name, id, age, game, stadium_id, stadium, seat_row, column_row, ticket, asistence)
        self.confirmation = confirmation

   def mostrarClient(self):
        super().mostrarClient()
        print(f'CONFIRMATION CODE: {self.confirmation}')
    

    