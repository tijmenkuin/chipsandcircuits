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






def runGreedy(chip_id, netlist_id, n):
    solutions = []
    
    for _ in range(n):
        solution_found = False
        while not solution_found:
            chip = Chip(chip_id,netlist_id)
            greedysimultaneous = GreedySimultaneous(chip, 7)
            correct_solution = greedysimultaneous.run()
            if correct_solution:
                results = ResultFunction(chip)
                solution_found = True
                solutions.append((results, chip))
                
    solutions.sort(key=lambda x: x[0].costs)    

    print("--------------------------")
    print(f"Chip: '{chip_id}' Netlist: '{netlist_id}'")
    print("Beste resultaat kosten:", solutions[0][0].costs)

    CSVWriter(solutions[0][1].solution, "greedy_simultaneous", chip_id, netlist_id, solutions[0][0].costs)






def runASearch(chip_id, netlist_id, n):
    solutions = []
    
    for _ in range(n):
        solution_found = False
        while not solution_found:
            chip = Chip(chip_id,netlist_id)
            chip.netlistRandomizer()

            asearch = ASearch(chip)
            correct_solution = asearch.run()
            if correct_solution:
                results = ResultFunction(chip)
                solution_found = True
                solutions.append((results, chip))          

    solutions.sort(key=lambda x: x[0].costs)    

    print("--------------------------")
    print(f"Chip: '{chip_id}' Netlist: '{netlist_id}'")
    print("Beste resultaat kosten:", solutions[0][0].costs)

    CSVWriter(solutions[0][1].solution, "asearch", chip_id, netlist_id, solutions[0][0].costs)



def wrongUsageMessage():
    print("Wrong usage use: ")
    print("python main.py help")
    print("For more information")





def helpMessage():
    print("----------[HELP]----------")
    print("python main.py [algorithm] [iterations]")
    print("example: python main.py gs 10")
    print("example: python main.py asearch 50")
    print("")
    print("python main.py [algorithm] [chip_id] [net_id] [iterations]")
    print("example: python main.py as 2 9 100")
    print("")
    print("python main.py hc [algorithm] [chip_id] [net_id] [solution_score] [iterations]")
    print("python main.py hillclimber [algorithm] [chip_id] [net_id] [solution_score] [iterations]")
    print("example: python main.py hc greedy_simultaneous 2 9 51123 100")
    print("")
    print("python main.py view [algorithm] [chip_id] [netlist_id] [solution_score]")
    print("example: python main.py view asearch 2 9 32514")





def main(args):
    if len(args) == 1 and args[0] == "help":
        helpMessage()
    elif len(args) == 2:
        if args[0] == "greedy_simultaneous" or args[0] == "gs":
            print("Running Greedy Simultaneous")
            for i in range(9):
                chip_id = i//3
                netlist_id = i + 1
                try:
                    n = int(args[1])
                    runGreedy(chip_id, netlist_id, n)
                except:
                    wrongUsageMessage()
                    return
        elif args[0] == "asearch" or args[0] == "as":
            print("Running ASearch")
            for i in range(9):
                chip_id = i//3
                netlist_id = i + 1
                try:
                    n = int(args[1])
                    runASearch(chip_id,netlist_id,n)
                except:
                    wrongUsageMessage()
                    return
        else:
            wrongUsageMessage()
    elif len(args) == 4:
        if args[0] == "greedy_simultaneous" or args[0] == "gs":
            print("Running Greedy Simultaneous")
            try:
                chip_id = int(args[1])
                netlist_id = int(args[2])
                n = int(args[3])
                runGreedy(chip_id, netlist_id, n)
            except:
                wrongUsageMessage()
                return
        elif args[0] == "asearch" or args[0] == "as":
            print("Running ASearch")
            try:
                chip_id = int(args[1])
                netlist_id = int(args[2])
                n = int(args[3])
                runASearch(chip_id,netlist_id,n)
            except:
                wrongUsageMessage()
                return
        else:
            wrongUsageMessage()
    elif len(args) == 4 and args[0] == "view":
        if args[0] == "greedy_simultaneous" or args[0] == "gs":
            try:
                chip = SolutionToChip("greedy_simultaneous", int(args[1]), int(args[2]), int(args[3])).readResults()
                visualise(chip.solution)
            except:
                print("Could not visualise this solution!")
                return
        if args[0] == "asearch" or args[0] == "as":
            try:
                chip = SolutionToChip("asearch", int(args[1]), int(args[2]), int(args[3])).readResults()
                visualise(chip.solution)
            except:
                print("Could not visualise this solution!")
                return
        else:
            wrongUsageMessage()
    elif len(args) == 6 and (args[0] == "hc" or args[0] == "hillclimber"): 
        if args[1] == "greedy_simultaneous" or args[1] == "gs":
            try:
                chip = SolutionToChip("greedy_simultaneous", int(args[2]), int(args[3]), int(args[4])).readResults()
                result = ResultFunction(chip)
                print("kosten", result.costs)

                hillclimber = HillClimber(chip)
                print("Now running hill climber")
                hillclimber.run(len(chip.netlist),5,int(args[5]))
                result = ResultFunction(hillclimber.best_chip)
                print("--------------------------")
                print(f"Chip: '{int(args[2])}' Netlist: '{int(args[3])}'")
                print("Beste resultaat kosten:", result.costs)
                CSVWriter(chip.solution, "greedy_simultaneous", int(args[2]), int(args[3]), result.costs)

            except:
                print("Can not use hill climber on this solution!")
                return
        if args[1] == "asearch" or args[1] == "as":
            try:
                chip = SolutionToChip("asearch", int(args[2]), int(args[3]), int(args[4])).readResults()


                hillclimber = HillClimber(chip)
                print("Now running hill climber")
                hillclimber.run(len(chip.netlist),5,int(args[5]))
                result = ResultFunction(hillclimber.best_chip)
                print("--------------------------")
                print(f"Chip: '{int(args[2])}' Netlist: '{int(args[3])}'")
                print("Beste resultaat kosten:", result.costs)
                CSVWriter(chip.solution, "asearch", int(args[2]), int(args[3]), result.costs)
            except:
                print("Can not use hill climber on this solution!")
                return
        else:
            wrongUsageMessage()           
    else:
        wrongUsageMessage()

if __name__ == "__main__":
   main([arg.lower() for arg in sys.argv[1:]])
