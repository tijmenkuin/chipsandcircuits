from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.asearch_tijm import ASearch
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.resultfunction import ResultFunction
from code.visualisation.visualise import visualise
from code.optimizations.self_intersector import selfIntersection

import numpy as np

if __name__ == "__main__":
    AMOUNT_SOLUTIONS = 100

    LOOP_AMOUNT = 2000

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
    #         netlist_id = j + 1 + (3 * i)
    #         amount_solutions = 0
    #         scores = []
    #         count = 0
    #         breaked = False

    #         while AMOUNT_SOLUTIONS != amount_solutions:
    #             count += 1
    #             chip = Chip(i, netlist_id)
    #             if greedy_ext(chip):
    #                 cost = CostFunction(chip.solution)
    #                 scores.append(cost.costs)
    #                 amount_solutions += 1
    #             if count == LOOP_AMOUNT:
    #                 breaked = True
    #                 break

            
    #         if not breaked:
    #             print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
    #             print("Gemiddelde kosten:", np.mean(scores))
    #             print("Variantie in kosten:", np.var(scores))
    #             print("Maximale kosten:", max(scores))
    #             print("Minimale kosten:", min(scores))
    #         elif amount_solutions != 0:
    #             print(f"Gevonden resultaten voor chip {i} en netlist {netlist_id} is over {amount_solutions} oplossingen:")
    #             print("Gemiddelde kosten:", np.mean(scores))
    #             print("Variantie in kosten:", np.var(scores))
    #             print("Maximale kosten:", max(scores))
    #             print("Minimale kosten:", min(scores))
    #         else:
    #             print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
    #             print(f"Geen oplossingen gevonden na {LOOP_AMOUNT} iteraties")

    
    # chip = Chip(0,3)
    # if greedy_ext(chip):
    #     print(len(chip.solution.values()))

    #     results = ResultFunction(chip.solution)

    #     print(results.costs)
    #     print(results.length)
    #     print(results.intersections)

    #     visualise(chip)

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

    netlist_id = 9
    chip_id = 2

    chip = Chip(chip_id, netlist_id)

    asearch = ASearch(chip)

    if asearch.run():
        results = ResultFunction(chip)

        print(results.costs)
        print(results.length)
        print(results.intersections)

        visualise(chip)
    else:
        print("Geen oplossingen gevonden")
        visualise(chip)