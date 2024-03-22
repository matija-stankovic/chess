class Piece:
    def __init__(self, id, position, player, pieceType, value):
        self.id = id
        self.position = position
        self.player = player
        self.pieceType = pieceType
        self.val = value
    
    def getId(self):
        return self.id 

    def getPosition(self):
        return self.position
    
    def getPlayer(self):
        return self.player

    def getPieceType(self):
        return self.pieceType

    def getPieceValue(self):
        return self.val
    
    def printStat(self):
        print(f"{self.getPieceType()} ({self.getId()} - {self.getPieceValue()}pts) belonging to {self.getPlayer()} at position {self.getPosition()}")

    def __str__(self):
        return self.pieceType