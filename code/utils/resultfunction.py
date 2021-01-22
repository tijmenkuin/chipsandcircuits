from ..objects.gridpoint import GridPoint
from ..objects.gridsegment import GridSegment
from ..objects.net import Net
from ..objects.chip import Chip
from ..objects.wire import Wire

import copy


class ResultFunction():
    """
    Calculates, given a solution, the costs of this solution, the calculation has two parts:
    - Calculation of the number of unit length wires
    - Calculation of the amount of intersections

    NOTE: Make sure the inserted solutions are valid, use checker class !!
    """
    def __init__(self, chip):
        self.solution = chip.solution

        self.intersections = None
        self.length = None

        self.lengthCount()
        self.intersectionCount()

        self.costs = self.length + 300 * self.intersections

    def lengthCount(self):
        length = 0
        for wire in self.solution.values():
            length += len(wire.path) - 1
        self.length = length

    def intersectionCount(self):
        counter = 0

        for wire in self.solution.values():
            for point in wire.path:
                if not (point.isGate() or point.checked) :
                    point.checked = True
                    if point.intersected > 0:
                        counter += point.intersected - 1
         
        self.intersections = counter
            
            