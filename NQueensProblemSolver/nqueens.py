"""

"""

from array import Array

from array import Array2D


def main():
    n = int(input("Enter n: "))
    boardInit = QueensBoard(n)
    solve = boardInit.size()
    print(solve)
    solve= boardInit.solveNQueens(0)
    solve2=boardInit.draw(0)

class QueensBoard:


    def __init__(self, n):
        self.board = Array2D(n, n)
        #self.board.clear(0)
        self.countQueens = 0


    def size(self):
        return self.board.numRows()

    def numQueens (self):
        return self.countQueens

    def unguarded(self, row, col):
        for j in range(self.board.numCols()):
            for i in range(self.board.numRows()):
                if self.board[i, j] == 'Q':
                    if row == i:
                        return False
                    if col == j:
                        return False
                    if abs(row - i) == abs(col - j):
                        return False

        return True


    def placeQueen(self, row, col):
        the1dArray = self.board.theRows[row]
        the1dArray[col] = 'Q'
        self.countQueens += 1


    def removeQueen(self, row, col):
        self.board[row, col] = 0
        self.countQueens -= 1


    def getQueen(self, row, col):
        #ndxTuple = (row, col)
        the1dArray=self.board.theRows[row]
        value=the1dArray[col]
        #value = self.board.__getitem__(ndxTuple)
        return value


    def reset(self):
        self.board.clear(0)
        self.countQueens = 0


    def solveNQueens(self,col):
        if self.numQueens() ==self.size():
            return True
        else:
            for row in range(self.size()):
                if self.unguarded(row, col):
                    self.placeQueen(row, col)
                    if self.solveNQueens( col+1):
                        return True
                    else:
                        self.removeQueen(row, col)

            return False

    def draw(self,col):
        if self.solveNQueens(col):
            for i in range(self.board.numRows()):
                for j in range(self.board.numCols()):
                    if self.board[i, j] == 'Q':
                        print(' Q ', end = "")
                    else:
                        print(' * ' , end= "")
                print()

main()




