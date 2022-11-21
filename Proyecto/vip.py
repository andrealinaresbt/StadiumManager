from cliente import Client

class VIP(Client):
    def __init__(self, name, id, age, game, seat, ticket, confirmation):
        super().__init__(name, id, age, game, seat, ticket)
        self.confirmation = confirmation
        
    def mostrarClient(self):
        super().mostrarClient()
        print(f'CONFIRMATION CODE: {self.confirmation}')
