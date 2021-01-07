class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate = False
        self.relatives = []
        self.grid_segments = []