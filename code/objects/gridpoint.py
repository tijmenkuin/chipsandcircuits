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
    
    @property
    def getCoordinates(self):
        return [self.x, self.y, self.z]

    def isGate(self):
        return self.gate_id is not None

    def isIntersected(self):
        return len([True for k in ('left', 'right', 'forwards', 'backwards', 'up','down') if self.isMovePossible(k)]) >= 4

    def isMovePossible(self, direction):
        if direction not in self.grid_segments:
            return False
        if  self.grid_segments[direction] is not None:
            return self.grid_segments[direction].isUsed()
        return False

    def checkMoveUsed(self, direction):
        if direction not in self.grid_segments:
            return None
        if  self.grid_segments[direction] is not None:
            return self.grid_segments[direction].isUsed()
        return None

    def moveTo(self, direction):
        if self.checkMoveUsed(direction) == False:
            self.grid_segments[direction].used = True
            if self.grid_segments[direction].connections[0] == self:
                return self.grid_segments[direction].connections[1]
            return self.grid_segments[direction].connections[0]  
        else:
            return False

    def getDirection(self, x,y,z):
        x = x - self.x
        y = y - self.y
        z = z - self.z

        if x == 1 and y == 0 and z == 0:
            return 'right'
        if x == -1 and y == 0 and z == 0:
            return 'left'
        if x == 0 and y == 1 and z == 0:
            return 'forwards'
        if x == 0 and y == -1 and z == 0:
            return 'backwards'
        if x == 0 and y == 0 and z == 1:
            return 'up'
        if x == 0 and y == 0 and z == -1:
            return 'down'
            
        return None
    
    def distanceToTarget(self, target_point):
        return self.distanceBetweenCoordinates(self.getCoordinates, target_point.getCoordinates)

    def distanceBetweenCoordinates(self, coordinate1, coordinate2):
        distance = 0
        for i in range(3):
            distance += abs(coordinate1[i] - coordinate2[i])
        return distance