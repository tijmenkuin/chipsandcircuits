class GridPoint():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.gate_id = None
        self.relatives = {}
        self.grid_segments = {}
        self.last_move = []
        self.intersected = 0
        self.checked = False
        self.heuristic_value = None
        self.gscore = None
        self.fscore = None

    def __repr__(self):
        return f"({self.x},{self.y},{self.z})"

    def intersect(self):
        self.intersected += 1
    
    def deIntersect(self):
        self.intersected -= 1

    def isGate(self):
        return self.gate_id is not None

    def isIntersected(self):
        if self.gate_id is not None:
            return 0
        used = len([True for k in ('left', 'right', 'forwards', 'backwards', 'up','down') if self.isMovePossible(k)])
        if used == 4 or used == 3:
            return 1
        if used == 5 or used == 6:
            return 2
        return 0

    def isIntersected2(self):
        return self.intersected > 0

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

    def reachableRelatives(self):
        """
        Gives list of relatives that are reachable (no colissions)
        """
        reachables = []
        for move, relative in self.relatives.items():
            if not self.grid_segments[move].used:
                reachables.append(relative)
        
        return reachables

    # def undoMove(self):
    #     direction = None

    #     if len(self.last_move) < 1:
    #         return False

    #     reverse_move = self.last_move.pop()

    #     if reverse_move == 'up':
    #         direction = 'down'
    #     elif reverse_move == 'down':
    #         direction = 'up'
    #     elif reverse_move == 'backwards':
    #         direction = 'forwards'
    #     elif reverse_move == 'forwards':
    #         direction = 'backwards'
    #     elif reverse_move == 'left':
    #         direction = 'right'
    #     elif reverse_move == 'right':
    #         direction = 'left'       

    #     if direction is None:
    #         return False

    #     if self.checkMoveUsed(direction):
    #         self.grid_segments[direction].used = False
    #         if self.grid_segments[direction].connections[0] == self:
    #             return self.grid_segments[direction].connections[1]
    #         return self.grid_segments[direction].connections[0]
    #     else:
    #         return False


    # def getDirection(self, x,y,z):
    #     x = x - self.x
    #     y = y - self.y
    #     z = z - self.z

    #     if x == 1 and y == 0 and z == 0:
    #         return 'right'
    #     if x == -1 and y == 0 and z == 0:
    #         return 'left'
    #     if x == 0 and y == 1 and z == 0:
    #         return 'forwards'
    #     if x == 0 and y == -1 and z == 0:
    #         return 'backwards'
    #     if x == 0 and y == 0 and z == 1:
    #         return 'up'
    #     if x == 0 and y == 0 and z == -1:
    #         return 'down'
            
    #     return None

    # def distanceToTarget(self, target_point):
    #     return self.distanceBetweenCoordinates(self.getCoordinates, target_point.getCoordinates)

    # def distanceBetweenCoordinates(self, coordinate1, coordinate2):
    #     distance = 0
    #     for i in range(3):
    #         distance += abs(coordinate1[i] - coordinate2[i])
    #     return distance
    
    def movePossible(self, move, end_gate):
        if self.grid_segments[move].used:
            return False
        
        if self.relatives[move].isGate() and self.relatives[move] != end_gate:
            return False

        return True

    def manhattanDistanceTo(self, point):
        return abs(self.x - point.x) + abs(self.y - point.y) + abs(self.z - point.z)
