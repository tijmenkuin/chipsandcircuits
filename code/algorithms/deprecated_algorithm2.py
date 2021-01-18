from ..objects.chip import Chip
import math

def StartersAlgoritme(chip):
    netlist = chip.netlist
    netid = 0
    currentPoint = chip.gates[netlist[0].target[0].gate_id]
    previousMove = None
    toGate = chip.gates[netlist[0].target[0].gate_id]

    while currentPoint:
        x = currentPoint.x
        y = currentPoint.y
        z = currentPoint.z
        moves = []

        left = chip.getGridPoint(x - 1, y, z)
        right = chip.getGridPoint(x + 1, y, z)
        forwards = chip.getGridPoint(x, y - 1, z)
        backwards = chip.getGridPoint(x, y + 1, z)
        
        checkPoint(moves, toGate, 'left', currentPoint,left)
        checkPoint(moves, toGate, 'right', currentPoint, right)
        checkPoint(moves, toGate, 'forwards', currentPoint, forwards)
        checkPoint(moves, toGate, 'backwards', currentPoint, backwards)
        
        moves.sort()
        print(moves)
        if len(moves) > 0:
            if (moves[0][0] == 0):
                if z != 0:
                    while currentPoint.checkMoveUsed('down') == False:
                        currentPoint = currentPoint.moveTo('down')
                        print(currentPoint.z)
                        print('down')
                if currentPoint.z != 0:
                    print("No solution found!")
                    break
                previousMove = None
                currentPoint.moveTo(moves[0][1])
                if len(netlist) > netid + 1:
                    netid = netid + 1
                    currentPoint = chip.gates[netlist[netid].target[0].gate_id]
                    toGate = chip.gates[netlist[netid].target[1].gate_id]
                    continue
        if len(moves) > 1:
            if (moves[0][0] == moves[1][0]):
                if moves[1][1] == previousMove:
                    previousMove = moves[1][1]
                    currentPoint = currentPoint.moveTo(moves[1][1])
                else:
                    previousMove = moves[0][1]
                    currentPoint = currentPoint.moveTo(moves[0][1])
            else:
                previousMove = moves[0][1]
                currentPoint = currentPoint.moveTo(moves[0][1])              
        elif len(moves) > 0:
            previousMove = moves[0][1]
            currentPoint = currentPoint.moveTo(moves[0][1])
        else:
            if currentPoint.checkMoveUsed('down') == False:
                currentPoint = currentPoint.moveTo('down')
                print('down')
            elif currentPoint.checkMoveUsed('up') == False:
                currentPoint = currentPoint.moveTo('up')
                print('up')  
            else:
                print("No solution found!")
                break




def checkPoint(moves, gate, direction, currentPoint, point):
    if currentPoint.checkMoveUsed(direction) == False:
        x_1 = point.x
        y_1 = point.y
        distance = abs(x_1-gate.x) + abs(y_1-gate.y)
        moves.append((distance, direction))

