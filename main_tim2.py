from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.asearch_tim import ASearch
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.resultfunction import ResultFunction
from code.visualisation.visualise import visualise
from code.optimizations.hillclimber import HillClimber
from code.utils.solution_reader import SolutionToChip
from code.utils.lower_bound import lowerBound

from random import randrange

import numpy as np

import sys
import time


def main(args):
    print("test1")

    for i in range(9):



        runtime = time.time() 
        
        netlist_id = i+1
        chip_id = i//3

        r = []

  

        seconds = 60

        while (time.time() - runtime) < seconds:            
            chip = Chip(chip_id,netlist_id)
            asearch = ASearch(chip)
            asearch.run()
            if (time.time() - runtime) > seconds:
                break
            results = ResultFunction(chip)
            r.append(results.costs)

        print(f"Chip: {chip_id} Netlist: {netlist_id}")
        print("Lowest:", min(r))
        print("Average:", np.mean(r))
        print("Variance:", np.var(r))
        print("Solutions:", len(r))

    return

    if len(args) == 2:
        pass
        # while True:
        #     chip = SolutionToChip("hillclimber_asearch", chip_id,netlist_id, 351).readLowest()
        #     # chip = Chip(args[0],args[1])
        #     # asearch = ASearch(chip)

        #     # if asearch.run():
        #     print("LowerBound:",lowerBound(chip))
        
        #     hillclimber = HillClimber(chip)
        #     hillclimber.run(len(chip.netlist),5,500)

        #     results = ResultFunction(hillclimber.best_solution)

        #     print("-------------------------------------")
        #     print("Beste resultaat Kosten:", results.costs)
        #     print("Beste resultaat Intersecties:", results.intersections)
        #     print("Beste resultaat Lengte:", results.length)
        #     visualise(hillclimber.best_solution)

        #     csvwriter = CSVWriter(hillclimber.best_solution.solution, "hillclimber_asearch", chip_id, netlist_id, results.costs)
    else:
        print("Wrong usage: python main_tim2.py [chip] [netlist]")

if __name__ == "__main__":
   main(sys.argv[1:])