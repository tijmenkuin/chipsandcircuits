#git branch

#nieuwe branch
#git branch tim

#ga naar branch
#git checkout tim

#git pull

#git push main
#git push origin tijmen:main

from gridpoint import GridPoint

class Chip():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = 7
        self.cost = 0
        self.grid = {}
        self.netlist = []
        self.wires = {}
    
    def initializeGrid(self):
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

    def getGridPoint(self, x, y, z):
        return self.grid[z][y][x]

