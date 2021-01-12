from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.asearch import asearchalg
from code.costfunction import costfunction

if __name__ == "__main__":
    chip = Chip(22,22)
    chip.initializeGates(1)
    chip.initializeNetlist(1,4)
    # tim.visualise(chip, 0)
    asearchalg(chip)

    print(costfunction(chip))

    # tim.visualise(chip, 0)
    # tim.visualise(chip, 1)
