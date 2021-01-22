import csv
from ..objects.chip import Chip
from ..objects.wire import Wire
from ..objects.net import Net

class SolutionToChip():
    """
    Writes a csv-file for a given solution, takes 4 extra arguments for orderly inventory

    NOTE : Before usage make sure the directories in writeResults-method exist !!
    """
    def __init__(self, algorithm, chip, netlist, score):
        self.score = score

        self.algorithm = algorithm
        self.score = score
        self.chip = chip
        self.netlist = netlist

    def readResults(self):
        chip = Chip(self.chip, self.netlist)

        with open(f"solutions/{self.algorithm}/chip_{self.chip}/netlist_{self.netlist}/{self.score}.csv", "rt", newline="") as csv_file:
            for row in csv_file:
                if (len(row.split('","')) == 2):

                    net = row.split('","')[0].replace('"(', '').replace(')', '')
                    wire_temp = row.split('","')[1].replace('"', '').replace('[', '').replace(']', '').rstrip().split('),(')
                    wire_temp = [wire_piece.replace(')', '').replace('(', '') for wire_piece in wire_temp]

                    wire_path = [chip.getGridPoint(int(wp.split(',')[0]),int(wp.split(',')[1]),int(wp.split(',')[2])) for wp in wire_temp]
                    net_gate_1 = chip.gates[int(net.split(',')[0])]
                    net_gate_2 = chip.gates[int(net.split(',')[1])]

                    wire = Wire()

                    wire.path = wire_path

                    chip.solution[Net(net_gate_1,net_gate_2)] = wire

        return chip