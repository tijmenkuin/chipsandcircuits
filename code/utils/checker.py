from ..objects.chip import Chip

class Checker():
    """
    Checks whether a solution is a valid solution, makes three checks:
    - There are no collisions in the solution
    - The wires are connected paths, which connect the wright gates
    - Amount wires in chip are correct

    Checks are done by simulating the made paths in dummy chip
    """
    def __init__(self, solution, chip_number, netlist_number):
        self.solution = solution

        self.chip = Chip(chip_number, netlist_number)
        
        self.collision_troubles = dict()
        self.connection_troubles = list()

    def isValid(self):
        return self.solutionCheck() and self.allNetsIn()
    
    def allNetsIn(self):
        return len(self.chip.netlist) == len(self.solution.keys())

    def solutionCheck(self):
        """
        Moves through the solutions wires and does the checks,
        sets the attributes troubles
        """
        for net, wire in self.solution.items():
            for point, neighbour in zip(wire.path, wire.path[1:]):
                dummy_point = self.chip.getGridPoint(point.x, point.y, point.z)
                dummy_neighbour = self.chip.getGridPoint(neighbour.x, neighbour.y, neighbour.z)

                found = False
                for move, relative in dummy_point.relatives.items():
                    if dummy_neighbour == relative:
                        if dummy_point.grid_segments[move].used:
                            self.collision_troubles[net] = dummy_point.grid_segments[move]
                            found = True
                            break
                        else:
                            dummy_point.grid_segments[move].used = True
                            found = True
                            break
                   
                if not found:
                    if self.connection_troubles == []:
                        self.connection_troubles = [net]
                    else:
                        self.connection_troubles.append(net)

        return self.collision_troubles == {} and self.connection_troubles == []