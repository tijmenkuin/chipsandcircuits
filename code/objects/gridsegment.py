class GridSegment():
    def __init__(self, gridpoint1, gridpoint2):
        self.connections = [gridpoint1, gridpoint2]
        self.used = False
    
    def __repr__(self):
        return f"{self.connections}"

