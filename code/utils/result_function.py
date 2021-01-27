"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

result_function.py

Chips and Circuits 2021
"""

class ResultFunction():
    """
    Calculates, given a solution, the costs of this solution, the calculation has two parts:
    - Calculation of the number of unit length wires
    - Calculation of the amount of intersections

    NOTE: Make sure the inserted solutions are valid, use checker class
    """
    def __init__(self, chip):
        self.chip = chip

        self.intersections = None
        self.length = None

        self.lengthCount()
        self.intersectionCount()

        self.costs = self.length + 300 * self.intersections

    def lengthCount(self):
        """
        Counts total length of wires
        """
        length = 0
        for wire in self.chip.solution.values():
            length += len(wire.path) - 1
        self.length = length

    def intersectionCount(self):
        """
        Counts intersections
        """
        counter = 0

        for wire in self.chip.solution.values():
            for point in wire.path:
                if not (point.isGate() or point.checked) :
                    point.checked = True
                    if point.intersected > 1:
                        counter += point.intersected - 1
         
        self.intersections = counter
        self.chip.setCheckedFalse()

    def costPerWire(self, wire):
        """
        Calculates the "costs" of a wire
        """
        intersection_counter = 0
        wire_length = len(wire.path) - 1

        for point in wire.path:
            if not point.isGate():
                if point.intersected > 1:
                    intersection_counter += 1
        
        return 300 * intersection_counter + wire_length

    def dictCostPerWire(self):
        """
        Return dict with keys the nets and values the "costs"
        """
        costs_per_wire = dict()

        for net, wire in self.chip.solution.items():
            costs_per_wire[net] = self.costPerWire(wire)

        return costs_per_wire