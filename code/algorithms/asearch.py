from ..objects.chip import Chip
from ..objects.wire import Wire

import random
import numpy as np

def asearchalg(chip):
    total_nets = len(chip.netlist)
    net = chip.netlist[0]
    
    current_point = net.target[0]
    end_point = net.target[1]
    
    wire = Wire(current_point)
    i = -1 

    for net in chip.netlist:
        current_point = net.target[0]
        end_point = net.target[1]
        wire = Wire(current_point)
        i += 1
        
        while not wire.connected:
            if current_point.intersected >= 1:
                chip.addIntersection()
            
            current_point.intersect()
            compare = []
            
            for move, option in current_point.relatives.items():
                if current_point.movePossible(move, end_point):
                    score = heuristic(option, end_point)
                    compare.append([score, move])
                    
            if compare == []:
                print("Vastgelopen: er pasten", i, "nets in, van de ", total_nets, "nets")
                print(chip.outputdict)
                return 0

            move = selectMove(compare)
            current_point.grid_segments[move].used = True
            current_point = current_point.relatives[move] 

            wire.wire_path.append(current_point)

            if current_point == end_point:
                wire.connected = True
        
        
        chip.outputdict[net] = wire
        
        
    chip.giveResults()
    
def heuristic(point, endpoint):
    return abs(point.x - endpoint.x) + abs(point.y - endpoint.y) + abs(point.z - endpoint.z) #+ 300 * point.intersected

def selectMove(comparation):
    scores = [score[0] for score in comparation]
    minval = min(scores)
    indeces = [i for i, v in enumerate(scores) if v == minval]
    pick = random.choice(indeces)
    return comparation[pick][1]

def options():
    """
    Gives list of move options and their heuristic value
    """
    pass