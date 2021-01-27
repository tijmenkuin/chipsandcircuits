from ..objects.chip import Wire

class ASearch():
    """
    Algorithm that uses A*-search for finding the cheapest paths for each net
    """
    def __init__(self, chip):
        self.chip = chip
        self.queue = dict()
        self.came_from = dict()

    def run(self):
        """
        Loops over netlist, and finds paths. After found one resets the necessary in chip.
        Returns True if solution is found, else False
        """
        for net in self.chip.netlist:
            # Extra check in case used by Hill Climber
            if net not in self.chip.solution:
                new_wire = self.findPath(net)
                if new_wire == None:
                    return False
                
                # Make wire and add to solution
                wire = Wire()
                for point in new_wire:
                    wire.addPoint(point)
                self.chip.solution[net] = wire
                
                # Make chip ready for finding next wire
                self.markPath(wire)
                self.queue = dict()
                self.came_from = dict()
        return True

    def findPath(self, net):
        """
        Returns cheapest path that connects a net
        """
        start_point = net.target[0]
        end_point = net.target[1]

        # Initialize gridpoints with default g and h values 
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

            # Add relatives to queue and update gscore if necessary
            for relative in current.reachableRelatives(end_point):
                tentative_gScore = current.gscore + 1 + 300 * relative.isIntersected2()
                
                if tentative_gScore < relative.gscore:
                    self.came_from[relative] = current
                    relative.gscore = tentative_gScore
                    relative.fscore = relative.gscore + relative.heuristic_value
                    
                    if relative not in self.queue.keys():
                        self.queue[relative] = relative.fscore

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
        Marks the used gridsegments and passed gridpoints by a wire
        """
        # Marks gridsegments
        for point, neighbour in zip(wire.path, wire.path[1:]):
            for move, relative in point.relatives.items():
                if neighbour == relative:
                    point.grid_segments[move].used = True
                    break

        # Intersects gridpoints
        for point in wire.path:
            if not point.isGate():
                point.intersect()