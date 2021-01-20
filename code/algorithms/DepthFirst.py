from ..objects.chip import Chip
from ..objects.wire import Wire
from ..objects.gridSegment import GridSegment
import copy

class DepthFirst:
    """
    # no deeper than 'depth'
    # add begin direction to directions 

    # get one of the directions

    # stop condition
        # for each possible direction:
            # deepcopy this direction
            # make new child
            # put on directions
    """

    def __init__(self, chip):
        self.chip = chip
        self.n = n
        
    def get_best_distance(self, gate_a, gate_b):
        """
        Gets the best distance from each point to the next one.
        """
        self.Wire = directions
        for direction in directions:
            if direction.is_valid:


    def is_valid(self):
        """
        Checks if the move in a speciefiec direction is valid or not.
        """
        if .has_used():
            return False

        for relative in self.relatives.used():
            if relative.used == self.used:
                return False

        return True

    def check_solution(self):
        """
        Checks and accepts better solutions than the current solution.
        """

    def cost(self, grid_point, n):
        """
        Calculate the total cost of the netlist.
        C = n + 300 * K
        n the numbe of grid segments are used
        K number of intersection
        """
        self.grid_point = grid_point
        self.grid_point.intersect = K
        C = n + 300 * K
        return C


    def run(self, gate_a, gate_b):
        copynetlist = []

        self.chip.netlist = netlist 

        for net in netlist:
            copynetlist.append(net)        
            gate_a = net.target[0]
            gate_b = net.target[1]
