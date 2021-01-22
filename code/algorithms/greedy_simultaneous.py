import copy
from random import random, randint


class GreedySimultaneous:
    def __init__(self, chip, n):
        self.chip = chip
        self.n = n
        self.current_point = None
        self.destination_point = None

    def manhattanDistance(self, point1, point2):
        return abs(point1.x-point2.x) + abs(point1.y-point2.y) + abs(point1.z-point2.z)  

    def moveScore(self, new_point):

        intersection =  300 * new_point.isIntersected() if new_point.isIntersected() > 0 and (not new_point.isGate()) else 0
        movescore = 1 + new_point.getMoveScore()
        distance = self.manhattanDistance(new_point, self.destination_point)

        return (distance + intersection**4) / (movescore**2) 

    def pathFinder(self):
        found_paths = []
        points = self.createMoveList(self.current_point)

        if points is None:
            return None

        for point in points:
            found_paths.append(self.depthPath(point[0], point[1], point[2]))

        found_paths = list(filter(None, found_paths))

        if len(found_paths) == 0:
            return None

        found_paths.sort(key=lambda x: x[0])

        return found_paths


    def depthPath(self, score, iterator_point, direction):
        path = [direction]

        for _ in range(self.n):
            moves = self.createMoveList(iterator_point)

            finished = [move for move in moves if self.manhattanDistance(move[1], self.destination_point) == 0]
            moves.sort(key=lambda x: x[0])

            path.append(moves[0][2])
            iterator_point = moves[0][1] 
            score = score + moves[0][0]
            moves.clear()

            if len(finished) > 0:
                return (score, path)

        return (score, path)


    def moveChecker(self, point, direction):
        if direction in point.grid_segments:
            if point.grid_segments[direction].used == False:
                if direction in point.relatives:
                    new_point = point.relatives[direction]
                    if new_point.isGate():
                        if new_point not in self.netlist[self.netid].copy:
                            return None
                    point.grid_segments[direction].used = True
                    score = self.moveScore(new_point)
                    point.grid_segments[direction].used = False
                    return (score, new_point, direction)
        return None
                    
    def createMoveList(self, point):
        moves = []
        moves.append(self.moveChecker(point, 'left'))
        moves.append(self.moveChecker(point, 'right'))
        moves.append(self.moveChecker(point, 'forwards'))
        moves.append(self.moveChecker(point, 'backwards'))
        moves.append(self.moveChecker(point, 'up'))
        moves.append(self.moveChecker(point, 'down'))
        moves = list(filter(None, moves))
        if len(moves) == 0:
            return None
        return moves

    def setNewPoints(self):
        currentid = 0
        destinationid = 1

        if random() < .5:
            currentid = 1
            destinationid = 0

        self.current_point = self.netlist [self.netid].copy[currentid]
        self.destination_point = self.netlist [self.netid].copy[destinationid]

        if currentid == 1:
            self.netlist [self.netid].wire_1.append(self.current_point)
        else:
            self.netlist [self.netid].wire_0.append(self.current_point)
            

    def run(self, score = None):
        copynetlist = []
        for net in self.chip.netlist:
            copynetlist.append(net)

        self.netlist = self.chip.netlist
        self.netid = randint(0,len(self.netlist )-1)

        currentid = 0
        destinationid = 1

        if random() < .5:
            currentid = 1
            destinationid = 0

        self.current_point = self.netlist [self.netid].copy[currentid]
        self.destination_point = self.netlist [self.netid].copy[destinationid]

        if currentid == 1:
            self.netlist [self.netid].wire_1.append(self.current_point)
        else:
            self.netlist [self.netid].wire_0.append(self.current_point)

        while self.current_point:

            path = self.pathFinder()

            if path is None:
                print("No solution found!")
                self.chip.netlist = copynetlist
                return False

            self.current_point = self.current_point.moveTo(path[0][1][0])

            # if self.current_point.isIntersected():
            #     self.chip.cost = self.chip.cost + 300
            # self.chip.cost = self.chip.cost + 1

            # if score is not None:
            #     if score < self.chip.cost:
            #         print(f"Too expensive! Cost: {self.chip.cost}")
            #         self.chip.netlist = copynetlist
            #         return False

            if currentid == 1:
                self.netlist [self.netid].wire_1.append(self.current_point)
            else:
                self.netlist [self.netid].wire_0.append(self.current_point)

            self.netlist [self.netid].copy[currentid] = self.current_point
 
            if (self.manhattanDistance(self.current_point, self.destination_point) == 0):
                if len(self.netlist ) > 0:
                    self.netlist.pop(self.netid)
                if len(self.netlist ) < 1:
                    print(f"Solution found! Cost: {self.chip.cost}")
                    self.chip.netlist = copynetlist
                    return score
            
            self.netid = randint(0,len(self.netlist )-1)
            currentid = 0
            destinationid = 1

            if random() < .5:
                currentid = 1
                destinationid = 0

            self.current_point = self.netlist[self.netid].copy[currentid]
            self.destination_point = self.netlist[self.netid].copy[destinationid]