class Stadium:
    estadio = []
    seats =[]
    def __init__(self, id, name, capacity, location, restaurants):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.location = location
        self.restaurants = restaurants

    def mostrarStadiums(self):
        print(f'''********{self.name}*********
ID: {self.id}
CAPACITY: {self.capacity}
LOCATION: {self.location}''') 
        for restaurant in self.restaurants:
            print(restaurant)
            print(f"RESTAURANT: {restaurant['name']}\n")

    def mostrarAsiento(self):
        seats = []
        for row in self.capacity[0]:
            fila = []
            for seat in self.capacity[1]:
                fila.append("V")
            seats.append(fila)
        
        print(seats)

    def verMenus(self):
        for restaurant in self.restaurants:
            print(restaurant['name'])
            for menu in restaurant['products']:
                print (f'''
    NAME: {menu['name']}
    PRICE: {menu['price']}''')

        