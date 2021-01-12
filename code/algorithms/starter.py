from ..objects.chip import Chip
from ..objects.wire import Wire

import random
import numpy as np

def starter(chip):
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
            compare = valued_options(current_point, end_point)

            if compare == []:
                # print("Vastgelopen: er pasten", i, "nets in, van de ", total_nets, "nets")
                # print(chip.outputdict)
                return i / total_nets

            move = selectMove(compare)
            current_point.grid_segments[move].used = True
            current_point = current_point.relatives[move] 

            wire.wire_path.append(current_point)

            if current_point == end_point:
                wire.connected = True

        chip.outputdict[net] = wire
        
    return 1
    
def heuristic(point, endpoint):
    amount_options = len(options(point, endpoint))
    heuristic_value = manhatten_distance(point, endpoint)

    return heuristic_value / (amount_options * 100)

def selectMove(comparation):
    """
    Decide move, for given data
    """
    scores = [score[0] for score in comparation]
    minval = min(scores)
    indeces = [i for i, v in enumerate(scores) if v == minval]
    pick = random.choice(indeces)

    return comparation[pick][1]

def valued_options(current_point, end_point):
    """
    Gives list of move options and their heuristic value
    """
    compare = []
    for move, option in current_point.relatives.items():
        if current_point.movePossible(move, end_point):
            score = heuristic(option, end_point)
            compare.append([score, move])

    return compare

def options(current_point, end_point):
    """
    Gives list of move options
    """
    options = []
    for move, option in current_point.relatives.items():
        if current_point.movePossible(move, end_point):
            options.append(move)

    return options

def manhatten_distance(point1, point2):
    return abs(point1.x - point2.x) + abs(point1.y - point2.y) + abs(point1.z - point2.z)