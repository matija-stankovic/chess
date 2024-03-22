from piece import Piece

class Pawn(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "P", 1)
        self.didFirstMove = False 

class Rook(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "R", 5)

class Bishop(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "B", 3)

class Knight(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "Kn", 3)

class Queen(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "Q", 9)

class King(Piece):
    def __init__(self, id, position, player):
        super().__init__(id, position, player, "K", -1)


