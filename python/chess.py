'''
Chess game design
'''

class Board:
    # Initialize a 8x8 square board
    def __init__(self):
        self.squares = []
        for i in range(8):
            self.squares[i] = []
            for j in range(8):
                self.squares[i].append(None)

    def movepiece(self, piece, position):
        self.squares[position[0], position[1]] = piece

    def initgame(self, p1, p2):
        # move the initial pieces of the players
        # to the appropriate positions on the square
        pass

class Piece:

    def __init__(self, type, player):
        self.type = type
        self.position = None
        self.player = player

    def move(self, board, position):
        board.movepiece(self, position)
        self.position = position

class Player:
    
    def __init__(self, id):
        self.id = id
        # initialize the 16 pieces for the player
        self.pieces = []
        queen = Piece('queen', id)
        king = Piece('king', id)
        rook1 = Piece('rook', id)
        rook2 = Piece('rook', id)
        bishop1 = Piece('bishop', id)
        bishop2 = Piece('bishop', id)
        knight1 = Piece('knight', id)
        knight2 = Piece('knight', id)

        self.pieces.append(queen, king, rook1, rook2,
                           bishop1, bishop2, knight1, knight2)
        pawns = []
        for i in range(8):
            self.pieces.append(Piece('pawn', id))

p1 = Player(1)
p2 = Player(2)
