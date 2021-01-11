from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.algorithm1 import algorithm

if __name__ == "__main__":
    # chip = Chip(10,10)
    # chip.initializeNetlist(0,1)
    # chip.makeDict()
    # chip.giveResults()
    # chip.initializeGates(0)
    # chip.initializeNetList(0,1)
    # chip.gates[2].moveTo('backwards').moveTo('backwards').moveTo('right').moveTo('right').moveTo('right').moveTo('forwards').moveTo('forwards').moveTo('forwards').moveTo('forwards').moveTo('left')
    # chip.gates[0].moveTo('right').moveTo('right').moveTo('up').moveTo('right').moveTo('right').moveTo('down').moveTo('right')
    # visualise(chip, 0)
    # tim.visualise(chip, 0)
    # tim.visualise(chip, 1)
    algorithm()

