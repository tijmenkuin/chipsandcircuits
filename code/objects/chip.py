from .gridpoint import GridPoint
from .gridsegment import GridSegment
from ..utils.size_determinator import SizeDeterminator
from .net import Net
from .wire import Wire

import csv
import math
import random

class Chip():
    def __init__(self, chip_id, netlist_id):
        self.chip_id = chip_id
        self.netlist_id = netlist_id

        sd = SizeDeterminator(chip_id)

        self.width = sd.getWidth()
        self.height = sd.getHeight()
        self.depth = 8

        self.cost = 0

        self.grid = {}

        self.netlist = []

        self.gates = {}

        self.initializeGrid()
        self.initializeGates(chip_id)
        self.initializeNetlist(chip_id, netlist_id)

        self.solution = {}
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

    def initializeGates(self, chip_id):
        with open(f"data/realdata/gates_netlists/chip_{chip_id}/print_{chip_id}.csv", "r") as inp:
            next(inp)
            for line in inp:
                location = list(map(int,line.rstrip("\n").split(",")))

                gate = self.getGridPoint(location[1], location[2], 0)
                gate.gate_id = location[0]
                self.gates[gate.gate_id] = gate

    def initializeNetlist(self, chip_id, netlist_id):
        with open(f"data/realdata/gates_netlists/chip_{chip_id}/netlist_{netlist_id}.csv", "r") as inp:
            next(inp)
            for line in inp:
                gate_ids = list(map(int,line.rstrip("\n").split(",")))
                net = Net(self.gates[gate_ids[0]], self.gates[gate_ids[1]])
                self.netlist.append(net)

    def clear(self):
        self.cost = 0
        for net in self.netlist:
            if net in self.solution:
                wire = self.solution[net]
                del wire
            net.copy = [net.target[0], net.target[1]]
            net.wire_0 = []
            net.wire_1 = []
        self.solution = {}

        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    point = self.getGridPoint(x,y,z)
                    for grid_segment in point.grid_segments.values():
                        grid_segment.used = False
                    point.last_move = []
                    point.intersected = 0

    def addIntersection(self):
        self.amount_intersections += 1


    def giveHeuristicValues3(self, start_point, target_point):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    dx1 = this_gridpoint.x - target_point.x
                    dy1 = this_gridpoint.y - target_point.y
                    dx2 = start_point.x - target_point.x
                    dy2 = start_point.y - target_point.y
                    cross = abs(dx1*dy2 - dx2*dy1)
                    this_gridpoint.heuristic_value = int(cross)

    def giveHeuristicValues4(self, target_point):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    dx = abs(this_gridpoint.x - target_point.x)
                    dy = abs(this_gridpoint.y - target_point.y)
                    dz = abs(this_gridpoint.z - target_point.z)
                    this_gridpoint.heuristic_value = (math.pow(dx, 2) + math.pow(dy, 2)+ math.pow(dz, 2))


    def giveHeuristicValues(self, target_point):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    this_gridpoint.heuristic_value = this_gridpoint.manhattanDistanceTo(target_point)

    def giveHeuristicValues2(self, start_point, end_point):      
        radius = int((self.height*self.width)/((self.height+self.width)*2))

        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)

                    start_worth = this_gridpoint.manhattanDistanceTo(start_point)
                    end_worth = this_gridpoint.manhattanDistanceTo(start_point)
                    extra_worth = 0

                    if x in range(end_point.x-radius, end_point.x+1+radius) and y in range(end_point.y-radius, end_point.y+1+radius):
                        extra_worth = 2*z

                    formula = int((0.5 * start_worth)) - 2*z + end_worth + extra_worth

                    this_gridpoint.heuristic_value = formula

    def giveDefaultGScores(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    this_gridpoint.gscore = math.inf


    def netlistRandomizer(self):
        random.shuffle(self.netlist)

    def clear2(self):
        self.netlist = []
        self.solution = {}

        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    point = self.getGridPoint(x,y,z)
                    for grid_segment in point.grid_segments.values():
                        grid_segment.used = False
                    point.intersected = 0
    
    def setCheckedFalse(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    point = self.getGridPoint(x,y,z)
                    point.checked = False

