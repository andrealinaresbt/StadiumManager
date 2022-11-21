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
import random

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
def viewSeats(stadiums):
    for stadium in Stadium.estadio:
        stadium.mostrarAsiento()
            #MENUS
def viewMenus(stadiums):
    for product in Product.productos:
        product.mostrar()

def invoice(clientName, clientID, pickSeat, ticket,ticketType, descuento, ticketprecio, total, clientGame, games):
    print(f'''
****************** INVOICE ******************
CLIENT NAME: {clientName}
CLIENT ID: {clientID}
SEAT: {pickSeat}
TYPE OF TICKET: {ticketType}
CODE: {ticket}
DISCOUNT: {descuento}
PRECIO IVA: {ticketprecio}
TOTAL:{total}''')
    for game in games:
        if str(clientGame) == game['id']:
            print('GAME:', game['home_team'], 'vs.', game['away_team'] )
            print('____________________________________')
#FUNCIONES DE BUSQUEDA
            #SEARCH BY TEAM
def searchTeam(teams, games, country_name, stadiums):
   for game in games:
        for stadium in stadiums:
            if country_name == game['home_team'].upper() or country_name == game['away_team'].upper():
                if game['stadium_id'] == stadium['id']:
              
                 print(f'''HOME TEAM: {game['home_team']}
AWAY TEAM: {game['away_team']}
DATE: {game['date']}
STADIUM: {stadium['name']}
ID: { game['id']}

''')
            #SEARCH BY STADIUM
def searchStadiums(games, stadiums, stadium_ID):
    for game in games:
        for stadium in stadiums:
            if stadium_ID == game['stadium_id']:
                if stadium['id'] == game['stadium_id']:
                    print(f'''HOME TEAM: {game['home_team']}
AWAY TEAM: {game['away_team']}
DATE: {game['date']}
STADIUM: {stadium['name']}
ID: { game['id']}

''')
            #SEARCH BY DATE OF GAME
def searchDate(games, dateSearch, dias, stadiums):
    for game in games:
        for stadium in stadiums:
            if dateSearch in game['date'].split(' '):
                if stadium['id'] == game['stadium_id']:
                    print(f'''HOME TEAM: {game['home_team']}
AWAY TEAM: {game['away_team']}
DATE: {game['date']}
STADIUM: {stadium['name']}
ID: { game['id']}

''')

            #SEARCH BY NAME OF PRODUCT
def searchProduct(restaurantList ,product_name):
    for restaurant in restaurantList:
        for product in restaurant['products']:
            if product_name == product['name'].upper():
                
                         print(f'***{restaurant["name"]}***')
                         print(f'''Name ---> {product["name"]}
 Price (IVA) ---> {product["price"]*0.14 + product["price"]}''')
                         if product['type'] == 'beverages':
                             if product['name'] == 'Beer':
                                 print('TYPE: Alcohol\n')
                             else:
                                 print('TYPE: No-Alcohol\n')
                         elif product['type'] == 'food':
                             if product['name'] == 'Fish and Chips':
                                 print('TYPE: Packaged\n')
                             else:
                                 print('TYPE: Prepared\n')
            #SEARCH BY TYPE OF PRODUCT
def searchTypeProduct(restaurantList, product_type):
    for restaurant in restaurantList:
        for product in restaurant['products']:
            if product_type == product['type']:
                print(f'***{restaurant["name"]}***')
                print(f'''Name ---> {product["name"]}
 Price (IVA) ---> {product["price"]*0.14 + product["price"]}''')
                if product['type'] == 'beverages':
                             if product['name'] == 'Beer':
                                 print('TYPE: Alcohol\n')
                             else:
                                 print('TYPE: No-Alcohol\n')
                elif product['type'] == 'food':
                    if product['name'] == 'Fish and Chips':
                        print('TYPE: Packaged\n')
                    else:
                        print('TYPE: Prepared\n')
            #SEARCH BY RANGE OF PRICE
def searchPriceRange(restaurantList, lowerNum, higherNum):
    for restaurant in restaurantList:
        for product in restaurant['products']:
            if product['price'] > lowerNum and product['price'] < higherNum:
                print(f'***{restaurant["name"]}***')
                print(f'''Name ---> {product["name"]}
 Price (IVA) ---> {product["price"]*0.14 + product["price"]}''')
                if product['type'] == 'beverages':
                             if product['name'] == 'Beer':
                                 print('TYPE: Alcohol\n')
                             else:
                                 print('TYPE: No-Alcohol\n')
                elif product['type'] == 'food':
                    if product['name'] == 'Fish and Chips':
                        print('TYPE: Packaged\n')
                    else:
                        print('TYPE: Prepared\n')
            
def processPurchase(pickSeat, clientTicket, ticketIDGen, ticketsIDVIP, clientName, clientID, clientAge, clientGame):
    while True:
        #viewSeats(stadium) 
        buyConfirm = input('Do you confirm your purchase? Y-Yes N-No: ').upper()
        if buyConfirm.isnumeric() == True:
            print('This is not an accepted value, its either Y or N. Not a number.')
        elif buyConfirm == 'Y' or buyConfirm == "N":
            if buyConfirm == 'Y':
                if clientTicket == 'GENERAL':
                    clientTicketCode = random.randint(1000,4000)
                    ticketIDGen.append(clientTicketCode)
                    Client.clients.append(General(clientName, clientID, clientAge,clientGame, pickSeat, clientTicket,  clientTicketCode ))
                    return clientTicketCode
                    
                if clientTicket == 'VIP':
                    clientTicketCode = random.randint(1000,4000)
                    ticketsIDVIP.append(clientTicketCode)
                    Client.clients.append(VIP(clientName, clientID, clientAge,clientGame, pickSeat, clientTicket,  clientTicketCode))
                    return clientTicketCode

def getDescuento(cedula):
    pass

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
    descuento = 0
    ticketsUsados = []
    cedulaVIPs= []


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
                                Product.productos.append(Bebida(restaurant['name'], product['name'], product['price'], product['name']))
                            elif product['type'] == "food":
                                Product.productos.append(Food(restaurant['name'], product['name'], product['price'], product['name']))                   
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
                game['date'], stadium['name'], game['id']))
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
            #MODULO UNO, AQUI ENCONTRARAS LAS FUNCIONES BASICAS DE LOS PARTIDOS 
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
                                viewTeams(teams)
                                while True:

                                    country_name = (input("Please enter the name of the country you wish to see the games of: ")).upper()
                                    if country_name.isnumeric() == True:
                                        print('This is not a valid option. Please enter a name and not a number.')
                                    elif  country_name not in equipos_name:
                                        print('Youre a loser! your team does not play in the world cup')
                                    else:
                                        print('____________________\n')
                                        print('THE GAMES BEING PLAYED BY THIS COUNTRY ARE:')
                                        searchTeam(teams, games, country_name, stadiums)
                                        print('____________________')
                                        break

                                #BUSQUEDA POR ESTADIO
                            elif searchPath == 2:
                                viewStadium(stadiums)
                                while True:
                                    stadium_ID = int((input("Please enter the ID of the stadium you wish to see the games being played of: ")))
                                    if stadium_ID > len(Stadium.estadio) or stadium_ID <= 0:
                                            print('This is not an available stadium. Please enter a valid ID.')
                                    else:
                                            print('____________________\n')
                                            print('THE GAMES BEING PLAYED IN THIS STADIUM ARE:')
                                            searchStadiums(games, stadiums, stadium_ID)
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
                                            searchDate(games, dateSearch, dias, stadiums)
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
                        clientName = input('Please enter your name: ')
                        #VALIDACION
                        if clientName.isalpha() == True:
                            break
                               
                        else:
                            print('Please enter a valid name. This is a numeric value.')
                        
                        #ID
                    while True:
                        clientID = (input('Please enter your ID: '))
                        if clientID.isnumeric() == True:
                            break
                        else:
                            print('Please enter a valid value')

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
                                                    cedulaVIPs.append(clientID)
                                                    pickSeat = int(input('Please pick a seat: '))
                                                    ticket = processPurchase(pickSeat,clientTicket, ticketIDGen, ticketsIDVIP, clientName, clientID, clientAge, clientGame)
                                                    ticketIVA = 120+(120*0.16)
                                                    total = ticketIVA - descuento
                                                
                                                    invoice(clientName, clientID, pickSeat, ticket, 
                                                    clientTicket, descuento, ticketIVA, total, clientGame, games)
                                                    break
                           
                                                
                                                elif clientTicket == 2:
                                                    clientTicket = 'GENERAL'
                                                    pickSeat = int(input('Please pick a seat: '))
                                                    ticket = processPurchase(pickSeat,clientTicket, ticketIDGen, ticketsIDVIP,
                                                     clientName, clientID, clientAge, clientGame)
                                                    ticketIVA = 50+(50*0.16)
                                                    total = ticketIVA - descuento
                                                    invoice(clientName, clientID, pickSeat, ticket, 
                                                    clientTicket, descuento, ticketIVA, total, clientGame, games)
                                                    break
                                            
               
                                            else:
                                                print('This is not an available option. Try again')
                                            
                                        else:
                                            print("This was not an accepted value try again.")
                                
                            else:
                                    print('This ticket isnt available')

                            break
                        else:
                            print('This is not an ID.')           
                            
                    break  
                #FALTA MOSTRAR LA ENTRADA AL PARTIDO
            elif mainPath == 3:
                while True:
                    gameID = int(input('Please enter the game ID of the game your attending: '))
                    if str(gameID) in gamesID:
                        verifyTicket = int(input('Please enter your ticket code: '))
                        if verifyTicket not in ticketsUsados:
                            if verifyTicket in ticketsIDVIP or verifyTicket in ticketIDGen:
                                ticketsUsados.append(verifyTicket)
                                print('Welcome!')

                                break
                            else:
                                print('Your code is fake\n')
                        else:
                            print('Someone already used this ticket\n')
                    else:
                        print('This game does not exist. \n')
                    

              
                #MODULO 3, GESTION DE RESTAURANTES Y BUSQUEDA DE PRODUCTOS
            elif mainPath == 4:
                
                pathRestaurants = int(input('''What would you like to do?
1. See all the menus.
2. Make a search. '''))

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
              
            elif mainPath == 7:
                goodbye()
                break

            else:
                print('Please enter a valid value.')

        except Exception as e:
            print('___________________________\n')
            print('ERROR:', e)
            print("Sorry! Something went wrong, please try again.")
            print('___________________________')


main()