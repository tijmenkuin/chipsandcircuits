class Chip():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.depth = 7
        self.cost = 0
        self.grid = {}
        self.netlist = []
        self.wires = {}


#test