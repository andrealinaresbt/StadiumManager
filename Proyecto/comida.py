from producto import Product
class Food(Product):
    def __init__(self, restaurant, name, price, type):
        super().__init__(restaurant, name, price)
        if self.name == "Fish and Chips":
            self.type = 'Packaged'
        else:
            self.type = 'Prepared'
    def mostrar(self):
        super().mostrar()
        print(f'TYPE: {self.type}\n')
        