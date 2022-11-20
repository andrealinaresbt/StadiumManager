from cliente import Client

class General(Client):
    def __init__(self, name, id, age, game, ticket,pric):
        super().__init__(name, id, age, game, ticket)