class SizeDeterminator():
    """
    Determines given a csv-file with gate coördinates, the width and height of the matching chip
    """
    def __init__(self, print_id):
        self.print_id = print_id
        
        self.width = None
        self.height = None

        self.determineSize()
        
    def determineSize(self):    
        with open(f"data/realdata/gates_netlists/chip_{self.print_id}/print_{self.print_id}.csv", "r") as inp:
            next(inp)
            width_list = []
            height_list = []
            for line in inp:
                location = list(map(int,line.rstrip("\n").split(",")))
                width_list.append(location[1])
                height_list.append(location[2])

            self.width = max(width_list)-min(width_list) + 3
            self.height = max(height_list)-min(height_list) + 3
    
    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height
        
    