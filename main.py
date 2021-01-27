"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

main.py

Chips and Circuits 2021
"""

from code.objects.chip import Chip
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.utils.csv_writer import CSVWriter
from code.utils.result_function import ResultFunction
from code.visualisation.visualise import visualise
from code.algorithms.hill_climber import HillClimber
from code.algorithms.a_search import ASearch
from code.utils.solution_reader import SolutionToChip

import sys
import time


def runAlgorithm(algorithm, chip_id, netlist_id, amount_solutions):
    """
    Run specified algorithm and save best solution
    """ 

    print(f"Running: {algorithm}")
    solutions = []
    
    for _ in range(amount_solutions):
        solution_found = False
        while not solution_found:
            chip = Chip(chip_id,netlist_id)

            if algorithm.lower() == "greedy_simultaneous":
                
                # Value can be changed
                depth_search = 7

                greedysimultaneous = GreedySimultaneous(chip, depth_search)
                correct_solution = greedysimultaneous.run()
            elif algorithm.lower() == "asearch":
                asearch = ASearch(chip)
                correct_solution = asearch.run()
            else:
                wrongUsageMessage()
                return
            if correct_solution:
                result = ResultFunction(chip)
                solution_found = True
                print(result.costs)
                solutions.append((result, chip))
                
    solutions.sort(key=lambda x: x[0].costs)    
    printResult(solutions[0][1], solutions[0][0], algorithm)


def runHillClimber(algorithm, chip_id, netlist_id, score, amount_solutions):
    """
    Run Hill Climber algorithm and save best solution
    """ 
    print("Running Hill Climber")

    chip = SolutionToChip(algorithm, chip_id, netlist_id, score).readResults()
    hillclimber = HillClimber(chip)

    # Values can be changed
    x = len(chip.netlist)
    y = 5

    hillclimber.run(x, y, amount_solutions)
    result = ResultFunction(hillclimber.best_chip)
    printResult(chip, result, algorithm)


def printResult(chip, result, algorithm):
    """
    Print result and save CSV-file
    """
    print("--------------------------")
    print(f"Chip: '{chip.chip_id}' Netlist: '{chip.netlist_id}'")
    print("Beste resultaat kosten:", result.costs)

    CSVWriter(chip.solution, algorithm, chip.chip_id, chip.netlist_id, result.costs)


def wrongUsageMessage():
    print("Wrong usage use: ")
    print("python main.py help")
    print("For more information")

def helpMessage():
    print("----------[HELP]----------")
    print("python main.py [algorithm] [amount_solutions]")
    print("example: python main.py gs 10")
    print("example: python main.py asearch 50")
    print("")
    print("python main.py [algorithm] [chip_id] [net_id] [amount_solutions]")
    print("example: python main.py as 2 9 100")
    print("")
    print("python main.py hc [algorithm] [chip_id] [net_id] [solution_score] [amount_solutions]")
    print("python main.py hillclimber [algorithm] [chip_id] [net_id] [solution_score] [amount_solutions]")
    print("example: python main.py hc greedy_simultaneous 2 9 51123 100")
    print("")
    print("python main.py view [algorithm] [chip_id] [netlist_id] [solution_score]")
    print("example: python main.py view asearch 2 9 32514")

def main(args):
    """
    Checks the arguments and returns messages, executes algorithms or view solution.
    """
    if len(args) == 1 and args[0] == "help":
        helpMessage()
    elif len(args) == 2:
        if args[0] == "greedy_simultaneous" or args[0] == "gs":
            for i in range(9):
                try:
                    runAlgorithm("greedy_simultaneous" ,int(i//3), int(i + 1), int(args[1]))
                except:
                    wrongUsageMessage()
                    return
        elif args[0] == "asearch" or args[0] == "as":
            for i in range(9):
                try:
                    runAlgorithm("asearch" ,int(i//3), int(i + 1), int(args[1]))
                except:
                    wrongUsageMessage()
                    return
        else:
            wrongUsageMessage()
    elif len(args) == 4:
        if args[0] == "greedy_simultaneous" or args[0] == "gs":
            try:
                runAlgorithm("greedy_simultaneous" ,int(args[1]), int(args[2]), int(args[3]))
            except:
                wrongUsageMessage()
                return
        elif args[0] == "asearch" or args[0] == "as":
            try:
                runAlgorithm("asearch" ,int(args[1]), int(args[2]), int(args[3]))
            except:
                wrongUsageMessage()
                return
        else:
            wrongUsageMessage()
    elif len(args) == 5 and args[0] == "view":
        if args[1] == "greedy_simultaneous" or args[1] == "gs":
            try:
                chip = SolutionToChip("greedy_simultaneous", int(args[2]), int(args[3]), int(args[4])).readResults()
                visualise(chip)
            except:
                print("Could not visualise this solution!")
                return
        elif args[1] == "asearch" or args[1] == "as":
            try:
                chip = SolutionToChip("asearch", int(args[2]), int(args[3]), int(args[4])).readResults()
                visualise(chip)
            except:
                print("Could not visualise this solution!")
                return
        else:
            wrongUsageMessage()
    elif len(args) == 6 and (args[0] == "hc" or args[0] == "hillclimber"): 
        if args[1] == "greedy_simultaneous" or args[1] == "gs":
            try:
                runHillClimber("greedy_simultaneous", int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            except:
                print("Can not use hill climber on this solution!")
                return
        elif args[1] == "asearch" or args[1] == "as":
            try:
                runHillClimber("asearch", int(args[2]), int(args[3]), int(args[4]), int(args[5]))
            except:
                print("Can not use hill climber on this solution!")
                return
        else:
            wrongUsageMessage()           
    else:
        wrongUsageMessage()

if __name__ == "__main__":
   main([arg.lower() for arg in sys.argv[1:]])
