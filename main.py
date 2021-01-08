from code.objects.chip import Chip
from code.visualisation import tim

if __name__ == "__main__":
    chip = Chip(10,10)
    chip.initializeGates(0)
    chip.initializeNetList(0,1)
    tim.visualise(chip, 0)

    

