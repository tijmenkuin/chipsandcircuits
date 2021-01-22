from ..utils.resultfunction import ResultFunction
from ..objects.chip import Chip
from ..objects.net import Net
from ..objects.wire import Wire
from ..algorithms.asearch_tijm import ASearch
from ..utils.csv_writer import CSVWriter


import random

class HillClimber():
    def __init__(self, chip):
        """
        Given a chip with a solution, runs for finding better solutions
        """
        self.chip = None

        self.best_solution = None

        self.initialize(chip)

        self.results = ResultFunction(self.chip)
        print(self.results.costs)

    def initialize(self, chip):
        """
        Writes the dummies to work in
        """
        self.chip = self.writeDummyChip(chip)
        self.best_solution = self.writeDummyChip(chip)

    def writeDummyChip(self, chip):
        """
        Writes a complete new dummy chip, to work with
        """
        dummy_chip = Chip(chip.chip_id, chip.netlist_id)
        dummy_chip.netlist = []

        for net, wire in chip.solution.items():
            # copies nets
            point1 = net.target[0]
            point2 = net.target[1]
            dummy_gate1 = dummy_chip.getGridPoint(point1.x, point1.y, point1.z)
            dummy_gate2 = dummy_chip.getGridPoint(point2.x, point2.y, point2.z)
            dummy_net = Net(dummy_gate1, dummy_gate2)
            dummy_chip.netlist.append(dummy_net)

            # copies wires
            new_wire = Wire()
            for point in wire.path:
                dummy_point = dummy_chip.getGridPoint(point.x, point.y, point.z)
                new_wire.addPoint(dummy_point)

                # copies passed gridpoints
                if not dummy_point.isGate():
                    dummy_point.intersect()

            dummy_chip.solution[dummy_net] = new_wire

            for point, neighbour in zip(wire.path, wire.path[1:]):
                dummy_point = dummy_chip.getGridPoint(point.x, point.y, point.z)
                dummy_neighbour = dummy_chip.getGridPoint(neighbour.x, neighbour.y, neighbour.z)

                # copies used gridsegments
                for move, relative in dummy_point.relatives.items():
                    if dummy_neighbour == relative:
                        dummy_point.grid_segments[move].used = True
                        break
        
        dummy_chip.giveDefaultGScores()
        return dummy_chip    
    
    def run(self, worst_x, y_reorganizations, loop_amount):
        """
        Picks the worst x wire, selects y of those, and tries to find new A* paths,
        and loops z times trying to find better solutions.
        """
        counter = 0
        while counter != loop_amount:
            worst_nets = self.selectWorstNets(worst_x)

            investigations = []

            while len(investigations) != y_reorganizations:
                net = random.choice(worst_nets)
                if net not in investigations:
                    investigations.append(net)
            
            for net in investigations:
                self.clear(net)
                del self.chip.solution[net]

            asearch = ASearch(self.chip)
            asearch.run()

            new_results = ResultFunction(self.chip)

            if new_results.costs < self.results.costs:
                self.results = new_results
                self.updateChip(self.best_solution, self.chip)
            else:
                problem = True
                self.updateChip(self.chip, self.best_solution)
            
            counter += 1 

    def clear(self, net):
        wire = self.chip.solution[net]
        for point in wire.path:
            if not point.isGate():
                point.deIntersect()

        for point, neighbour in zip(wire.path, wire.path[1:]):
            for move, relative in point.relatives.items():
                if neighbour == relative:
                    point.grid_segments[move].used = False
                    break
    
    def selectWorstNets(self, worst_x):
        self.results = ResultFunction(self.chip)
        valued_wires = self.results.dictCostPerWire()
        worst_nets = []

        for i in range(worst_x):
            worst_net = max(valued_wires, key=valued_wires.get)
            worst_nets.append(worst_net)
            del valued_wires[worst_net]

        return worst_nets

    def updateChip(self, chip1, chip2):
        """
        Updates chip1 with chip2
        """
        chip1.clear()

        for net, wire in chip2.solution.items():
            # copies nets
            point1 = net.target[0]
            point2 = net.target[1]
            dummy_gate1 = chip1.getGridPoint(point1.x, point1.y, point1.z)
            dummy_gate2 = chip1.getGridPoint(point2.x, point2.y, point2.z)
            dummy_net = Net(dummy_gate1, dummy_gate2)
            chip1.netlist.append(dummy_net)

            # copies wires
            new_wire = Wire()
            for point in wire.path:
                dummy_point = chip1.getGridPoint(point.x, point.y, point.z)
                new_wire.addPoint(dummy_point)

                # copies passed gridpoints
                if not dummy_point.isGate():
                    dummy_point.intersect()

            chip1.solution[dummy_net] = new_wire

            for point, neighbour in zip(wire.path, wire.path[1:]):
                dummy_point = chip1.getGridPoint(point.x, point.y, point.z)
                dummy_neighbour = chip1.getGridPoint(neighbour.x, neighbour.y, neighbour.z)

                # copies used gridsegments
                for move, relative in dummy_point.relatives.items():
                    if dummy_neighbour == relative:
                        dummy_point.grid_segments[move].used = True
                        break