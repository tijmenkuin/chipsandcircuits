class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate = False
        self.id = None
        self.relatives = []
        self.grid_segments = []
    
    def __str__(self):
        return f"point: {self.x}, {self.y}, {self.z}"