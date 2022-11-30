class Equipos:
    equipos = []

    def __init__(self, name, flag, fifa_code, group, id):
        self.name = name
        self.flag = flag
        self.fifa_code = fifa_code
        self.group =group
        self.id = id

    def mostrarEquipo(self):
        
        return(f'''***** {self.name} *******
FLAG: {self.flag}
FIFA CODE: {self.fifa_code}
GROUP: {self.group}
ID: {self.id}

''')

    



   