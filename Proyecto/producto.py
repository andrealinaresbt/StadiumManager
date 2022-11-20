class Product:
    productos =[]
    def __init__(self, restaurant, name, price):
        self.restaurant = restaurant
        self.name = name
        self.price = price*0.16 + price

    def mostrar(self):
        print(f'***{self.restaurant}***')
        print (f'''Name ---> {self.name}
Price (IVA) ---> {self.price}''')
