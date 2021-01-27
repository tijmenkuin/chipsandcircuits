from code.objects.chip import Chip
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.utils.csv_writer import CSVWriter
from code.utils.result_function import ResultFunction
from code.visualisation.visualise import visualise
from code.algorithms.hill_climber import HillClimber
from code.utils.solution_reader import SolutionToChip

import sys
import time


def main(args):

    for i in range(9):

        chip_id = i//3
        netlist_id = i + 1
        n = 10

        solutions = []
        
        for _ in range(n):
            solution_found = False
            while not solution_found:
                chip = Chip(chip_id,netlist_id)
                gd = GreedySimultaneous(chip, 7)
                correct_solution = gd.run()
                if correct_solution:
                    results = ResultFunction(chip)
                    solution_found = True
                    solutions.append((results, chip))
                    


        solutions.sort(key=lambda x: x[0].costs)    

        print("-------------------------------------")
        print(f"Chip: '{chip_id}' Netlist: '{netlist_id}'")
        print("Beste resultaat kosten:", solutions[0][0].costs)


        CSVWriter(solutions[0][1].solution, "greedy_simultaneous", chip_id, netlist_id, solutions[0][0].costs)

    # if len(args) == 2:
    #     while True:
    #         chip_id = args[0]
    #         netlist_id = args[1]

    #         chip = SolutionToChip("hillclimber_asearch", chip_id,netlist_id, 351).readResults()

    #         hillclimber = HillClimber(chip)
    #         hillclimber.run(len(chip.netlist),5,500)

    #         results = ResultFunction(hillclimber.best_solution)

    #         print("-------------------------------------")
    #         print("Beste resultaat Kosten:", results.costs)
    #         print("Beste resultaat Intersecties:", results.intersections)
    #         print("Beste resultaat Lengte:", results.length)

    #         csvwriter = CSVWriter(hillclimber.best_solution.solution, "hillclimber_asearch", chip_id, netlist_id, results.costs)
    # else:
    #     print("Wrong usage: python main_tim2.py [chip] [netlist]")

if __name__ == "__main__":
   main(sys.argv[1:])