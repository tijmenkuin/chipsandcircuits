from code.objects.chip import Chip
from code.objects.wire import Wire
from code.objects.net import Net
from code.visualisation.visualise import visualise
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.algorithms.Aster import A_star


import numpy as np
 
def main(args):
    if len(args) == 4:
        chip = Chip(int(args[0]),int(args[1]))
        chip.initializeGates(args[2])
        chip.initializeNetlist(args[2],args[3])
        algorithmTim.StartersAlgoritme(chip)
        start = args[2]
        end = args[3]
        path = A_star(chip, start, end)

    else:
        print("Wrong usage: python main.py [width] [height] [chip] [netlist]")

