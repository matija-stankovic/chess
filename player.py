import sys

class Player:
    def __init__(self, id, colour):
        self.colour = colour
        self.id = id
        self.score = 0
        self.isWon = False
        self.pieces = {}
    
    def addPiece(self, location, piece):
        self.pieces[location] = piece

    def isPiece(self, location):
        if location in self.pieces:
            return True
        else:
            return False

    def getPieceAtLocation(self, location):
        return self.pieces[location]
        

    def getProperRow(self):
        while True:
            try:
                row = int(input("Choose the row you want to move from: "))
                if 1 > row or row > 8:
                    print("Must be an int between 1 - 8")
                else:
                    break
            except KeyboardInterrupt:
                sys.exit()
            except:
                print("Must be an int between 1 - 8")
        return row - 1
    
    def getProperCol(self):
        cols = ["A", "B", "C", "D", "E", "F", "G", "H"]
        while True:
            col = input("Choose the column you want to move from (A - H): ").upper()
            if col in cols:
                break
            else:
                print("Must be an Letter between A - H")
        return col
    
    def won(self):
        return self.isWon

    def move(self):
        row = self.getProperRow()
        col = self.getProperCol()
        
        while not self.isPiece((row, col)):
            print("You don't have a piece there. Choose again")
            row = self.getProperRow()
            col = self.getProperCol()
        
        piece = self.getPieceAtLocation((row, col))
        piece.printStat()
    
    def __str__(self):
        return "Player " + str(self.id) + " (" + self.colour + ")"

