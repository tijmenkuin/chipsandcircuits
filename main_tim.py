from code.objects.chip import Chip
from code.objects.wire import Wire
from code.objects.net import Net
from code.visualisation.visualise import visualise
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.utils.csv_writer import CSVWriter
from code.utils.solution_reader import SolutionToChip
from code.utils.lower_bound import lowerBound
import time

import numpy as np

import sys

def main(args):

    
    chip = SolutionToChip("asearch-tim", 2,9, 27349).readResults()
    visualise(chip)
    return


    if len(args) == 2:
        solutions = []
        n = 30
        runtime = time.time() 
        # while True:
        for i in range(n):
            i = i + 1
            print("Iteration: " + str(i))     
            chip = Chip(args[0],args[1])
            greedy = GreedySimultaneous(chip, 25)

            while not greedy.run(51620):
                chip.clear()
                greedy = GreedySimultaneous(chip, 25)

        
            netlist = []
            for net in chip.netlist:
                wires = []
                for point in net.wire():
                    wires.append((point.x, point.y, point.z))
                netlist.append((net.target[0].gate_id, net.target[1].gate_id, wires))

            intersection = 0

            for z in range(chip.depth):
                for y in range(chip.height):
                    for x in range(chip.width):
                        point = chip.getGridPoint(x,y,z)
                        if point.isIntersected() > 0:
                            if not point.isGate():
                                intersection = intersection + point.isIntersected()

            wire_length = 0
            for _,_,wires in netlist:
                wire_length = wire_length + len(wires)-1
            score = (intersection * 300) + wire_length
            solutions.append((score,netlist))
            del chip

        chip = Chip(args[0],args[1])

        scores = []
        for i in range(n):
            scores.append(solutions[i][0])
        
        solutions.sort(key=lambda x: int(x[0]))

        for g1,g2,w in solutions[0][1]:
            wire = Wire()
            for point in w:
                x = point[0]
                y = point[1]
                z = point[2]
                wire.path.append(chip.getGridPoint(x,y,z))
            chip.solution[Net(chip.gates[g1], chip.gates[g2])] = wire       

        visualise(chip)     

        print("Gemiddelde: " + str(np.mean(scores)))
        print("Variantie: " + str(np.var(scores)))
        print("Minimum: " + str(min(scores)))
        print("Maximum: " + str(max(scores)))
        print("Tijd: " + str(time.time() - runtime))

        CSVWriter(chip.solution, "greedt_simultaneous", args[0], args[1], solutions[0][0])
        solutions = []

    else:
        print("Wrong usage: python main.py [width] [height] [chip] [netlist]")

if __name__ == "__main__":
   main(sys.argv[1:])

# def main(args):
#     if len(args) == 2:
#         solutions = []
#         n = 30
#         runtime = time.time() 
#         for i in range(n):
#             print("Iteration: " + str(i))     
#             chip = Chip(args[0],args[1])
#             greedy = GreedySimultaneous(chip, 7)

#             while not greedy.run():
#                 del chip
#                 chip = chip = Chip(args[0],args[1])
#                 greedy = GreedySimultaneous(chip, 7)
        
#             netlist = []
#             for net in chip.netlist:
#                 wires = []
#                 for point in net.wire():
#                     wires.append((point.x, point.y, point.z))
#                 netlist.append((net.target[0].gate_id, net.target[1].gate_id, wires))

#             intersection = 0

#             for z in range(chip.depth):
#                 for y in range(chip.height):
#                     for x in range(chip.width):
#                         point = chip.getGridPoint(x,y,z)
#                         if point.isIntersected() > 0:
#                             if not point.isGate():
#                                 intersection = intersection + point.isIntersected()

#             wire_length = 0
#             for _,_,wires in netlist:
#                 wire_length = wire_length + len(wires)-1
#             score = (intersection * 300) + wire_length
#             solutions.append((score,netlist))
#             del chip

#         chip = Chip(args[0],args[1])

#         scores = []
#         for i in range(n):
#             scores.append(solutions[i][0])
        
#         solutions.sort(key=lambda x: int(x[0]))

#         for g1,g2,w in solutions[0][1]:
#             wire = Wire()
#             for point in w:
#                 x = point[0]
#                 y = point[1]
#                 z = point[2]
#                 wire.path.append(chip.getGridPoint(x,y,z))
#             chip.solution[Net(chip.gates[g1], chip.gates[g2])] = wire       

#         visualise(chip)     

#         print("Gemiddelde: " + str(np.mean(scores)))
#         print("Variantie: " + str(np.var(scores)))
#         print("Minimum: " + str(min(scores)))
#         print("Maximum: " + str(max(scores)))
#         print("Tijd: " + str(time.time() - runtime))

#         CSVWriter(chip.solution, "greedt_simultaneous", args[0], args[1], solutions[0][0])

#     else:
#         print("Wrong usage: python main.py [width] [height] [chip] [netlist]")

# if __name__ == "__main__":
#    main(sys.argv[1:])

