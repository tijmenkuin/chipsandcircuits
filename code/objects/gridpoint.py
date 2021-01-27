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
        
        #asearch
        self.heuristic_value = None
        self.gscore = None
        self.fscore = None

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def isGate(self):
        return self.gate_id is not None

    def manhattanDistanceTo(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y) + abs(self.z - point.z)

    
    

    # code for A search

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

    # code for GreedySimultenous

    def isIntersected(self):
        if self.gate_id is not None:
            return 0
        used = len([True for k in ('left', 'right', 'forwards', 'backwards', 'up','down') if self.isMovePossible(k)])
        if used == 4 or used == 3:
            return 1
        if used == 5 or used == 6:
            return 2
        return 0

    def getMoveScore(self):
        if self.gate_id is not None:
            return 0
        return len([True for k in ('left', 'right', 'forwards', 'backwards', 'up','down') if self.checkMoveUsed(k) == False])

    def isMovePossible(self, direction):
        if direction not in self.grid_segments:
            return False
        if  self.grid_segments[direction] is not None:
            return self.grid_segments[direction].used
        return False

    def checkMoveUsed(self, direction):
        if direction not in self.grid_segments:
            return None
        if  self.grid_segments[direction] is not None:
            return self.grid_segments[direction].used
        return None

    def moveTo(self, direction):
        if self.checkMoveUsed(direction) == False:
            self.grid_segments[direction].used = True
            newPoint = None

            if self.grid_segments[direction].connections[0] == self:
                newPoint = self.grid_segments[direction].connections[1]
            else:
                newPoint = self.grid_segments[direction].connections[0]
            
            newPoint.last_move.insert(0, direction)

            return newPoint
        else:
            return False