from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.costfunction import CostFunction
from code.visualisation.visualise import visualise

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
    #                 cost = CostFunction(chip.solution, chip.amount_intersections)
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

    chip = Chip(0, 1)
    greedy_ext(chip)
    cost = CostFunction(chip.solution, chip.amount_intersections)
    costs = cost.costs
    
    write = CSVWriter(chip.solution, "greedy_ext", 0, 1, costs)