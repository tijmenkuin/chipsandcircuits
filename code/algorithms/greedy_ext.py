from ..objects.chip import Chip
from ..objects.wire import Wire

import random
import numpy as np
from operator import itemgetter
import copy

def greedy_ext(chip):
    total_nets = len(chip.netlist)
    i = -1 

    # netlistSortDistance(chip)

    for net in chip.netlist:
        current_point = net.target[0]
        end_point = net.target[1]

        wire = Wire()
        wire.addPoint(current_point)

        i += 1

        while not wire.connected:
            if current_point.intersected >= 1 and not current_point.isGate():
                chip.addIntersection()
            
            current_point.intersect()
            compare = valueOptions(current_point, end_point, 1)

            if compare == []:
                return False

            move = selectMove(compare)
            current_point.grid_segments[move].used = True
            current_point = current_point.relatives[move] 

            wire.addPoint(current_point)

            if current_point == end_point:
                wire.connected = True

        chip.solution[net] = wire
        
    return True
    
def heuristic(point, endpoint, look_ahead):
    opts = options(point, endpoint)

    if look_ahead == 1:
        amount_options = len(opts)
        # if amount_options == 0:
        #     return 100000

        distance_value = manhattenDistance(point, endpoint)
        if point.intersected == 0:
            intersection = 0
        else:
            intersection = 1

        return distance_value / (amount_options + 1)
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

def valueOptions(current_point, end_point, look_ahead):
    """
    Gives list of move options and their heuristic value
    """
    compare = []
    for move, relative in current_point.relatives.items():
        if current_point.movePossible(move, end_point):
            score = heuristic(relative, end_point, look_ahead)
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

def manhattenDistance(point1, point2):
    """
    Calculates Manhattan distance between points
    """
    return abs(point1.x - point2.x) + abs(point1.y - point2.y) + abs(point1.z - point2.z)

def netlistSortDistance(chip):
    """
    Sorts netlist in manhatten-distance, small to big
    """
    distances = list()
    just_distances = set()

    for i, net in enumerate(chip.netlist):
        dist = manhattenDistance(net.target[0], net.target[1])
        distances.append((i, dist))
        just_distances.add(dist)

    distances.sort(key=itemgetter(1))

    k = -1
    bible = dict()

    for dista in just_distances:
        k += 1
        newlist = []
        for twiple in distances:
            if twiple[1] == dista:
                newlist.append(twiple)
        
        bible[k] = newlist
    
    for key, value in bible.items():
        random.shuffle(value)
        bible[key] = value

    new_distances = []
    for sub_list in bible.values():
        new_distances.extend(sub_list)
    
    new_netlist = []
    for order in new_distances:
        new_netlist.append(chip.netlist[order[0]])

    chip.netlist = new_netlist