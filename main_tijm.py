from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.costfunction import CostFunction
from code.visualisation.visualise import visualise

if __name__ == "__main__":
    AMOUNT_SOLUTIONS = 1000
    LOOP_AMOUNT = 100

    for i in range(3):
        for j in range(3):
            gem = 0
            for k in range(LOOP_AMOUNT):
                netlist_id = j + 1 + (3 * i)
                chip = Chip(i, netlist_id)
                gem += greedy_ext(chip)
            print("Gevonden resultaat voor chip", i, "en netlist", netlist_id, "is:")
            print(gem / LOOP_AMOUNT * 100)

    # amount_solutions = 0
    # total_costs = 0

    # while AMOUNT_SOLUTIONS != amount_solutions:
    #     chip = Chip(0,2)
    #     if greedy_ext(chip):
    #         cost = CostFunction(chip.solution, chip.amount_intersections)
    #         total_costs += cost.costs
    #         amount_solutions += 1
        
    # print("Gemiddelde kosten is:", total_costs / AMOUNT_SOLUTIONS)