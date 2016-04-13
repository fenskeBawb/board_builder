

class Customer:

    def __init__(self, _name, _id, _adrs, _zip, _city, _state):
        self.name = _name
        self.id = _id
        self.boards = []

    def add_board(self, board):
        self.boards = board

