from code.objects.chip import Chip
from code.objects.wire import Wire
from code.objects.net import Net
from code.visualisation.visualise import visualise
from code.visualisation import tim
from code.algorithms.greedy_ext import greedy_ext
from code.algorithms.greedy_simultaneous import GreedySimultaneous
from code.costfunction import costfunction
from code.algorithms import algorithmTim
import time

import numpy as np

import sys

def main(args):
    if len(args) == 4:

        #chip 1: 18,14
        #chip 2: 18,18

        #haal gate lopen weg

        solutions = []

        n = 100

        runtime = time.time() 

        for i in range(n):
            print("Iteration: " + str(i))     
            chip = Chip(int(args[0]),int(args[1]))
            chip.initializeGates(args[2])
            chip.initializeNetlist(args[2],args[3])
            greedy = GreedySimultaneous(chip, 7)

            while not greedy.run():
                del chip
                chip = Chip(int(args[0]),int(args[1]))
                chip.initializeGates(args[2])
                chip.initializeNetlist(args[2],args[3])
                greedy = GreedySimultaneous(chip, 7)
        
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
                        if point.isIntersected():
                            if not point.isGate():
                                intersection = intersection + 1

            wire_length = 0
            for _,_,wires in netlist:
                wire_length = wire_length + len(wires)-1

            score = (intersection * 300) + wire_length

            solutions.append((score,netlist))


            # tim.visualise(chip, 0)
            # tim.visualise(chip, 1)
            # tim.visualise(chip, 2)
            # tim.visualise(chip, 3)
            # tim.visualise(chip, 4)
            # tim.visualise(chip, 5)
            # tim.visualise(chip, 6)
            # tim.visualise(chip, 7)



            del chip

        chip = Chip(int(args[0]),int(args[1]))
        chip.initializeGates(args[2])
        chip.initializeNetlist(args[2],args[3])

        scores = []

        for i in range(n):
            scores.append(solutions[i][0])

        print(np.mean(scores))
        print(np.var(scores))

        solutions.sort(key=lambda x: int(x[0]))

        # print(f"Solution {0} score {solutions[0][0]}:")
        # for g1,g2,wires in solutions[0][1]:
        #     print("")
        #     print(f"Netlist: gate {g1} to gate {g2}:")
        #     print("")
        #     print(f"Gate {g1} location: ({chip.gates[g1].x},{chip.gates[g1].y},{chip.gates[g1].z})")
        #     print(f"Gate {g2} location: ({chip.gates[g2].x},{chip.gates[g2].y},{chip.gates[g2].z})")
        #     print("")
        #     print(wires)



        for g1,g2,w in solutions[0][1]:
            wire = Wire()   
            for point in w:
                x = point[0]
                y = point[1]
                z = point[2]
                wire.wire_path.append(chip.getGridPoint(x,y,z))
            chip.outputdict[Net(chip.gates[g1], chip.gates[g2])] = wire            

        print("Score: " + str(solutions[0][0]))
        chip.giveResults("greedy_simultaneous",args[2],args[3],solutions[0][0])

        print("tijd: " + str(time.time() - runtime))

        # solutions[0][1][2]

        # for i in range(n):
        #     print(f"Solution {i} score {solutions[i][0]}:")
        #     for g1,g2,wires in solutions[i][1]:
        #         print("")
        #         print(f"Netlist: gate {g1} to gate {g2}:")
        #         print("")
        #         print(f"Gate {g1} location: ({chip.gates[g1].x},{chip.gates[g1].y},{chip.gates[g1].z})")
        #         print(f"Gate {g2} location: ({chip.gates[g2].x},{chip.gates[g2].y},{chip.gates[g2].z})")
        #         print("")
        #         print(wires)

        #     print("")
        #     print("")


    else:
        print("Wrong usage: python main.py [width] [height] [chip] [netlist]")

if __name__ == "__main__":
   main(sys.argv[1:])

