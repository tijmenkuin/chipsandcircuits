#git branch

#nieuwe branch
#git branch tim

#ga naar branch
#git checkout tim

#git pull

#git push main
#git push origin tijmen:main

from gridpoint import GridPoint
from gridsegment import GridSegment

class Chip():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = 7
        self.cost = 0
        self.grid = {}
        self.netlist = []
        self.wires = {}
        self.initializeGrid()
    
    def initializeGrid(self):
        #Initialize GridPoints
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    if z in self.grid:
                        if y >= len(self.grid[z]):
                            self.grid[z].append([GridPoint(x,y,z)])
                        else:
                            self.grid[z][y].append(GridPoint(x,y,z))
                    else:
                        self.grid[z] = [[GridPoint(x,y,z)]]

        #Initialize GridSegments
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    current_gridpoint = self.getGridPoint(x,y,z)
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x - 1, y, z), 'left', 'right')
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x + 1, y, z), 'right', 'left')
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x, y - 1, z), 'backwards', 'forwards')
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x, y + 1, z), 'forwards', 'backwards')
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x, y, z - 1), 'down', 'up')
                    self.addGridSegment(current_gridpoint, self.getGridPoint(x, y, z + 1), 'up', 'down')


    def addGridSegment(self, gridpoint1, gridpoint2, direction1, direction2):
        if gridpoint2 is not None:
            if direction2 not in gridpoint2.grid_segments:
                gridsegment = GridSegment(gridpoint1, gridpoint2)
                gridpoint1.grid_segments[direction1] = gridsegment
                gridpoint2.grid_segments[direction2] = gridsegment


    def getGridPoint(self, x, y, z):
        if x < 0 or y < 0 or z < 0:
            return None
        try:
            return self.grid[z][y][x]
        except:
            return None