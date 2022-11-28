from producto import Product
class Bebida(Product):
    def __init__(self, restaurant, stadium_id, name, quantity, price, type, additional):
        super().__init__(restaurant, stadium_id, name, quantity, price, type, additional)

    def mostrar(self):
        return super().mostrar()
           