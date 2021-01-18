from ..objects.gridpoint import GridPoint
from ..objects.gridsegment import GridSegment
from ..objects.net import Net
from ..objects.chip import Chip
from ..objects.wire import Wire

import copy


class CostFunction():
    """
    Calculates, given a solution, the costs of this solution, the calculation has two parts:
    - Calculation of the number of unit length wires
    - Calculation of the amount of intersections

    NOTE: Make sure the inserted solutions are valid, use checker class !!
    """
    def __init__(self, solution):
        self.solutioncopy = dict((k,v) for k,v in solution.items())

        # self.costs = self.lengthCount() + 300 * self.intersectionCount()
        self.intersectionCount()

    def lengthCount(self):
        length = 0
        for wire in self.solutioncopy.values():
            length += len(wire) - 1
        return length

    def intersectionCount(self):
        for wire in self.solutioncopy.values():
            wire.path.pop()
             

        return 0