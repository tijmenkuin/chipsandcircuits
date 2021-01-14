from code.objects.chip import Chip
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.greedy_ext import greedy_ext
from code.costfunction import costfunction
from code.algorithms import algorithmTim

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
   main(sys.argv[1:])

