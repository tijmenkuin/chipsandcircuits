from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim

if __name__ == "__main__":
    chip = Chip(10,10)
    chip.initializeGates(0)
    chip.initializeNetList(0,1)
    chip.getGridPoint(1,3,0).gate_id = 1
    chip.getGridPoint(2,4,0).gate_id = 2
    chip.getGridPoint(0,3,0).gate_id = 3
    visualise(chip, 0)
    print(chip.netlist)
    # tim.visualise(chip, 0)