from code.objects.chip import Chip
from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.asearch_tim import ASearch
from code.utils.checker import Checker
from code.utils.size_determinator import SizeDeterminator
from code.utils.csv_writer import CSVWriter
from code.utils.resultfunction import ResultFunction
from code.visualisation.visualise import visualise
from code.optimizations.self_intersector import selfIntersection

import numpy as np


from datetime import datetime


if __name__ == "__main__":
    AMOUNT_SOLUTIONS = 10


    LOOP_AMOUNT = 20000


    start=datetime.now()

    for i in range(3):
        for j in range(3):
            if i == 0:
                continue 
            netlist_id = j + 1 + (3 * i)
            amount_solutions = 0
            costs = []
            amount_intersections = []
            count = 0
            breaked = False

            while AMOUNT_SOLUTIONS != amount_solutions:
                count += 1
                chip = Chip(i, netlist_id)
                chip.netlistRandomizer()
                asearch = ASearch(chip)
                if asearch.run():
                    result = ResultFunction(chip)
                    if count == 1 or result.costs < min(costs):
                        writer = CSVWriter(chip.solution, "asearch-tim", i, netlist_id, result.costs)
                        costs.append(result.costs)
                    amount_intersections.append(result.intersections)
                    amount_solutions += 1
                if count == LOOP_AMOUNT:
                    breaked = True
                    break

            
            if not breaked:
                print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
                print("Gemiddelde kosten:", np.mean(costs))
                print("Gemiddeld aantal intersecties:", np.mean(amount_intersections))
                print("Minimale kosten:", min(costs))
                print("Minimale aantal intersecties:", min(amount_intersections))
            elif amount_solutions != 0:
                print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, f"over {amount_solutions} oplossingen:")
                print("Gemiddelde kosten:", np.mean(costs))
                print("Gemiddeld aantal intersecties:", np.mean(amount_intersections))
                print("Minimale kosten:", min(costs))
                print("Minimale aantal intersecties:", min(amount_intersections))
            else:
                print("Gevonden resultaten voor chip", i, "en netlist", netlist_id, "is:")
                print(f"Geen oplossingen gevonden na {LOOP_AMOUNT} iteraties")


            now = datetime.now()
            print(now-start)