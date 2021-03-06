"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

grid_point.py

Chips and Circuits 2021
"""

import random

class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate_id = None
        self.relatives = {}
        self.grid_segments = {}
        self.intersected = 0
        self.checked = False
        
        # Asearch attributes
        self.heuristic_value = None
        self.gscore = None
        self.fscore = None

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def isGate(self):
        """
        Returns true if GridPoint is a gate
        """
        return self.gate_id is not None

    def manhattanDistanceTo(self, point):
        """
        Returns the Manhattan Distance to a different GridPoint
        """
        return abs(self.x - point.x) + abs(self.y - point.y) + abs(self.z - point.z)


    # Asearch and Hill Climber functions

    def reachableRelatives(self, end_gate):
        """
        Gives randomly shuffled list of relatives that are reachable (no colissions, no different gates)
        """
        reachables = []
        for move, relative in self.relatives.items():
            if not self.grid_segments[move].used and (not relative.isGate() or relative == end_gate):
                reachables.append(relative)
        random.shuffle(reachables)
        
        return reachables

    def intersect(self):
        self.intersected += 1
    
    def deIntersect(self):
        self.intersected -= 1

    def givesIntersection(self):
        return self.intersected > 0 

    # Greedy Simultaneous functions

    def amountOfIntersections(self):
        """
        Returns the amount of intersections
        """
        used = len([True for direction in self.relatives.keys() if self.grid_segments[direction].used and not self.isGate()])
        if used < 3:
            return 0
        return 1 if used == 3 or used == 4 else 2

    def getMoveScore(self):
        """
        Returns the amount of grid sections that have not been used
        """
        return len([True for direction in self.relatives.keys() if not self.grid_segments[direction].used and not self.isGate()])

    def moveTo(self, direction):
        """
        Returns False if move is not possible, else returns the point in the given direction
        """
        if direction not in self.relatives:
            return False
        grid_segment = self.grid_segments[direction]
        if grid_segment.used:
            return False
        grid_segment.used = True
        return self.relatives[direction]