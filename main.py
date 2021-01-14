from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.greedy import Greedy
from code.algorithms.greedy_ext import greedy_ext
from code.costfunction import costfunction

import random
import numpy as np

if __name__ == "__main__":
    LOOP_AMOUNT = 100

    # gem = 0
    # for k in range(LOOP_AMOUNT):
    #     print(k)
    #     chip = Chip(22,22)
    #     chip.initializeGates(1)
    #     chip.initializeNetlist(1, 6)

    #     random.shuffle(chip.netlist)

    #     gem += greedy_ext(chip)

    # print("Gevonden resultaat voor chip 1 en netlist 6 is:")
    # print(gem)

    for i in range(3):
        for j in range(3):
            gem = 0
            for k in range(LOOP_AMOUNT):
                netlist = j + 1 + (3 * i)
                chip = Chip(22,22)
                chip.initializeGates(i)
                chip.initializeNetlist(i, netlist)
                gem += greedy_ext(chip)
            print("Gevonden resultaat voor chip", i, "en netlist", netlist, "is:")
            print(gem / LOOP_AMOUNT * 100)
