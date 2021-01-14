from ..objects.chip import Chip
from ..objects.wire import Wire

import random
import numpy as np

def greedy_ext(chip):
    total_nets = len(chip.netlist)
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
            compare = valued_options(current_point, end_point, 1)

            if compare == []:
                return 0

            move = selectMove(compare)
            current_point.grid_segments[move].used = True
            current_point = current_point.relatives[move] 

            wire.wire_path.append(current_point)

            if current_point == end_point:
                wire.connected = True

        chip.outputdict[net] = wire
        
    return 1
    
def heuristic(point, endpoint, look_ahead):
    opts = options(point, endpoint)

    if look_ahead == 1:
        amount_options = len(opts)
        distance_value = manhatten_distance(point, endpoint)
        return distance_value / amount_options
    else:
        score = 0
        for new_state in opts:
            score += heuristic(new_state, endpoint, look_ahead - 1)
        return score
            

def selectMove(comparation):
    """
    Decide move, for given data
    """
    scores = [score[0] for score in comparation]
    minval = min(scores)
    indeces = [i for i, v in enumerate(scores) if v == minval]
    pick = random.choice(indeces)

    return comparation[pick][1]

def valued_options(current_point, end_point, look_ahead):
    """
    Gives list of move options and their heuristic value
    """
    compare = []
    for move, option in current_point.relatives.items():
        if current_point.movePossible(move, end_point):
            score = heuristic(option, end_point, look_ahead)
            compare.append([score, move])

    return compare

def options(current_point, end_point):
    """
    Gives list of accessible neighbour points
    """
    options = []
    for move, option in current_point.relatives.items():
        if current_point.movePossible(move, end_point):
            options.append(current_point.relatives[move])

    return options

def manhatten_distance(point1, point2):
    """
    Calculates Manhattan distance between points
    """
    return abs(point1.x - point2.x) + abs(point1.y - point2.y) + abs(point1.z - point2.z)