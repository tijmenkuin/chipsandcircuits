from ..objects.chip import Chip
from ..objects.wire import Wire

import random
import numpy as np
import copy

class Greedy():
    def __init__(self, chip):
        self.chip = chip

        self.netlist = self.chip.netlist
        
        self.current_point = None
        self.end_point = None
    
    def run(self):
        count = -1
        for net in self.netlist:
            count += 1
            self.current_point = net.target[0]
            self.end_point = net.target[1]

            wire = Wire(self.current_point)

            if self.makeWire(wire):
                self.chip.outputdict[net] = wire
            else:
                return count / len(self.netlist)
        
        return 1

    def makeWire(self, wire):
        while not wire.connected:
            if self.current_point.intersected >= 1:
                self.chip.addIntersection()
            
            self.current_point.intersect()

            compare = self.valued_options()

            if compare == []:
                return False

            move = self.selectMove(compare)

            self.current_point.grid_segments[move].used = True
            self.current_point = self.current_point.relatives[move]

            wire.wire_path.append(self.current_point)

            if self.current_point == self.end_point:
                wire.connected = True
        return True 
        
    
    def heuristic(self, point):
        amount_options = len(self.options(point))
        heuristic_value = self.manhatten_distance(point, self.end_point)

        return heuristic_value / amount_options

    def selectMove(self, comparation):
        """
        Decide move, for given data
        """
        scores = [score[0] for score in comparation]
        minval = min(scores)
        indeces = [i for i, v in enumerate(scores) if v == minval]
        pick = random.choice(indeces)

        return comparation[pick][1]

    def valued_options(self):
        """
        Gives list of move options and their heuristic value
        """
        compare = []
        for move, option in self.current_point.relatives.items():
            if self.current_point.movePossible(move, self.end_point):
                score = self.heuristic(option)
                compare.append([score, move])

        return compare

    def options(self, point):
        """
        Gives list of move options
        """
        options = []
        for move, option in self.current_point.relatives.items():
            if self.current_point.movePossible(move, self.end_point):
                options.append(move)

        return options

    def manhatten_distance(self, point1, point2):
        return abs(point1.x - point2.x) + abs(point1.y - point2.y) + abs(point1.z - point2.z)