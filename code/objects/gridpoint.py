class GridPoint():
    def __init__(self, x, y, z, gate):
        self.x = x
        self.y = y
        self.z = z
        self.gate = gate
        self.relatives = []
        self.grid_segments = []