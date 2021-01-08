from .gridpoint import GridPoint
import csv

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

    
    def initializeGates(self, chip):
        with open(f"data/realdata/gates_netlists/chip_{chip}/print_{chip}.csv", "r") as inp:
            next(inp)
            for line in inp:
                location = list(map(int,line.rstrip("\n").split(",")))
                print(location)
                
                # grid = self.getGridPoint(location[1], location[2], 0)
                # grid.gate = True
                # grid.id = location[0]
