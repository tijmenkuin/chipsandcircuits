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

import numpy as np


if __name__ == "__main__":
    chip_id = 2
    netlist_id = 9

    chip = SolutionToChip("hillclimber_asearch", chip_id,netlist_id, 1229).readResults()

    print("LowerBound:",lowerBound(chip))
    

    hillclimber = HillClimber(chip)
    hillclimber.run(len(chip.netlist),5,3000)

    results = ResultFunction(hillclimber.best_solution)

    print("-------------------------------------")
    print("Beste resultaat Kosten:", results.costs)
    print("Beste resultaat Intersecties:", results.intersections)
    print("Beste resultaat Lengte:", results.length)
    visualise(hillclimber.best_solution)

    csvwriter = CSVWriter(hillclimber.best_solution.solution, "hillclimber_asearch", chip_id, netlist_id, results.costs)




