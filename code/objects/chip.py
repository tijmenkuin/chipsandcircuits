from .gridpoint import GridPoint
from .gridsegment import GridSegment
from .net import Net
from .wire import Wire

import csv

class Chip():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = 8
        self.cost = 0
        self.grid = {}
        self.wires = self.createWires()
        self.netlist = []
        self.gates = {}
        self.initializeGrid()
        self.outputdict = {}
        self.amount_intersections = 0
    
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
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x - 1, y, z), 'left', 'right')
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x + 1, y, z), 'right', 'left')
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x, y - 1, z), 'forwards', 'backwards')
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x, y + 1, z), 'backwards', 'forwards')
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x, y, z - 1), 'down', 'up')
                    self.addGridSegmentAndRelatives(current_gridpoint, self.getGridPoint(x, y, z + 1), 'up', 'down')


    def addGridSegmentAndRelatives(self, gridpoint1, gridpoint2, direction1, direction2):
        if gridpoint2 is not None:
            gridpoint1.relatives[direction1] = gridpoint2

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

    
    def initializeGates(self, chip):
        with open(f"data/realdata/gates_netlists/chip_{chip}/print_{chip}.csv", "r") as inp:
            next(inp)
            for line in inp:
                location = list(map(int,line.rstrip("\n").split(",")))

                gate = self.getGridPoint(location[1], location[2], 0)
                gate.gate_id = location[0]
                self.gates[gate.gate_id] = gate



    def initializeNetlist(self, chip, netlist):
        with open(f"data/realdata/gates_netlists/chip_{chip}/netlist_{netlist}.csv", "r") as inp:
            next(inp)
            for line in inp:
                gate_ids = list(map(int,line.rstrip("\n").split(",")))
                net = Net(self.gates[gate_ids[0]], self.gates[gate_ids[1]])
                self.netlist.append(net)
            


    def giveResults(self):
        with open("testfile.csv", "w", newline="") as f:
            thewriter = csv.writer(f)
            thewriter.writerow(['net', 'wire'])

            for key in self.outputdict:
                thewriter.writerow([str(key), str(self.outputdict[key])])
            return thewriter
    
    def createWires(self):
        """
        For time being hard coded
        """
        wire1 = Wire([[1,5,0],[2,5,0],[3,5,0],[4,5,0],[5,5,0],[6,5,0]])
        wire2 = Wire([[1,5,0],[1,4,0],[2,4,0],[3,4,0],[4,4,0]])
        wire3 = Wire([[4,4,0],[4,3,0],[3,3,0],[2,3,0],[1,3,0],[0,3,0],[0,2,0],[0,1,0],[0,0,0],[1,0,0],[2,0,0],[3,0,0],[3,1,0]])
        wire4 = Wire([[6,2,0],[5,2,0],[5,3,0],[5,4,0],[6,4,0],[6,5,0]])
        wire5 = Wire([[3,1,0],[4,1,0],[5,1,0],[6,1,0],[7,1,0],[7,2,0],[6,2,0]])

        return [wire1, wire2, wire3, wire4, wire5]

    def makeDict(self):
        self.outputdict = {}
        wires = self.createWires()
        if len(wires) == len(self.netlist):
            iterations = len(wires)
            for i in range(iterations):
                self.outputdict[self.netlist[i]] = wires[i].wire_path
    
    def addIntersection(self):
        self.amount_intersections += 1
