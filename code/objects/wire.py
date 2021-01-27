"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

wire.py

Chips and Circuits 2021
"""

class Wire():
    def __init__(self):
        self.path = []
        self.connected = False

    def __repr__(self):
        return f"{self.path}"
    
    def addPoint(self, point):
        """
        Adds point to wire path
        """
        self.path.append(point)

