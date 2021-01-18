from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.costfunction import CostFunction
from code.visualisation.visualise import visualise

import sys

def main(args):
    if len(args) == 4:
        chip = Chip(int(args[0]),int(args[1]))
        chip.initializeGates(args[2])
        chip.initializeNetlist(args[2],args[3])
        algorithmTim.StartersAlgoritme(chip)
        tim.visualise(chip, 0)
        tim.visualise(chip, 1)
    else:
        print("Wrong usage: python main.py [width] [height] [chip] [netlist]")

if __name__ == "__main__":
#    main(sys.argv[1:])
    # LOOP_AMOUNT = 100
    
    # for i in range(3):
    #     for j in range(3):
    #         gem = 0
    #         for k in range(LOOP_AMOUNT):
    #             netlist = j + 1 + (3 * i)
    #             chip = Chip(22,22)
    #             chip.initializeGates(i)
    #             chip.initializeNetlist(i, netlist)
    #             gem += greedy_ext(chip)
    #         print("Gevonden resultaat voor chip", i, "en netlist", netlist, "is:")
    #         print(gem / LOOP_AMOUNT * 100)
    
    chip = Chip(0,2)
    greedy_ext(chip)

    print(chip.solution)

    visualise(chip, chip.solution)
    
    # greedy_ext(chip)
    # score = costfunction(chip)

    # print(chip.solution)
    # costs = CostFunction(chip.solution)
    
    # write = CSVWriter(chip.solution, "greedy_ext", 0, 1, score)