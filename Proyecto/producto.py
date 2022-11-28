class Product:
    productos =[]
    def __init__(self, restaurant, stadium_id, name, quantity, price,type, additional):
        self.restaurant = restaurant
        self.stadium_id = stadium_id
        self.name = name
        self.quantity =quantity
        self.price = price*0.16 + price
        self.type = type
        self.additional = additional


    def mostrar(self):
        
        print (f'''Name ---> {self.name}
Price (IVA) ---> {self.price}
Stock: {self.quantity}
Type: {self.type}
    Additional: {self.additional}
    ''')

    def mostrarFactura(self):
         print (f'''Name ---> {self.name}
Price (IVA) ---> {self.price}
Stock: {self.quantity}
Type: {self.type}
    Additional: {self.additional}
    ''')

