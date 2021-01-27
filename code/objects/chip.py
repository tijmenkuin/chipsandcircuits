"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

chip.py

Chips and Circuits 2021
"""

from .grid_point import GridPoint
from .grid_segment import GridSegment
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
        self.grid = {}
        self.netlist = []
        self.gates = {}

        self.initializeGrid()
        self.initializeGates(chip_id)
        self.initializeNetlist(chip_id, netlist_id)

        self.solution = {}
    
    def initializeGrid(self):
        """
        Initializes GridPoints and GridSegments objects and puts them in the grid dictionary
        """
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
        """
        Connects the GridSegments with the GridPoints and connects relative GridPoints to the iterating GridPoint
        """
        if gridpoint2 is not None:
            gridpoint1.relatives[direction1] = gridpoint2

            if direction2 not in gridpoint2.grid_segments:
                gridsegment = GridSegment(gridpoint1, gridpoint2)
                gridpoint1.grid_segments[direction1] = gridsegment
                gridpoint2.grid_segments[direction2] = gridsegment

    def getGridPoint(self, x, y, z):
        """
        Returns the GridPoint at a certain x,y,z value and returns None if it does not exist
        """
        if x < 0 or y < 0 or z < 0:
            return None
        try:
            return self.grid[z][y][x]
        except:
            return None

    def initializeGates(self, chip_id):
        """
        Adds a gate_id to the correct GridPoint and stores gate in dictionary
        """
        with open(f"data/chip_{chip_id}/print_{chip_id}.csv", "r") as inp:
            next(inp)
            for line in inp:
                location = list(map(int,line.rstrip("\n").split(",")))

                gate = self.getGridPoint(location[1], location[2], 0)
                gate.gate_id = location[0]
                self.gates[gate.gate_id] = gate

    def initializeNetlist(self, chip_id, netlist_id):
        """
        Initilizes all Net objects with the corresponding gates
        """
        with open(f"data/chip_{chip_id}/netlist_{netlist_id}.csv", "r") as inp:
            next(inp)
            for line in inp:
                gate_ids = list(map(int,line.rstrip("\n").split(",")))
                net = Net(self.gates[gate_ids[0]], self.gates[gate_ids[1]])
                self.netlist.append(net)



#### A SEARCH

    def giveTiesHeuristicValues(self, start_point, target_point):
        """
        Heuristic based on Ties
        """
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

    def giveEuclidesHeuristicValues(self, target_point):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    dx = abs(this_gridpoint.x - target_point.x)
                    dy = abs(this_gridpoint.y - target_point.y)
                    dz = abs(this_gridpoint.z - target_point.z)
                    this_gridpoint.heuristic_value = (math.pow(dx, 2) + math.pow(dy, 2)+ math.pow(dz, 2))


    def giveManhattanHeuristicValues(self, target_point):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    this_gridpoint.heuristic_value = this_gridpoint.manhattanDistanceTo(target_point)

    def giveDefaultGScores(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    this_gridpoint = self.getGridPoint(x,y,z)
                    this_gridpoint.gscore = math.inf

    def netlistRandomizer(self):
        random.shuffle(self.netlist)

    # Hill Climber
    
    def clear(self):
        self.netlist = []
        self.solution = {}
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    point = self.getGridPoint(x,y,z)
                    for grid_segment in point.grid_segments.values():
                        grid_segment.used = False
                    point.intersected = 0
    
    
    # Resultfunction
    def setCheckedFalse(self):
        for z in range(self.depth):
            for y in range(self.height):
                for x in range(self.width):
                    point = self.getGridPoint(x,y,z)
                    point.checked = False