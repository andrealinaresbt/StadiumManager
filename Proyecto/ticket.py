class Ticket:
    tickets = []
    def __init__(self, code, row, column, game, stadium, ticket_type):
        self.code =code
        self.row = row
        self.column = column
        self.game = game
        self.stadium =stadium
        self.ticket_type = ticket_type
        