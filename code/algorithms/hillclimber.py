from ..utils.copy_chip import CopyChip
from ..utils.resultfunction import ResultFunction
from ..algorithms.asearch import ASearch

import random

class HillClimber():
    def __init__(self, chip):
        """
        Given a chip with a solution, runs for finding better solutions
        """
        self.chip = None
        self.best_chip = None
        self.best_score = None

        # Gives length of netlist
        self.nets_to_fill = None

        self.initializeChips(chip)

    def initializeChips(self, chip):
        """
        Writes the dummies to work in
        """
        copy = CopyChip(chip)
        self.chip = copy.writeCopy(None)
        self.best_chip = copy.writeCopy(None)

        results = ResultFunction(self.chip)
        self.best_score = results.costs
        
        self.nets_to_fill = len(self.chip.netlist)
    
    def run(self, worst_x, y_reorganizations, loop_amount):
        """
        Picks the worst x wires, selects y of those, and tries to find new A* paths,
        and loops z times trying to find better solutions.
        """
        assert worst_x >= y_reorganizations

        counter = 0
        while counter != loop_amount:
            worst_nets = self.selectWorstNets(worst_x)
            investigations = self.selectRandomNets(worst_x, y_reorganizations, worst_nets)
            self.clearNets(investigations)

            # Make place deleted wires again using Asearch
            asearch = ASearch(self.chip)

            found_solution = asearch.run() and len(self.chip.solution.keys()) == self.nets_to_fill
            new_results = ResultFunction(self.chip)

            # In case found valid new better solution, update best_chip, else start over from best result found so far
            if new_results.costs <= self.best_score and found_solution:
                self.best_score = new_results.costs

                copy = CopyChip(self.chip)
                self.best_chip = copy.writeCopy(self.best_chip)
            else:
                copy = CopyChip(self.best_chip)
                self.chip = copy.writeCopy(self.chip)
            
            counter += 1

    def clear(self, net):
        """
        Marks wire (from given net) as unused,
        """
        wire = self.chip.solution[net]
        # Deintersect gridpoints in wire
        for point in wire.path:
            if not point.isGate():
                point.deIntersect()
        
        # Sets used gridsegment as unused
        for point, neighbour in zip(wire.path, wire.path[1:]):
            for move, relative in point.relatives.items():
                if neighbour == relative:
                    point.grid_segments[move].used = False
                    break
    
    def selectWorstNets(self, worst_x):
        """
        Selects the x worst net of an solution and returns them as a list
        """
        results = ResultFunction(self.chip)
        valued_wires = results.dictCostPerWire()
        worst_nets = []

        for i in range(worst_x):
            worst_net = max(valued_wires, key=valued_wires.get)
            worst_nets.append(worst_net)
            del valued_wires[worst_net]

        return worst_nets
    
    def selectRandomNets(self, worst_x, y_reorganizations, worst_nets):
        """
        Select random y nets, returns list containing them
        """
        investigations = []
        if worst_x == y_reorganizations:
            investigations = worst_nets
        else:
            while len(investigations) != y_reorganizations:
                net = random.choice(worst_nets)
                investigations.append(net)
                worst_nets.remove(net)
        return investigations
        
    def clearNets(self, investigations):
        """
        Clear the wires of given netlist
        """
        for net in investigations:
            self.clear(net)
            del self.chip.solution[net]