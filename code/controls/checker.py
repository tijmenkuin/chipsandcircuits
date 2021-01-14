from ..objects.chip import Chip
from ..objects.wire import Wire

class Checker():
    """
    Checks whether a solution is a valid solution, makes three checks:
    - There are no collisions in the solution
    - The wires are connected paths, which connect the wright gates

    Checks are done by simulating the made paths in dummy chip
    """
    def __init__(self, solution, chip_number, netlist_number, width, height):
        self.solution = solution

        self.chip = None
        self.chipBuild(width, height, chip_number, netlist_number)

        self.collision_troubles = dict()
        self.connection_troubles = list()

        self.solutionCheck()
    
    def chipBuild(self, width, height, chip_number, netlist_number):
        """
        Builds dummy chip
        """
        self.chip = Chip(width, height)
        self.chip.initializeGrid()
        self.chip.initializeGates(chip_number)

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

    def giveResults(self):
        if self.collision_troubles == {} and self.connection_troubles == []:
            print("Congrats, no collision or connection errors found")
        elif self.collision_troubles != {} and self.connection_troubles != []:
            print("Oops, there are found some connection and collision errors found")
            print("Connection errors:")
            print(f"{self.connection_troubles}")
            print("Collision errors:")
            print(f"{self.collision_troubles}")
        elif self.collision_troubles != {} and self.connection_troubles == []:
            print("Oops, there are found some collision errors found")
            print("Collision errors:")
            print(f"{self.collision_troubles}")
        else:
            print("Oops, there are found some connection errors found")
            print("Connection errors:")
            print(f"{self.connection_troubles}")



                    
                
                