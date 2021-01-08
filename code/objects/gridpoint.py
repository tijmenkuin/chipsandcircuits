class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate_id = None
        self.relatives = {}
        self.grid_segments = {}

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"

    def isGate(self):
        return self.gate_id is not None

    def isIntersected(self):
        return len([True for k in ('left', 'right', 'forwards', 'backwards', 'up','down') if self.isMovePossible(k)]) >= 4

    def isMovePossible(self, move):
        if move not in self.grid_segments:
            return False
        if  self.grid_segments[move] is not None:
            return self.grid_segments[move].isUsed()
        return False

    def checkMoveUsed(self, move):
        if move not in self.grid_segments:
            return None
        if  self.grid_segments[move] is not None:
            return self.grid_segments[move].isUsed()
        return None