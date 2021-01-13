from ..objects.chip import Chip
import math

import random

import time


def distance(point1, point2):
    return abs(point1.x-point2.x) + abs(point1.y-point2.y) + abs(point1.z-point2.z)

def StartersAlgoritme(chip):

    timeout = time.time() + 60*0.5   # 5 minutes from now

    tempList = []

    netlist = chip.netlist

    for net in netlist:
        point1 = net.target[0]
        point2 = net.target[1]
        d = abs(point1.x-point2.x) + abs(point1.y-point2.y) + abs(point1.z-point2.z)
        tempList.append((d, net))

    tempList.sort(key=lambda x: x[0], reverse=False)

    netlist = [net for d,net in tempList]

    print(netlist)

    netid = 0
    currentPoint = chip.gates[netlist[0].target[0].gate_id]
    previousMove = None
    gate = chip.gates[netlist[0].target[1].gate_id]

    print(currentPoint)

    #wire = [currentPoint]

    n = 7

    while currentPoint:
        if (time.time() > timeout):
            print("Time limit reached!")
            break

        
        path = pathFinder(currentPoint, n, gate, chip)
        
        if path is None:
            oldPoint = currentPoint
            #print(currentPoint)
            randommove = randomMove(currentPoint, gate)
            if randommove is None:
                i = 0
                while oldPoint == currentPoint or i > 15:
                    if (time.time() > timeout):
                        break
                    i = i+1
                    currentPoint = backTrack(currentPoint, n, gate)
                continue
            else:
                currentPoint = currentPoint.moveTo(randommove)
                #wire.append(currentPoint)       

        currentPoint = currentPoint.moveTo(path[0][1][0])
        #wire.append(currentPoint)
        # print(currentPoint)
        distance = abs(gate.x-currentPoint.x) + abs(gate.y-currentPoint.y) + abs(gate.z-currentPoint.z)
        if (distance == 0):
            if len(netlist) > netid + 1:
                #chip.netlist[netid].wire = wire
                netid = netid + 1
                currentPoint = chip.gates[netlist[netid].target[0].gate_id]
                gate = chip.gates[netlist[netid].target[1].gate_id]
                print(str([currentPoint.gate_id, currentPoint, gate.gate_id, gate]))
                print(currentPoint)
                clearHistory(chip)
                print(netid)
            else:
                break


def pathFinder(currentPoint, n, gate, chip):

    found_paths = []

    points = []

    points.append(moveChecker(currentPoint, 'left', gate))
    points.append(moveChecker(currentPoint, 'right', gate))
    points.append(moveChecker(currentPoint, 'forwards', gate))
    points.append(moveChecker(currentPoint, 'backwards', gate))
    points.append(moveChecker(currentPoint, 'up', gate))
    points.append(moveChecker(currentPoint, 'down', gate))

    points = list(filter(None, points))
    if len(points) == 0:
        return None

    for point in points:
        found_paths.append(depthPath(point[1], n, gate, point[2], point[0], chip)) 

    found_paths = list(filter(None, found_paths))

    if len(found_paths) == 0:
        return None

    found_paths.sort(key=lambda x: x[0])

    return found_paths


def depthPath(currentPoint, n, gate, direction, points, chip):
    path = [direction]
    iteratorPoint = currentPoint
    points = points

    for _ in range(n):
        moves = []
        moves.append(moveChecker(iteratorPoint, 'left', gate))
        moves.append(moveChecker(iteratorPoint, 'right', gate))
        moves.append(moveChecker(iteratorPoint, 'forwards', gate))
        moves.append(moveChecker(iteratorPoint, 'backwards', gate))
        moves.append(moveChecker(iteratorPoint, 'up', gate))
        moves.append(moveChecker(iteratorPoint, 'down', gate))
        moves = list(filter(None, moves))
        if len(moves) == 0:
            return None
        finished = [move for move in moves if distance(move[1], gate) == 0]
        moves.sort(key=lambda x: x[0])
        path.append(moves[0][2])
        iteratorPoint = moves[0][1] #chip.getGridPoint(moves[0][1].x, moves[0][1].y, moves[0][1].z) #moves[0][1] #cpu.getGridPoint(moves[0][1].x, moves[0][1].y, moves[0][1].z)
        points = points + moves[0][0]
        moves.clear()
        if len(finished) > 0:
            return (points, path)

    return (points, path)

def moveChecker(currentPoint, direction, gate):
    if direction in currentPoint.grid_segments:
        if currentPoint.grid_segments[direction].used == False:
            if direction in currentPoint.relatives:
                newPoint = currentPoint.relatives[direction]
                currentPoint.grid_segments[direction].used = True
                intersection =  300 if newPoint.isIntersected() else 0
                movescore = 1 + newPoint.getMoveScore()
                currentPoint.grid_segments[direction].used = False
                distance = abs(gate.x-newPoint.x) + abs(gate.y-newPoint.y) + abs(gate.z-newPoint.z)
                #bewegingsmogelijkheid

               

                total = (intersection + distance) / (movescore*movescore)
                return (total, newPoint, direction)
    return None




def randomMove(currentPoint, gate):
    points = []
    
    if moveChecker(currentPoint, 'up', gate) is None:
        points.append(moveChecker(currentPoint, 'left', gate))
        points.append(moveChecker(currentPoint, 'right', gate))
        points.append(moveChecker(currentPoint, 'forwards', gate))
        points.append(moveChecker(currentPoint, 'backwards', gate))
        points.append(moveChecker(currentPoint, 'up', gate))
        points.append(moveChecker(currentPoint, 'down', gate))

        points = list(filter(None, points))
        if len(points) == 0:
            return None

        return random.choice(points)[2]
    else:
        return 'up'

def backTrack(point, n, gate):
    for _ in range(random.randrange(1,n)):
        backtrack = point.undoMove()    
        if backtrack:
            point = backtrack
    
    for _ in range(random.randrange(1,int(n/2))):
        randommove = randomMove(point, gate)
        if randommove is not None:
            point = point.moveTo(randommove)

    return point
    

def clearHistory(chip):
    for z in range(chip.depth):
        for y in range(chip.height):
            for x in range(chip.width):
                chip.getGridPoint(x,y,z).last_move = []