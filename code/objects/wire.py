class Wire():
    def __init__(self):
        self.path = []
        self.connected = False

    def __repr__(self):
        return f"{self.path}"
    
    def addPoint(self, point):
        self.path.append(point)

