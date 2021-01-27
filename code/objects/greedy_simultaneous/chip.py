from ..chip import Chip

class GreedyChip(Chip):
    def __init__(self, chip_id, netlist_id):
        super().__init__(chip_id, netlist_id)
        self.graduationyear = 2019