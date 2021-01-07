class Wire():
    def __init__(self, move):
        self.wire_path = [move]
        self.connected = False

    def addMove(self, move):
        self.wire_path.append(move)

    def removeMove(self, move):
        self.wire_path

wire_path: [ (x0,y0,z0),(x1,y1,z1),... ]
connected: Boolean