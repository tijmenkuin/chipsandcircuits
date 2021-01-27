from ..objects.chip import Chip
from ..objects.net import Net
from ..objects.wire import Wire


class CopyChip():
    """
    Makes a copy of a given chip in an (non)existing chip
    """
    def __init__(self, chip):
        self.chip = chip

    def writeCopy(self, chip_to_write_in):
        """
        Writes a complete new dummy chip, by copying the given chip
        """
        if chip_to_write_in == None:
            dummy_chip = Chip(self.chip.chip_id, self.chip.netlist_id)
            dummy_chip.netlist = []
        else:
            chip_to_write_in.clear()
            dummy_chip = chip_to_write_in

        for net, wire in self.chip.solution.items():
            # copies nets
            point1 = net.target[0]
            point2 = net.target[1]
            dummy_gate1 = dummy_chip.getGridPoint(point1.x, point1.y, point1.z)
            dummy_gate2 = dummy_chip.getGridPoint(point2.x, point2.y, point2.z)
            dummy_net = Net(dummy_gate1, dummy_gate2)
            dummy_chip.netlist.append(dummy_net)
            # chip_to_write_in.netlist.append(dummy_net)

            # copies wires
            new_wire = Wire()
            for point in wire.path:
                dummy_point = dummy_chip.getGridPoint(point.x, point.y, point.z)
                # dummy_point = chip_to_write_in.getGridPoint(point.x, point.y, point.z)
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

