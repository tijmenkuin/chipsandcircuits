from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.asearch_tim import ASearch
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.resultfunction import ResultFunction
from code.visualisation.visualise import visualise
from code.optimizations.hillclimber import HillClimber

import numpy as np

from datetime import datetime



if __name__ == "__main__":

    AMOUNT_SOLUTIONS = 25

    LOOP_AMOUNT = 20000

    start=datetime.now()


    # for i in range(3):
    #     for j in range(3):
    #         gem = 0
    #         for k in range(LOOP_AMOUNT):
    #             netlist_id = j + 1 + (3 * i)
    #             chip = Chip(i, netlist_id)
    #             gem += greedy_ext(chip)
    #         print("Gevonden resultaat voor chip", i, "en netlist", netlist_id, "is:")
    #         print(gem)

    # amount_solutions = 0
    # total_costs = 0

    # while AMOUNT_SOLUTIONS != amount_solutions:
    #     chip = Chip(0,2)
    #     if greedy_ext(chip):
    #         cost = CostFunction(chip.solution, chip.amount_intersections)
    #         total_costs += cost.costs
    #         amount_solutions += 1
        
    # print("Gemiddelde kosten is:", total_costs / AMOUNT_SOLUTIONS)

    # for i in range(3):
    #     for j in range(3):
    #         if i == 0:
    #             continue 
    #         netlist_id = j + 1 + (3 * i)
    #         amount_solutions = 0
    #         costs = []
    #         amount_intersections = []
    #         count = 0
    #         breaked = False

    #         while AMOUNT_SOLUTIONS != amount_solutions:
    #             count += 1
    #             chip = Chip(i, netlist_id)
    #             # chip.netlistRandomizer()
    #             chip.netlistOrder()
    #             asearch = ASearch(chip)
    #             if asearch.run():
    #                 result = ResultFunction(chip)
    #                 if count == 1 or result.costs < min(costs):
    #                     writer = CSVWriter(chip.solution, "asearch", i, netlist_id, result.costs)
    #                     costs.append(result.costs)
    #                 amount_intersections.append(result.intersections)
    #                 amount_solutions += 1
    #             if count == LOOP_AMOUNT:
    #                 breaked = True
    #                 break
  
            
    #         if not breaked:
    #             print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
    #             print("Gemiddelde kosten:", np.mean(costs))
    #             print("Gemiddeld aantal intersecties:", np.mean(amount_intersections))
    #             print("Minimale kosten:", min(costs))
    #             print("Minimale aantal intersecties:", min(amount_intersections))
    #         elif amount_solutions != 0:
    #             print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, f"over {amount_solutions} oplossingen:")
    #             print("Gemiddelde kosten:", np.mean(costs))
    #             print("Gemiddeld aantal intersecties:", np.mean(amount_intersections))
    #             print("Minimale kosten:", min(costs))
    #             print("Minimale aantal intersecties:", min(amount_intersections))
    #         else:
    #             print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
    #             print(f"Geen oplossingen gevonden na {LOOP_AMOUNT} iteraties")

    # while True:
    #     chip = Chip(1,5)
    #     if greedy_ext(chip):
    #         visualise(chip)
    #         break
           
    #     print(len(chip.solution.values()))

    #     results = ResultFunction(chip.solution)

    #     print(results.costs)
    #     print(results.length)
    #     print(results.intersections)

        

    # cost = CostFunction(chip.solution)
    # costs = cost.costs
    # print(costs)
    
    # write = CSVWriter(chip.solution, "greedy_ext", chip_id, netlist_id, costs)

    # while True:
    #     netlist_id = 4
    #     chip_id = 1

    #     chip = Chip(chip_id, netlist_id)
    #     greedy_ext(chip)


    #     visualise(chip)

    #     for wire in chip.solution.values():
    #         inter = selfIntersection(wire)

    #     if inter.self_intected:
    #         visualise(chip)
    #         break



    # chip = Chip(chip_id, netlist_id)
    # # chip.netlistRandomizer()
    # chip.netlistOrder()
    
    while True:
        chip_id = 2
        netlist_id = 9

        chip = Chip(chip_id, netlist_id)
        chip.netlistRandomizer()

        #chip = SolutionToChip("hillclimber_asearch", chip_id,netlist_id, 2699).readResults()

        asearch = ASearch(chip)
        print("waah")
        if asearch.run():
            hillclimber = HillClimber(chip)
            hillclimber.run(12,9,500)

            results = ResultFunction(hillclimber.best_solution)

            print("-------------------------------------")
            print("Beste resultaat Kosten:", results.costs)
            print("Beste resultaat Intersecties:", results.intersections)
            print("Beste resultaat Lengte:", results.length)
            visualise(hillclimber.best_solution)
    
            csvwriter = CSVWriter(hillclimber.best_solution.solution, "hillclimber_asearch", chip_id, netlist_id, results.costs)
            break

    # if asearch.run():
    #     results = ResultFunction(chip)

    #     print(results.costs)
    #     print(results.length)
    #     print(results.intersections)

        # visualise(chip)
    # else:
    #     print("Geen oplossingen gevonden")
    #     visualise(chip)