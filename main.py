from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms import algorithm1

if __name__ == "__main__":
    chip = Chip(10,10)
    chip.initializeGates(0)
    # chip.initializeNetList(0,1)
    visualise(chip, 0)
    # algorithm1.StartersAlgoritme(chip)