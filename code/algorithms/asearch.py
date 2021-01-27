from ..objects.chip import Wire
import random

class ASearch():
    def __init__(self, chip):
        self.chip = chip
        self.queue = dict()
        self.came_from = dict()

    def run(self):
        """
        Loops over netlist, and finds paths. After found resets the necessary in chip.
        Returns True is solution is found, else false
        """
        for net in self.chip.netlist:
            if net not in self.chip.solution:
                new_wire = self.findPath(net)
                if new_wire == []:
                    return False
                
                wire = Wire()
                for point in new_wire:
                    wire.addPoint(point)
                
                self.chip.solution[net] = wire
                self.markPath(wire)

                self.queue = dict()
                self.came_from = dict()
        return True

    def findPath(self, net):
        """
        Returns cheapest path that connects net
        """
        start_point = net.target[0]
        end_point = net.target[1]

        self.chip.giveManhattanHeuristicValues(end_point)
        self.chip.giveDefaultGScores()

        self.queue[start_point] = start_point.heuristic_value

        start_point.gscore = 0
        start_point.fscore = start_point.heuristic_value

        while self.queue != {}:
            current = min(self.queue, key=self.queue.get)
            
            if current == end_point:
                return self.reconstructPath(current)
            
            del self.queue[current]

            for relative in current.reachableRelatives(end_point):
                tentative_gScore = current.gscore + 1 + 300 * relative.isIntersected2()

                
                if tentative_gScore < relative.gscore:
                    self.came_from[relative] = current
                    relative.gscore = tentative_gScore
                    relative.fscore = relative.gscore + relative.heuristic_value
                    
                    if relative not in self.queue.keys():
                        self.queue[relative] = relative.fscore
        return []

    def reconstructPath(self, point):
        """
        Builds the path given the parents parents of final point
        """
        total_path = [point]

        while point in self.came_from.keys():
            point = self.came_from[point]
            total_path.insert(0, point)

        return total_path

    def markPath(self, wire):
        """
        Marks the used gridsegments and pass gridpoints for a wire
        """
        for point, neighbour in zip(wire.path, wire.path[1:]):
            for move, relative in point.relatives.items():
                if neighbour == relative:
                    point.grid_segments[move].used = True
                    break

        for point in wire.path:
            if not point.isGate():
                point.intersect()