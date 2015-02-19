'''
Simulate a snake and ladder game
'''
import random

class Square:

    def __init__(self, value):
        self.value = value
        # either a snake or a ladder
        # by default it's a isolated node
        self.moveto = None

class Board:

    def __init__(self, num_squares):
        self.current_pos = None
        self.squares = [1000]
        for i in range(1, num_squares+1):
            s = Square(i)
            self.squares.append(s)

    def setup_snake_ladder(self, edges):
        for e in edges:
            self.squares[e[0]].moveto = self.squares[e[1]]

    def setup_play(self, start, end):
        self.current_pos = self.squares[start]
        self.end_pos = self.squares[end]

    def throw(self):
        roll = random.randint(1, 6)
        if self.current_pos.value + roll <= len(self.squares)-1:
            self.current_pos = self.squares[self.current_pos.value + roll]
            if self.current_pos.moveto:
                self.current_pos = self.current_pos.moveto
            print('Position: ', self.current_pos.value)
            if self.current_pos == self.end_pos:
                print 'Winner!'
                return True

# initialize the board
b = Board(30)
edges = [(27, 1),
         (11, 26),
         (3, 22),
         (21, 9),
         (17, 4),
         (8, 5),
         (19, 7)]
b.setup_snake_ladder(edges)
b.setup_play(1, 30)
while True:
    if b.throw():
        break
