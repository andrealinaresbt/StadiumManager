from cliente import Client

class VIP(Client):
    def __init__(self, name, id, age, game, ticket, price):
        super().__init__(name, id, age, game, ticket)
        self.price = price
