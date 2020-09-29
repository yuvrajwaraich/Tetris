
import tetris_objects
from random import randint
from Position import Position
from sys import exit


class Tetris():

    def __init__(self):
        self.board = [[Position(x, y) for y in range(20)]
                      for x in range(15)]
        self.numRow = 20
        self.numCol = 15
        self.obj = None

    def newObject(self):
        a = randint(0, 6)
        if a == 0:
            obj = tetris_objects.OrangeRicky(randint(0, 3))
        elif a == 1:
            obj = tetris_objects.BlueRicky(randint(0, 3))
        elif a == 2:
            obj = tetris_objects.CleveZ(randint(0, 1))
        elif a == 3:
            obj = tetris_objects.RhodeZ(randint(0, 1))
        elif a == 4:
            obj = tetris_objects.Hero(randint(0, 1))
        elif a == 5:
            obj = tetris_objects.Teewee(randint(0, 3))
        elif a == 6:
            obj = tetris_objects.Smashboy()

        self.obj = obj
        for coord in obj.getCoords():
            if self.board[coord[0]][coord[1]].getObject() == None:
                self.board[coord[0]][coord[1]].setObject(obj)
            else:
                exit()

    def rotate(self):
        self.obj.rotate(self.board)

    def moveObject(self):
        self.obj.moveDown(self.board)

    def moveRight(self):
        self.obj.moveRight(self.board)

    def moveLeft(self):
        self.obj.moveLeft(self.board)

    def hitBottom(self):
        for coord in self.obj.getCoords():
            if coord[1] == 19:
                return True
            if coord[1] + 1 < self.numRow and self.board[coord[0]][coord[1] + 1].getObject() not in [self.obj, None]:
                return True
        return False

    def moveDownRow(self, doneRow):
        for y in range(doneRow - 1, -1, -1):
            for x in range(15):
                self.board[x][y + 1].setObject(self.board[x][y].getObject())
                self.board[x][y].setObject(None)

    def checkRowDone(self):
        done = True
        for y in range(20):
            for x in range(15):
                if self.board[x][y].getObject() == None:
                    done = False
            if done:
                self.moveDownRow(y)
            done = True

    def slamDown(self):

        while not self.hitBottom():
            self.moveObject()