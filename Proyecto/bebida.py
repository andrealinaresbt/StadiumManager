from producto import Product
class Bebida(Product):
    def __init__(self, restaurant, name, price,type):
        super().__init__(restaurant, name, price)
        if self.name == 'Beer':
            self.type = 'Alcohol'
        else:
            self.type = 'Non-Alcohol'

    def mostrar(self):
        super().mostrar()
        print(f'TYPE: {self.type}\n')
           