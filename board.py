from player import Player
from all_pieces import *
class Board:
    def __init__(self):
        self.board = {}
        
        for i in range(8):
            self.board[i] = {
                'A' : None,
                'B' : None,
                'C' : None,
                'D' : None,
                'E' : None,
                'F' : None,
                'G' : None,
                'H' : None,
            }
        
        self.player1 = Player(1, "White")
        self.player2 = Player(2, "Black")

        self.pieceId = 0
        self.turn = 0
        self.populateBoard()
        self.printBoard()
        self.play()


    def play(self):
        while not self.player1.won() and not self.player2.won():
            if self.turn % 2 == 0:
                print(str(self.player1), "to move")
                self.player1.move()
            else:
                print(str(self.player2), "to move")
                self.player2.move()
            self.turn += 1


    def populateBoard(self):
        # Pawns for P1
        for spot in self.board[1]:
            self.board[1][spot] = Pawn(self.pieceId, (1, spot), self.player1)
            self.player1.addPiece((1, spot), self.board[1][spot])
            self.pieceId += 1
        
        # Pawns for P2
        for spot in self.board[6]:
            self.board[6][spot] = Pawn(self.pieceId, (6, spot), self.player2)
            self.player2.addPiece((6, spot), self.board[6][spot])
            self.pieceId += 1
        
        # Knights for for P1
        self.board[0]["B"] = Knight(self.pieceId, (0, "B"), self.player1)
        self.player1.addPiece((0, "B"), self.board[0]["B"])
        self.pieceId += 1

        self.board[0]["G"] = Knight(self.pieceId, (0, "G"), self.player1)
        self.player1.addPiece((0, "G"), self.board[0]["G"])
        self.pieceId += 1

        # Knights for for P2
        self.board[7]["B"] = Knight(self.pieceId, (7, "B"), self.player2)
        self.player2.addPiece((7, "B"), self.board[7]["B"])
        self.pieceId += 1

        self.board[7]["G"] = Knight(self.pieceId, (7, "G"), self.player2)
        self.player2.addPiece((7, "G"), self.board[7]["G"])
        self.pieceId += 1


        # Rooks for for P1
        self.board[0]["A"] = Rook(self.pieceId, (0, "A"), self.player1)
        self.player1.addPiece((0, "A"), self.board[0]["A"])
        self.pieceId += 1

        self.board[0]["H"] = Rook(self.pieceId, (0, "H"), self.player1)
        self.player1.addPiece((0, "H"), self.board[0]["H"])
        self.pieceId += 1

        # Rooks for for P2
        self.board[7]["A"] = Rook(self.pieceId, (7, "A"), self.player2)
        self.player2.addPiece((7, "A"), self.board[7]["A"])
        self.pieceId += 1
        
        self.board[7]["H"] = Rook(self.pieceId, (7, "H"), self.player2)
        self.player2.addPiece((7, "H"), self.board[7]["H"])
        self.pieceId += 1


        # Bishops for for P1
        self.board[0]["C"] = Bishop(self.pieceId, (0, "C"), self.player1)
        self.player1.addPiece((0, "C"), self.board[0]["C"])
        self.pieceId += 1

        self.board[0]["F"] = Bishop(self.pieceId, (0, "F"), self.player1)
        self.player1.addPiece((0, "F"), self.board[0]["F"])
        self.pieceId += 1

        # Bishops for for P2
        self.board[7]["C"] = Bishop(self.pieceId, (7, "C"), self.player2)
        self.player2.addPiece((7, "C"), self.board[7]["C"])
        self.pieceId += 1

        self.board[7]["F"] = Bishop(self.pieceId, (7, "F"), self.player2)
        self.player2.addPiece((7, "F"), self.board[7]["F"])
        self.pieceId += 1


        # Royals for for P1
        self.board[0]["D"] = Queen(self.pieceId, (0, "D"), self.player1)
        self.player1.addPiece((0, "D"), self.board[0]["D"])
        self.pieceId += 1

        self.board[0]["E"] = King(self.pieceId, (0, "E"), self.player1)
        self.player1.addPiece((0, "E"), self.board[0]["E"])
        self.pieceId += 1

        # Royal for for P2
        self.board[7]["D"] = Queen(self.pieceId, (7, "D"), self.player2)
        self.player2.addPiece((7, "D"), self.board[7]["D"])
        self.pieceId += 1

        self.board[7]["E"] = King(self.pieceId, (7, "E"), self.player2)
        self.player2.addPiece((7, "E"), self.board[7]["E"])
        self.pieceId += 1


    def printRow(self, rowNum, row):
        print(f"{rowNum + 1} |", end="")
        for key in row:
            if row[key]:
                print(str(row[key]).center(3), end="")
            else:
                print(".".center(3), end="")
        print()

    def printPieces(self):
        for key in reversed(self.board):
            self.printRow(key, self.board[key])

    def printBoard(self):
        row = self.board[0]
        print("  |", end="")
        for key in row:
            print(str(key).center(3), end="")

        print("\n----------------------------")
        
        self.printPieces()

        print("------------------------------")
        print("  |", end="")
        for key in row:
            print(str(key).center(3), end="")

        print()
        