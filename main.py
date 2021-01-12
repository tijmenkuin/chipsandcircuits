from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.starter import starter
from code.costfunction import costfunction

if __name__ == "__main__":
    # tim.visualise(chip, 0)
    LOOP_AMOUNT = 100

    for i in range(3):
        for j in range(3):
            gem = 0
            for k in range(LOOP_AMOUNT):
                netlist = j + 1 + (3 * i)
                chip = Chip(22,22)
                chip.initializeGates(i)
                chip.initializeNetlist(i, netlist)
                gem += starter(chip)
            print("Gevonden resultaat voor chip", i, "en netlist", netlist, "is:")
            print(gem / LOOP_AMOUNT * 100)


    # print(costfunction(chip))

    # tim.visualise(chip, 0)
    # tim.visualise(chip, 1)
