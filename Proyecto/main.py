#IMPORTS
import requests
import json
from equipos import Equipos 
from estadios import Stadium
from partidos import Games
from producto import Product
from vip import VIP
from general import General
from cliente import Client
from bebida import Bebida
from comida import Food
from ticket import Ticket
import random
from collections import Counter
import math

#FUNCIONES DE MOSTRAR
           
            #EQUIPOS

def viewTeams(teams):
    for equipos in Equipos.equipos:
        print(equipos.mostrarEquipo())
          
            #ESTADIOS

def viewStadium( stadiums):
    for stadium in Stadium.estadio:
        stadium.mostrarStadiums()
           
            #JUEGOS

def viewGames(games):
    for game in Games.partidos:
        print(game.mostrarGames())
            
            #ASIENTOS
def viewSeats(clientGame):
    searchedSeat =[]
    for game in Games.partidos:
            if clientGame in [game.id]:
                
                searchedSeat.append(game)
    for game in searchedSeat:
        for stadium in Stadium.estadio:
            if clientGame == game.id:
                if game.stadium_id == stadium.id:
                
                    row_seat, column_seat = stadium.mostrarAsiento()
                
                    return row_seat, column_seat

            #MENUS
def viewMenus(stadiums):
    for product in Product.productos:
        print('______________________')
        print('        MENU          ')
        print(product.restaurant)
        product.mostrar()
        print('______________________')


#FUNCIONES DE BUSQUEDA

            #SEARCH BY TEAM
def searchTeam(country_name):
   searchedMatch=[]
   for game in Games.partidos:
            if country_name.upper() in [game.home_team.upper()] or country_name in [game.away_team.upper()]:
                searchedMatch.append(game)

   if len(searchedMatch) == 0:
        print(f'The team {country_name} is not on the world cup')

   else:
        print(f"\n{country_name}'s matches in the world cup 2022 are: ")

        for game in searchedMatch:
            print(f'''HOME TEAM: {game.home_team}
AWAY TEAM: {game.away_team}
DATE: {game.date}
ID: {game.id}
STADIUM: {game.stadium} 
ID STADIUM: {game.stadium_id}
''')
             
            #SEARCH BY STADIUM

def searchStadiums(stadium_ID):
    searchedStadium =[]
    for game in Games.partidos:
            if stadium_ID in [game.stadium_id]:
                
                    searchedStadium.append(game)

    if len(searchedStadium) != 0:
        print(f"\nThe games being played at this stadium are: ")
        for game in searchedStadium:
             print(f'''HOME TEAM: {game.home_team}
AWAY TEAM: {game.away_team}
DATE: {game.date}
ID: {game.id}
STADIUM: {game.stadium} 
ID STADIUM: {game.stadium_id}
''')
           
            #SEARCH BY DATE OF GAME

def searchDate(dateSearch):
    searchedDate =[]

    for game in Games.partidos:
            if dateSearch in game.date.split(' '):
                searchedDate.append(game)
            
    if len(searchedDate) != 0:
        print(f"\nThe games being played in this date are: ")
        for game in searchedDate:
            print(f'''HOME TEAM: {game.home_team}
AWAY TEAM: {game.away_team}
DATE: {game.date}
ID: {game.id}
STADIUM: {game.stadium} 
ID STADIUM: {game.stadium_id}
''')

    else:
        print('This is not an available date.')

            #SEARCH BY NAME OF PRODUCT

def searchProduct(restaurantList ,product_name):
    for product in Product.productos:
        if product_name in product.name.upper():
            if product_name == product.name.upper():
                print(f'***********{product.restaurant}***********')
                product.mostrar()
    
                    
                            
          
            #SEARCH BY TYPE OF PRODUCT

def searchTypeProduct(restaurantList, product_type):
    for product in Product.productos:
            if product_type in product.type:
                if product_type == product_type:
                    print(f'***********{product.restaurant}***********')
                    product.mostrar()
            elif product_type != "beverages" and product_type != "food":
                print("None xd")

            

           
            #SEARCH BY RANGE OF PRICE

def searchPriceRange(restaurantList, lowerNum, higherNum):
    print("IF THERE ARE NO ANSWERS, THEN THERE ARE NO RESTAURANTS THAT SELL BETWEEN THIS RANGE.\n")
    for product in Product.productos:
            if product.price > lowerNum and product.price < higherNum:
                print(f'***********{product.restaurant}***********')
                product.mostrar()
            
            

  #VALIDACION DE CLIENTE VIP PARA INGRESO RESTAURANTE          
def VIPClientIDValid(clientIDRest, cedulaVIPs):
        if str(clientIDRest) in cedulaVIPs:
            return True
        else:
            return False

#PAGO PROCESO
def processPurchase(pickSeat,clientTicket, ticketIDGen, ticketsIDVIP, clientName, clientID, clientAge, clientGame, cedulaVIPs, discountpercentage):
    seat_available = False
    seat = None
    game_pick = -1
    while not seat_available:
        for id, game in enumerate(Games.partidos):
            if game.id == clientGame:
                game_pick = id
                break
        if game_pick >=0:
            break
    for game in Games.partidos:
        if game.id == clientGame:
            seat = game.capacity


    print('Please select your seat. You need to input the coordinate of the seat by row and column.')
    Games.partidos[game_pick].mostrarAsiento()
    while True:
        print(' ')
        seat_row = (input('SEAT: '))
        column_row = (input('ROW: '))
        if seat_row.isnumeric() and column_row.isnumeric():
            seat_row= int(seat_row) - 1
            column_row = int(column_row) - 1
        
            if seat_row > seat[0] or seat_row < 0: 
                print("Please enter a valid seat")
            if column_row > seat[1] or column_row < 0:
                print("Please enter a valid seat")
            else:
                break
        else:
            print('THIS IS NOT A NUMERIC VALUE.')
    if Games.partidos[game_pick].seats[seat_row][column_row] == "O":
        print(f'SEAT {seat_row},{column_row} IS NOT AVAILABLE, SORRY. \n')
    else:
        seat_available = True

    if seat_available:
        discount = 0
        if clientTicket == 'GENERAL':
            clientTicketCode = random.randint(1000,4000)
            
            ticket_price = 50
            ticketIVA = ticket_price+(ticket_price*0.16)
            if discountpercentage == []:
                discount = 0
            else: 
                discount = 0.50
            descuentoTicket = discount*ticketIVA
            total = ticketIVA - descuentoTicket

            
            for game in Games.partidos:
                if clientGame == game.id:
                    pickSeat.append(seat_row)
                    pickSeat.append(column_row)
                    resume(clientName, clientID, seat_row, column_row, clientTicketCode, 
            clientTicket, descuentoTicket, ticketIVA, total, clientGame, game)
                    path = input('Do you confirm your purchase? Y-Yes. N-No: ').upper()
                    if path == 'Y':
                        ticketIDGen.append(clientTicketCode)
                        Ticket.tickets.append(Ticket(clientTicketCode, seat_row, column_row, clientGame, game.stadium_id, 'GENERAL' ))
                        Client.clients.append(General(clientName, clientID, clientAge, clientGame,  game.stadium_id, game.stadium, seat_row, column_row, clientTicket,  'Inasistente', clientTicketCode, total))
                        invoice(clientName, clientID, seat_row, column_row, clientTicketCode, 
            clientTicket, descuentoTicket, ticketIVA, total, clientGame, game)
                        Games.partidos[game_pick].seats[seat_row][column_row] ="O"
                        Games.partidos[game_pick].ticketsSold.append(Ticket.tickets)
                        for game in Games.partidos:
                            if game.id == clientGame: 
                                game.tickets_Sold += 1
                        break

                    elif path == 'N':
                        return 'CANCELLED'
                    
                    else:
                        print("THIS IS NOT AN ACCEPTED VALUE.")

        if clientTicket == 'VIP':
            clientTicketCode = random.randint(1000,4000)
            
            ticket_price = 120
            ticketIVA = ticket_price+(ticket_price*0.16)
            if discountpercentage == []:
                discount = 0
            else: 
                discount = 0.50
            descuentoTicket = discount*ticketIVA
            total = ticketIVA - descuentoTicket

            for game in Games.partidos:
                
                        if clientGame == game.id:
                            pickSeat.append(seat_row)
                            pickSeat.append(column_row)
                            resume(clientName, clientID, seat_row, column_row, clientTicketCode, 
                    clientTicket, descuentoTicket, ticketIVA, total, clientGame, game)
                            path = input('Do you confirm your purchase? Y-Yes. N-No: ').upper()
                            if path == 'Y':
                                
                                        ticketsIDVIP.append(clientTicketCode)
                                        Ticket.tickets.append(Ticket(clientTicketCode, seat_row, column_row, clientGame, game.stadium_id, 'GENERAL' ))
                                        Client.clients.append(VIP(clientName, clientID, clientAge, clientGame,  game.stadium_id, game.stadium, seat_row, column_row, clientTicket,  "Inasistente" , clientTicketCode, total))
                                        invoice(clientName, clientID, seat_row, column_row, clientTicketCode, 
                            clientTicket, descuentoTicket, ticketIVA, total, clientGame, game)
                                        cedulaVIPs.append(clientID)
                                        Games.partidos[game_pick].seats[seat_row][column_row] ="O"
                                        Games.partidos[game_pick].ticketsSold.append(Ticket.tickets)
                                        for game in Games.partidos:
                                            if game.id == clientGame: 
                                                game.tickets_Sold += 1 
                                        break

                            elif path == 'N':
                                return 'CANCELLED'
                            
                            else:
                                print("THIS IS NOT AN ACCEPTED VALUE.")

#VALIDACION DE VAMPIRO 
def valid(a, b):
     if len(a) != len(b):
        
        return False
     
     return Counter(a) == Counter(b)

#FACTURAS Y VARIOS
         
def invoice(clientName, clientID, seat_row, column_row, ticket, clientTicket, descuentoTicket, ticketIVA, total, clientGame, games):
    total = ticketIVA -descuentoTicket
    print(f''' SUCCESFUL PAYMENT!

****************** INVOICE ******************
CLIENT NAME: {clientName}
CLIENT ID: {clientID}
SEAT: ROW ----> {seat_row}, COLUMN ----> {column_row}
TYPE OF TICKET: {clientTicket}
CODE: {ticket}
DISCOUNT: {descuentoTicket}
PRECIO IVA: {ticketIVA}
TOTAL:{total}''')
    print('GAME: ', games.home_team, 'vs.', games.away_team)
    print('STADIUM:', games.stadium)
    print('DATE:', games.date)
    
    print('____________________________________')

def resume(clientName, clientID, seat_row, column_row, ticket, clientTicket, descuentoTicket, ticketIVA, total, clientGame, games):
    total = ticketIVA -descuentoTicket
    print(f'''
-------------------- RESUME ------------------
CLIENT NAME: {clientName}
CLIENT ID: {clientID}
SEAT: ROW ----> {seat_row}, COLUMN ----> {column_row}
TYPE OF TICKET: {clientTicket}
CODE: {ticket}
DISCOUNT: {descuentoTicket}
PRECIO IVA: {ticketIVA}
TOTAL:{total}''')   
    print('GAME: ', games.home_team, 'vs.', games.away_team)
    print('STADIUM:', games.stadium)
    print('DATE:', games.date)
    
    print('____________________________________')


def invoiceProduct(purchased_items,product_buyBrute, discountPrice, totalBuy):
    print('________________________________________________')
    for product in purchased_items:
        product.mostrarFactura()
    print(f'''TOTAL BRUTE: {product_buyBrute}
DISCOUNT: {discountPrice}

TOTAL: {totalBuy}
________________________________________________''')
    


def getPerfect(clientIDRest):
    aux = clientIDRest -1 
    acum = 0
    list=[]
    
    while aux >= 1:
        if clientIDRest % aux == 0:
            acum += aux
            list.append(aux)

        aux -= 1
    if sum(list) == clientIDRest:
        return 0.15
    else:
        return 0

def sort(list):
    if len(list) > 1:
        middle_p = len(list)//2
        
        left = list[:middle_p]
        right = list[middle_p:]

        sort(left)
        sort(right)
        merge(list,left, right, middle_p)
        
        return list

def merge(asistencia_list,left,right, middle_p):
    i=0
    j=0
    m=0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            asistencia_list[m] = left[i]
            i += 1
        else:
            asistencia_list[m] = right[j]
            j+=1
        m+=1

    while i < len(left):
            asistencia_list[m] = left[i]
            i += 1
            m += 1
 
    while j < len(right):
            asistencia_list[m] = right[j]
            j += 1
            m += 1    

#FUNCIONES DE ESTETICA QUE HACEN QUE SE VEA MAS AMIGABLE EL CODIGO
def welcome():
    print("""_____________________

WELCOME TO THE WORLD CUP 2022 MENU 
_____________________
""")

def goodbye():
    print('')
    print('THANK YOU FOR COMING. I HOPE YOU ENJOY THE WORLD CUP.\n')

def main():
    equipos_name =[]
    dias = []
    gamesID = []
    productStock = []
    restaurantList = []
    ticketIDGen = []
    ticketsIDVIP = []
    discountpercentage = []
    ticketsUsados = []
    cedulaVIPs= []
    pickSeat = []
    purchased_items =[]
    clientVIP = []
    tickets_list = []
    product_list = []

    #BUSQUEDA DE INFORMACION DE LAS APIS
    url_equipos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/teams.json"
    url_estadios = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/stadiums.json"
    url_partidos = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-1/api-proyecto/main/matches.json" 
     
    #PAGE RESPONSES [200,202,404, ...]
    response_equipos = requests.get(url_equipos)
    response_estadios = requests.get(url_estadios)
    response_partidos = requests.get(url_partidos)

    #JSON FILES 
    if response_partidos.status_code == 200:
        games = response_partidos.json()
    if response_estadios.status_code == 200:
        stadiums = response_estadios.json()
    if response_partidos.status_code == 200:
        teams = response_equipos.json()

    #CREACION DE LISTA DE OBJETOS
        #EQUIPOS
    for team in teams:
        Equipos.equipos.append(Equipos(team['name'], team['flag'], 
        team['fifa_code'], team['group'], team['id']))
            #SOLO NOMBRES
    for team in teams:
        equipos_name.append(team['name'].upper())
        #ESTADIOS
    
    for stadium in stadiums:
        
        Stadium.estadio.append(Stadium(stadium['id'], stadium['name'],
        stadium['capacity'], stadium['location'], stadium['restaurants']))
        #PRODUCTOS 
    for stadium in stadiums:
                    for restaurant in stadium['restaurants']:
                        for product in restaurant['products']:
                            if product['type'] == "beverages":
                                Product.productos.append(Bebida(restaurant['name'], stadium['id'], product['name'], product['quantity'], product['price'], product['type'], product['adicional']))
                            elif product['type'] == "food":
                                Product.productos.append(Food(restaurant['name'], stadium['id'], product['name'], product['quantity'], product['price'], product['type'], product['adicional']))                   
        #AVAILABLE PRODUCTS
    
    for stadium in stadiums:
        for restaurant in stadium['restaurants']:
            restaurantList.append(restaurant)

    for stadium in stadiums:
        for restaurant in stadium['restaurants']:
                for menu in restaurant['products']:
                    productStock.append(menu['name'].upper())
        #JUEGOS
    for game in games:
        for stadium in stadiums:
            if game['stadium_id'] == stadium['id']:
                Games.partidos.append(Games(game['home_team'], game['away_team'],
                game['date'], game['stadium_id'], stadium['name'], stadium['capacity'], game['id'], 0,0))
            #IDS  
    for game in games:
        gamesID.append(game['id'])

    welcome()
    while True:
      
        try:
            mainPath = int(input('''What can we do for you today?
1. Games and Stadium management.
2. Tickets management.
3. Attendance management.
4. Restaurant management.
5. Restaurant sales manegement.
6. End of the day.
7. Exit
----> '''))
              #MODULO 1, AQUI ENCONTRARAS LAS FUNCIONES BASICAS DE LOS PARTIDOS 
            if mainPath == 1:
                while True:
                    secondPath = int(input('''What would you like to do?
1. View Categories.
2. Make a Search.
-----> '''))
                        #MUESTRA DE DATOS
                    if secondPath == 1:
                        while True:
                            showPath = int(input('''What category would you like to see?
    1. View teams.
    2. View games.
    3. View stadiums.
    ----> ''' ))
                            
                              #MUESTRA EQUIPOS
                            if showPath == 1:
                                viewTeams(teams)
                                break

                                #MUESTRA JUEGOS
                            elif showPath == 2:
                                viewGames(games)
                                break
                            
                                #MUESTRA ESTADIOS
                            elif showPath == 3:
                                viewStadium(stadiums)
                                break
                        
                        #BUSQUEDA
                    elif secondPath == 2:
                        while True:
                            searchPath = int(input('''What type of search would you like to do?
    1. All the games by country.
    2. All the games by stadium.
    3. All the games by date. 
    4. Return.
    ---> '''))
                                #BUSQUEDA POR PAIS
                            if searchPath == 1:
                                while True:

                                    country_name = (input("Please enter the name of the country you wish to see the games of: ")).upper()
                                    if country_name.isnumeric() == True:
                                        print('This is not a valid option. Please enter a name and not a number.')
                                    elif  country_name not in equipos_name:
                                        print('Youre a loser! your team does not play in the world cup')
                                    else:
                                        print('____________________')
                                        searchTeam(country_name)
                                        print('____________________')
                                        break

                                #BUSQUEDA POR ESTADIO
                            elif searchPath == 2:
                                while True:
                                    stadium_ID = int((input("Please enter the ID of the stadium you wish to see the games being played of: ")))
                                    if stadium_ID > len(Stadium.estadio) or stadium_ID <= 0:
                                            print('This is not an available stadium. Please enter a valid ID.')
                                    else:
                                            print('____________________\n')
                                            print('THE GAMES BEING PLAYED IN THIS STADIUM ARE:')
                                            searchStadiums(stadium_ID)
                                            print('____________________')
                                            break
                                
                                #BUSQUEDA POR DIA
                            elif searchPath == 3:
                                for game in games:
                                    gameDate = game['date'].split(' ')
                                    dias.append(gameDate[0])

                                while True:
                                    dateSearch = input('Please enter the date you wish to search MM/DD/YYYY: ')
                                    if dateSearch.isalpha() == True:
                                        print('This is not an accepted value. Dont write it with aplphabetic letters.')
                                    elif dateSearch.isalpha() == False:
                                        if dateSearch in dias:
                                            print('____________________\n')
                                            print('THE GAMES BEING PLAYED THIS DAY ARE: \n')
                                            searchDate(dateSearch)
                                            print('____________________')
                                            break
                                        else:
                                            print('This game doesnt exist')
                                        break
                                    else:
                                            print('This is not an acepted value, try again')

                                    break
                                #RETURN
                            elif searchPath == 4:
                                break

                            else:
                                print('This is not an acepted value. Try again.')     
                
                    break


                #MODULO 2, REGISTRO DE VENTA DE ENTRADAS <<< NOT FINISHED >>> FALTA MUESTRA DE ASIENTOS Y DESCUENTO  
            elif mainPath == 2:
                while True:
                    #DATOS DEL CLIENTE
                            #NAME
                    while True:
                        clientName = input('Please enter your name: ').capitalize()
                        #VALIDACION
                        if clientName.isnumeric() == True:
                            print('Please enter a valid name. This is a numeric value.')
                        else:
                            break
                            
                        
                        #ID
                    while True:
                        clientID = ((input('Please enter your ID: ')))
                        if clientID.isnumeric() == True:
                            if len(clientID) %2 == 0:
                                
                                for x in range(0,int(math.pow(10, len(str(clientID))/2))):
                                    
                                    for y in range(0,int(math.pow(10, len(str(clientID))/2))):
                                        if (x*y == int(clientID)):
                                            if (valid(str(str(x)+''+str(y)), str(clientID))):
                                                discountpercentage.append(0.50)
                                                    
                                        else:
                                            pass
                            elif len(clientID) %2 != 0:
                                discountpercentage = []
                                pass
                                        
                                            
                            
                                            
        
                                
                            break

                        else:
                            print('Please enter a valid value')
                    
                    
                    if discountpercentage == []:
                        pass
                    elif discountpercentage[0] == 0.50:
                        print("CONGRATS! YOU GOT A 50% OFF")
                         #AGE
                    while True:
                        clientAge =(input('Please enter your age: '))
                        '''AQUI SE QUIERE BUSCAR SI EL CLIENTE ES O NO MAYOR
                        DE EDAD'''
                        if clientAge.isnumeric() == True:
                            clientAge =int(clientAge)
                            if clientAge >= 18:
                                bebidaAlcohol = "Yes"
                                break
                            else:
                                bebidaAlcohol = "No"
                                break
                        else:
                            print('Please enter a valid value')
                    #COMPRA DE TICKET
                    viewGames(games)
                    while True:
                        clientGame = (input('Please enter the ID of the match you wish to see: '))
                        if clientGame.isnumeric() == True:
                            if clientGame in gamesID:
                                    while True:
                                        print(''' 
    _____________________

    There are two types of tickets:
    THE VIP TICKETS: You have unlimited access to the restaurants. Price --> 120$
    THE GENERAL TICKETS: You can only watch the games from the comfort of your seat. Price --> 50$

    _____________________
    ''')
                                        clientTicket = (input("""Please select the type of ticket you wish to buy:
                    1. VIP.
                    2. GENERAL.
                    ----->  """))       
                                        if clientTicket.isnumeric() == True:
                                            clientTicket = int(clientTicket)
                                            if clientTicket == 1 or clientTicket ==2:
                                                if clientTicket ==1:
                                                    clientTicket = 'VIP'

                                                    processPurchase(pickSeat,clientTicket, ticketIDGen, ticketsIDVIP, clientName,
                                                     clientID, clientAge, clientGame, cedulaVIPs, discountpercentage)
                                                if clientTicket ==2:
                                                    clientTicket = 'GENERAL'

                                                    processPurchase(pickSeat,clientTicket, ticketIDGen, ticketsIDVIP, clientName,
                                                     clientID, clientAge, clientGame, cedulaVIPs, discountpercentage)
                                                    break
                                   
                                                else:
                                                    print('')
                                                    break
                                            break
                                        break
                                    break
                            break
                        break
                    break
    
                #MODULO 3, MUESTRA Y REGISTRA LA ENTRADA A LOS PARTIDOS.
            elif mainPath == 3:
                while True:
                        verifyTicket = int(input('Please enter your ticket code: '))
                        if verifyTicket not in ticketsUsados:
                            if verifyTicket in ticketsIDVIP or verifyTicket in ticketIDGen:
                                ticketsUsados.append(verifyTicket)
                                for client in Client.clients:
                                    if verifyTicket == client.confirmation:
                                        print(f'''
Welcome to the {client.stadium} stadium! ''')
                                        client.asistencia = "Asistente"
                                        client.mostrarClient()
                                        print('______________________________________')
                                        
                                        for game in Games.partidos:
                                            if game.id == client.game: 
                                                game.attendance += 1

                                break
                            else:
                                print('Your code is fake\n')
                                break
                        else:
                            print('Someone already used this ticket\n')
                            break
            
                #MODULO 4, GESTION DE RESTAURANTES Y BUSQUEDA DE PRODUCTOS
            elif mainPath == 4:
                while True:
                    pathRestaurants = int(input('''What would you like to do?
    1. See all the menus.
    2. Make a search. 
    3. Return. '''))

                    #MENUS DE PRODUCTOS
                    if pathRestaurants == 1:
                        viewMenus(stadium)

                        #BUSQUEDAS DE PRODUCTOS
                    elif pathRestaurants == 2:
                     while True:
                        pathSearchRestaurant = int(input('''What type of search would you like to do?
    1. Search by name.
    2. Search by type.
    3. Search by price range. 
    4. Return
    -----> '''))
                        #BUSQUEDA DE PRODUCTOS POR NOMBRE IE: PEPSI, HAMBURGER, ETC...
                        if pathSearchRestaurant == 1:
                            while True:

                                product_name = (input("Please enter the name of the product you wish to see the information of: ")).upper()
                                if product_name.isnumeric() == True:
                                    print('This is not a valid option. Please enter a name and not a number.')
                                elif  product_name not in productStock:
                                    
                                    print('This product isnt available. You just spent 120 dollars for nothing.')
                                else:
                                    print('____________________\n')
                                    print('THE RESTAURANTS THAT SELL THIS PRODUCT ARE:')
                                    searchProduct (restaurantList, product_name )
                                    print('____________________')
                                    break
                        
                        #BUSQUEDA DE PRODUCTO POR TIPO IE: FOOD O BEVERAGE
                        if pathSearchRestaurant == 2:
                            print('''_________________________
THERE ARE TWO TYPES OF PRODUCTS: FOOD OR BEVERAGES.
''')
                            while True:
                                product_type =  input("Please enter the type of product you wish to see: ").lower()
                                if product_type.isnumeric() == True:
                                    print('This is not a valid option. Please enter a type and not a number.')
                                elif product_type != 'beverages' and product_type != 'food':
                                    print('This product isnt available. You just spent 120 dollars for nothing.')
                                else:
                                    print('____________________\n')
                                    print('THE RESTAURANTS THAT SELL THIS PRODUCT ARE:')
                                    searchTypeProduct(restaurantList, product_type)
                                    print('____________________')
                                    print('_________________________')
                                    break

                        #BUSQUEDA DE PRODUCTO POR PRECIO
                        if pathSearchRestaurant == 3:
                            print('''________________________
FOR THIS SEARCH YOU WILL NEED TO INPUT TWO VALUES, THE FIRST PARAMETER
IS THE START OF THE RANGE, THE SECOND ONE THE LAST ONE. 
''')
                            while True:
                                lowerNum = int(input('Please enter first parameter of your range (lower): '))
                                higherNum = int(input('Please enter the second parameter of your range (higher): '))
                                if lowerNum < 0 or higherNum < 0: 
                                    print("These are not real values, be serious. ")
                            
                                elif lowerNum < higherNum:
                                    if higherNum < 4.5600000000000005:
                                        print('Eres pobre <3 \n')
                                    else:
                                        print('____________________\n')
                                        print('THE RESTAURANTS THAT SELL PRODUCTS IN THIS PRICE RANGE ARE: \n')
                                        searchPriceRange(restaurantList, lowerNum, higherNum)
                                        print('____________________')
                                        print('________________________')
                                    
                                    break
                                
                                else:
                                    print('You literally didnt follow the instructions READ!!!!')
                        
                        #RETURN
                        if pathSearchRestaurant == 4:
                            break
                    
                    elif pathRestaurants == 3:
                        break
                    
                    else:
                            print('Please enter a valid option.')
                    
                        
            elif mainPath == 5:
                print('''___________________________

TO ENTER THIS AREA YOU NEED TO BE A VIP COSTUMER,
PLEASE ENTER YOUR ID. ''')

                clientIDRest = int(input('----> '))
                VIPStatus = VIPClientIDValid(clientIDRest, cedulaVIPs)
                product_menu =[]
                purchased_items = []
                if VIPStatus == True:  
                     print('______________________________________')
                     print('                MENU                  ')
                     
                     for client in Client.clients:
                                    if str(clientIDRest) ==  client.id:
                                        for product in Product.productos:
                                            if client.stadium_id == product.stadium_id:
                                                    product_menu.append(product.name.upper())
                                                    product.mostrar()
                     print('______________________________________')
        

                     while True:
                        
                        pathPurchased = int(input("""What do you want to do?
1. Make a purchase.
2. View purchase.
3. Exit
----> """))
                        
                        if pathPurchased == 1:
        
                                for client in Client.clients:
                                    if str(clientIDRest) ==  client.id:
                                                productBuy = input("Please enter the name of the product you want to buy: ").upper()
                                
                                                if productBuy not in product_menu:
                                                        print("This is not an available product")
                                                else:
                                                        for product in Product.productos:
        
                                                            if productBuy == product.name.upper():
                                                                if client.stadium_id == product.stadium_id:

                                                                    if product.quantity == 0:
                                                                        print("Sorry this product is not available. ")
                                                                        
                                                                    else:
                                                                        if product.additional != "alcoholic":
                                                                            purchased_items.append(product)
                                                                            print(" Added to chart! ")
                                                                            break
                                                                        
                                                            

                                                                        else:
                                                                                if client.age < 18: 
                                                                                    print("You cant buy this.")
                                                                                else:
                                                                                    purchased_items.append(product)
                                                                                    print(" Added to chart! ")     
                                                                                    break                                  
                                                                
                        elif pathPurchased ==2:
                            if len(purchased_items) == 0:
                                print("There are no items.")
                            else:
                                
                                product_brute_list = []
                                discountPerfect = getPerfect(clientIDRest)
                                
                                for product in purchased_items:
                                    product_brute_list.append(product.price)
                                product_buyBrute = sum(product_brute_list)
                                discountPrice =discountPerfect*product_buyBrute
                                totalBuy= product_buyBrute -  discountPrice 
                                print('\n                 RESUME                      ')
                                invoiceProduct(purchased_items,product_buyBrute, discountPrice, totalBuy)

                                finalCall = (input("Would you like to finish you purchase? Y-Yes N-No.")).upper()
                                if finalCall == 'Y':
                                    for product in Product.productos:
                                        for productx in purchased_items:
                                         if product == productx:
                                            product.quantity = product.quantity -1
                                            Product.products_bought +=1

                                    

                                    for client in Client.clients:
                                        if str(clientIDRest) ==  client.id:
                                            print('\nSUCCESSFUL PAY!')
                                            print('********************INVOICE*******************')
                                            print(f'''NAME: {client.name} 
ID: {client.id}

            {product.restaurant}''')
                                            for product in purchased_items:
                                                product.mostrar()
                                            print(f'DISCOUNT: {discountPrice}')
                                            print(f'TOTAL: {totalBuy}\n')
                                            client.clientBuy += totalBuy
                                            break

                                    if finalCall == 'N':
                                        purchased_items = []
                                        break

                                    elif finalCall != 'N' and finalCall != 'Y':
                                        print('This is not an accepted value.')
                                    break

                        elif pathPurchased ==3:
                            break

                        else:
                            print('This is not a valid path. ')

                else:
                    print("Youre not a vip costumer.")
            elif mainPath ==6:
                asistencia_list = []
                clientVIP = []

                if Ticket.tickets != []:
                    
                    for game in Games.partidos:
                        asistencia_list.append(game.attendance)
                        tickets_list.append(game.tickets_Sold)
                    asistencia_list = sort(asistencia_list)
                    tickets_list = sort(tickets_list)
                
                for product in Product.productos:
                    product_list.append(product.quantity)
                
                
                
                product_list = sort(product_list)
                n=1
                
                Games.partidos.sort(key=lambda x: x.attendance, reverse=True)
                while True:
                    path6 =int(input('''
    What would you like to see?
    1. Average VIP spendings.
    2. Best to worst attendance.
    3. Best attendance game.
    4. Best sold game.
    5. Top three most sold items.
    6. Top three clients.
    7. Exit.
    ---->'''))      
                    if path6 == 1:
                        if Ticket.tickets != []:
                           
                            if len(Client.clients) != None:
                                clientVIP = []
                                for client in Client.clients:
                                    
                                    if client.ticket == "VIP":
                                        
                                        clientVIP.append(client.clientBuy)
                                
                                if len(clientVIP)==1:
                                    clientVIP = clientVIP[0]
                                    clientVIPAverage = clientVIP
                                else:
                                    clientVIP = sort(clientVIP)
                                    
                                    clientVIPAverage = sum(clientVIP)/len(clientVIP)
                                print(f'The average VIP client spending is of {clientVIPAverage}')
                                datos = open('datos.txt', 'w')
                                datos.write(f'AVERAGE VIP SPENDING {clientVIPAverage}')
                        else:
                            print("There werent any vip clients")
                    elif path6 ==2:

                        print("THE ORDER FROM MORE TO LESS ASSISTED GAMES: ")
                        for partido in Games.partidos:
                            print(f'[{n}]')
                            print(partido.mostrarGames())
                            print(f'''ASISTENCIA: {partido.attendance}
            BOLETOS VENDIDOS: {partido.tickets_Sold}
            RELACION DE ASISTENCIA: DE {partido.tickets_Sold} FUERON {partido.attendance}''')
                            n+=1

                    elif path6 ==3:
                        if Ticket.tickets != []:
                            for game in Games.partidos:
                                if asistencia_list[-1] == 0:
                                    print("There is no most assisted game. ")
                                elif asistencia_list[-1]==game.attendance:
                                    print(f'The game or games with the most amount of attendance were of {asistencia_list[-1]} and they were: ')
                                    print(game.mostrarGames())
                                    print(f'''ASISTENCIA: {game.attendance}
                BOLETOS VENDIDOS: {game.tickets_Sold}
                RELACION DE ASISTENCIA: DE {game.tickets_Sold} FUERON {game.attendance}''')
                                    datos.write(f'MOSTA ATTENDED GAME: {game.mostrarGames()}\n')
                    elif path6 ==4:  
                            if Ticket.tickets != []:
                                for game in Games.partidos:
                                    if tickets_list[-1] == game.tickets_Sold:
                                        print(f'The game or games with the most amount of tickets sold were of {tickets_list[-1]} and they were: ')
                                        print(game.mostrarGames())
                                        print(f'''ASISTENCIA: {game.attendance}
                    BOLETOS VENDIDOS: {game.tickets_Sold}
                    RELACION DE ASISTENCIA: DE {game.tickets_Sold} FUERON {game.attendance}''')
                                        datos.write(f'MOST SOLD GAME: {game.mostrarGames()}\n')
                            else:
                                print('There wasnt a more attendance game')
                    elif path6 ==5:
                        
                        Product.productos.sort(key=lambda x: x.quantity)
                        if Product.products_bought <3 or Product.products_bought == 0 :
                            print('There werent enough purchases to make top three.')
                            
                        else:
                            print('THE TOP THREE BEST SELLING PRODUCTS ARE: ')
                            for i in Product.productos[0:3]:
                                i.mostrarFactura()
                                datos.write('TOP SELLING: ', i.mostrarFactura())
                    elif path6 ==6:
                        if len(Client.clients) < 3:
                            print('There werent enough clients.')
                        else:
                            print('The top three clients are:')
                            for client in Client.clients[0:3]:
                                client.mostrar()
                
                                datos.write('TOP CLIENTS:', client.mostrar())
                                
                            

                        
                    elif path6 ==7:
                        datos.close()   
                        break






                
                
            elif mainPath == 7:
                goodbye()
                break

            else:
                print('Please enter a valid value.')


        except Exception as e:
            print('_______________________________\n')
            print('___________________________\n')
            print('ERROR:', e)
            print("Sorry! Something went wrong, please try again.")
            
main()