class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate = False
        self.gate_id = None
        self.state = 0
        self.relatives = {}
        self.grid_segments = {}

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"
    
    def __str__(self):
        return f"({self.x},{self.y},{self.z})"