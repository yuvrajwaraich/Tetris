

class OrangeRicky():

    def __init__(self, rotation):
        self.colour = "O"
        self.rotation = rotation

        if rotation == 0:
            self.coords = [[8, 0], [8, 1], [7, 1], [6, 1]]
        elif rotation == 1:
            self.coords = [[8, 2], [7, 2], [7, 1], [7, 0]]
        elif rotation == 2:
            self.coords = [[6, 2], [6, 1], [7, 1], [8, 1]]
        elif rotation == 3:
            self.coords = [[6, 0], [7, 0], [7, 1], [7, 2]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0]][self.coords[0][1] + 2].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][1] += 2
                self.coords[1][1] += 1
                self.coords[1][0] -= 1
                self.coords[3][1] -= 1
                self.coords[3][0] += 1
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0] - 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][0] -= 2
                self.coords[1][1] -= 1
                self.coords[1][0] -= 1
                self.coords[3][1] += 1
                self.coords[3][0] += 1
                self.rotation = 2
        elif self.rotation == 2:
            if board[self.coords[0][0]][self.coords[0][1] - 2].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][1] -= 2
                self.coords[1][1] -= 1
                self.coords[1][0] += 1
                self.coords[3][1] += 1
                self.coords[3][0] -= 1
                self.rotation = 3
        elif self.rotation == 3:
            if board[self.coords[0][0] + 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][0] += 2
                self.coords[1][1] += 1
                self.coords[1][0] += 1
                self.coords[3][1] -= 1
                self.coords[3][0] -= 1
                self.rotation = 0

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class BlueRicky():

    def __init__(self, rotation):
        self.colour = "DB"
        self.rotation = rotation
        if rotation == 0:
            self.coords = [[6, 0], [6, 1], [7, 1], [8, 1]]
        elif rotation == 1:
            self.coords = [[8, 0], [7, 0], [7, 1], [7, 2]]
        elif rotation == 2:
            self.coords = [[8, 2], [8, 1], [7, 1], [6, 1]]
        elif rotation == 3:
            self.coords = [[6, 2], [7, 2], [7, 1], [7, 0]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0] + 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][0] += 2
                self.coords[1][1] -= 1
                self.coords[1][0] += 1
                self.coords[3][1] += 1
                self.coords[3][0] -= 1
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0]][self.coords[0][1] + 2].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][1] += 2
                self.coords[1][1] += 1
                self.coords[1][0] += 1
                self.coords[3][1] -= 1
                self.coords[3][0] -= 1
                self.rotation = 2
        elif self.rotation == 2:
            if board[self.coords[0][0] - 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][0] -= 2
                self.coords[1][1] += 1
                self.coords[1][0] -= 1
                self.coords[3][1] -= 1
                self.coords[3][0] += 1
                self.rotation = 3
        elif self.rotation == 3:
            if board[self.coords[0][0]][self.coords[0][1] - 2].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][1] -= 2
                self.coords[1][1] -= 1
                self.coords[1][0] -= 1
                self.coords[3][1] += 1
                self.coords[3][0] += 1
                self.rotation = 0

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class CleveZ():

    def __init__(self, rotation):
        self.colour = "R"
        self.rotation = rotation
        if rotation == 0:
            self.coords = [[6, 0], [7, 0], [7, 1], [8, 1]]
        elif rotation == 1:
            self.coords = [[8, 0], [8, 1], [7, 1], [7, 2]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0] + 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][0] += 2
                self.coords[1][1] += 1
                self.coords[1][0] += 1
                self.coords[3][1] += 1
                self.coords[3][0] -= 1
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0] - 2][self.coords[0][1]].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][0] -= 2
                self.coords[1][1] -= 1
                self.coords[1][0] -= 1
                self.coords[3][1] -= 1
                self.coords[3][0] += 1
                self.rotation = 0

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class RhodeZ():

    def __init__(self, rotation):
        self.colour = "G"
        self.rotation = rotation
        if rotation == 0:
            self.coords = [[8, 0], [7, 0], [7, 1], [6, 1]]
        elif rotation == 1:
            self.coords = [[8, 2], [8, 1], [7, 1], [7, 0]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0]][self.coords[0][1] + 2].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][1] += 2
                self.coords[1][1] += 1
                self.coords[1][0] += 1
                self.coords[3][1] -= 1
                self.coords[3][0] += 1
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0]][self.coords[0][1] - 2].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][1] -= 2
                self.coords[1][1] -= 1
                self.coords[1][0] -= 1
                self.coords[3][1] += 1
                self.coords[3][0] -= 1
                self.rotation = 0

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class Hero():

    def __init__(self, rotation):
        self.colour = "LB"
        self.rotation = rotation
        if rotation == 0:
            self.coords = [[7, 0], [7, 1], [7, 2], [7, 3]]
        elif rotation == 1:
            self.coords = [[6, 1], [7, 1], [8, 1], [9, 1]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0] - 1][self.coords[0][1] + 1].getObject() == None and\
                    board[self.coords[2][0] + 1][self.coords[2][1] - 1].getObject() == None and\
                    board[self.coords[3][0] + 2][self.coords[3][1] - 2].getObject() == None:

                self.coords[0][1] += 1
                self.coords[0][0] -= 1
                self.coords[2][1] -= 1
                self.coords[2][0] += 1
                self.coords[3][1] -= 2
                self.coords[3][0] += 2
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0] + 1][self.coords[0][1] - 1].getObject() == None and\
                    board[self.coords[2][0] - 1][self.coords[2][1] + 1].getObject() == None and\
                    board[self.coords[3][0] - 2][self.coords[3][1] + 2].getObject() == None:

                self.coords[0][1] -= 1
                self.coords[0][0] += 1
                self.coords[2][1] += 1
                self.coords[2][0] -= 1
                self.coords[3][1] += 2
                self.coords[3][0] -= 2
                self.rotation = 0

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class Teewee():

    def __init__(self, rotation):
        self.colour = "P"
        self.rotation = rotation

        if rotation == 0:
            self.coords = [[8, 1], [7, 0], [7, 1], [7, 2]]
        elif rotation == 1:
            self.coords = [[7, 2], [8, 1], [7, 1], [6, 1]]
        elif rotation == 2:
            self.coords = [[6, 1], [7, 2], [7, 1], [7, 0]]
        elif rotation == 3:
            self.coords = [[7, 0], [6, 1], [7, 1], [8, 1]]

    def rotate(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        if self.rotation == 0:
            if board[self.coords[0][0] - 1][self.coords[0][1] + 1].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][1] += 1
                self.coords[0][0] -= 1
                self.coords[1][1] += 1
                self.coords[1][0] += 1
                self.coords[3][1] -= 1
                self.coords[3][0] -= 1
                self.rotation = 1
        elif self.rotation == 1:
            if board[self.coords[0][0] - 1][self.coords[0][1] - 1].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] + 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] - 1].getObject() == None:

                self.coords[0][1] -= 1
                self.coords[0][0] -= 1
                self.coords[1][1] += 1
                self.coords[1][0] -= 1
                self.coords[3][1] -= 1
                self.coords[3][0] += 1
                self.rotation = 2
        elif self.rotation == 2:
            if board[self.coords[0][0] + 1][self.coords[0][1] - 1].getObject() == None and\
                    board[self.coords[1][0] - 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] + 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][1] -= 1
                self.coords[0][0] += 1
                self.coords[1][1] -= 1
                self.coords[1][0] -= 1
                self.coords[3][1] += 1
                self.coords[3][0] += 1
                self.rotation = 3
        elif self.rotation == 3:
            if board[self.coords[0][0] + 1][self.coords[0][1] + 1].getObject() == None and\
                    board[self.coords[1][0] + 1][self.coords[1][1] - 1].getObject() == None and\
                    board[self.coords[3][0] - 1][self.coords[3][1] + 1].getObject() == None:

                self.coords[0][1] += 1
                self.coords[0][0] += 1
                self.coords[1][1] -= 1
                self.coords[1][0] += 1
                self.coords[3][1] += 1
                self.coords[3][0] -= 1
                self.rotation = 0

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour


class Smashboy():

    def __init__(self):
        self.colour = "Y"
        self.coords = [[6, 0], [7, 0], [6, 1], [7, 1]]

    def rotate(self, board):
        return

    def moveDown(self, board):
        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(None)

        self.coords[0][1] += 1
        self.coords[1][1] += 1
        self.coords[2][1] += 1
        self.coords[3][1] += 1

        for coord in self.coords:
            board[coord[0]][coord[1]].setObject(self)

    def moveRight(self, board):
        move = True
        for coord in self.coords:
            if coord[0] + 1 == 15:
                return
            if board[coord[0] + 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] += 1
            self.coords[1][0] += 1
            self.coords[2][0] += 1
            self.coords[3][0] += 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def moveLeft(self, board):
        move = True
        for coord in self.coords:
            if coord[0] - 1 == -1:
                return
            if coord[0] - 1 > -1 and board[coord[0] - 1][coord[1]].getObject() not in [None, self]:
                move = False

        if move:
            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(None)

            self.coords[0][0] -= 1
            self.coords[1][0] -= 1
            self.coords[2][0] -= 1
            self.coords[3][0] -= 1

            for coord in self.coords:
                board[coord[0]][coord[1]].setObject(self)

    def getCoords(self):
        return self.coords

    def getColour(self):
        return self.colour
