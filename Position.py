class Position():
    def __init__(self, y, x, tObject = None):
        self.y = y
        self.x = x
        self.tObject = tObject

    def getObject(self):
        return self.tObject

    def setObject(self, newObject):
        self.tObject = newObject