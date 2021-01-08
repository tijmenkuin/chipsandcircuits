class Wire():
    def __init__(self, path):
        self.wire_path = path #[move]
        self.connected = True #False

    def addMove(self, move):
        self.wire_path.append(move)

    def removeMove(self, move):
        self.wire_path.remove(move)