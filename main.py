from code.objects.chip import Chip

if __name__ == "__main__":
    chip = Chip(4,5)
    chip.initializeGrid()
    chip.initializeGates(0)
    chip.initializeNetList(0,1)
    print(chip.netlist)
