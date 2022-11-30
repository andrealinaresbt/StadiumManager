class Stadium:
    estadio = []
    seats =[]
    def __init__(self, id, name, capacity, location, restaurant):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.location = location
        self.restaurant = restaurant
       
        self.seats = [[0 for i in range(self.capacity[1])] for _ in range(self.capacity[0])]

    def mostrarStadiums(self):
        print(f'''********{self.name}*********
ID: {self.id}
CAPACITY: {self.capacity}
LOCATION: {self.location}''') 
        for restaurant in self.restaurant:
            print(f"RESTAURANT: {restaurant['name']}\n")

    

    def verMenus(self):
        for restaurant in self.restaurants:
            print(restaurant['name'])
            for menu in restaurant['products']:
                print (f'''
    NAME: {menu['name']}
    PRICE: {menu['price']}''')

        