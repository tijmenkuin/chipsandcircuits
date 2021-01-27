from code.objects.chip import Chip
#from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.algorithms.asearch import ASearch
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.resultfunction import ResultFunction
from code.visualisation.visualise import visualise
from code.algorithms.hillclimber import HillClimber
from code.utils.solution_reader import SolutionToChip

from random import randrange

import numpy as np

import sys
import time


def main(args):

    chip = Chip(2,9)
    gd = GreedySimultaneous(chip, 7)

    test = gd.run()
    if test:
        results = ResultFunction(chip)
        print(chip.solution)
        print(results.costs)
        visualise(chip)
        csvwriter = CSVWriter(chip.solution, "greedy_simultaneous", 2, 9, results.costs)

    return

    # chip = Chip(2,8)
    # asearch = ASearch(chip)
    # asearch.run()
    # results = ResultFunction(chip)

    # csvwriter = CSVWriter(chip.solution, "hillclimber_asearch", 2,8, results.costs)

    # return

    if len(args) == 2:
        while True:
            chip_id = args[0]
            netlist_id = args[1]

            chip = SolutionToChip("hillclimber_asearch", chip_id,netlist_id, 351).readLowest()
            # chip = Chip(args[0],args[1])
            # asearch = ASearch(chip)

            # if asearch.run():
            #print("LowerBound:",lowerBound(chip))
        
            hillclimber = HillClimber(chip)
            hillclimber.run(len(chip.netlist),5,500)

            results = ResultFunction(hillclimber.best_solution)

            print("-------------------------------------")
            print("Beste resultaat Kosten:", results.costs)
            print("Beste resultaat Intersecties:", results.intersections)
            print("Beste resultaat Lengte:", results.length)
            #visualise(hillclimber.best_solution)

            csvwriter = CSVWriter(hillclimber.best_solution.solution, "hillclimber_asearch", chip_id, netlist_id, results.costs)
    else:
        print("Wrong usage: python main_tim2.py [chip] [netlist]")

if __name__ == "__main__":
   main(sys.argv[1:])