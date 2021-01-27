"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

greedy_simultaneous.py

Chips and Circuits 2021
"""

from ..objects.wire import Wire
from random import choice, random

class GreedySimultaneous:

    def __init__(self, chip, n):
        self.chip = chip
        self.n = n
        self.current_point = None
        self.destination_point = None

        self.targets = dict()
        for net in self.chip.netlist:
            self.targets[(net.target[0], net.target[1])] = ([net.target[0]],[net.target[1]])

    def moveHeuristicScore(self, new_point):
        """
        Gives a Heuristic value to a possible move by taking the possible moves left, intersections and Manhattan Distance into consideration
        """
        intersection_penalty = 300
        exponential_intersection = 4
        exponential_movescore = 2

        intersection =  intersection_penalty if not new_point.isGate() and new_point.amountOfIntersections() > 1 else 0
        distance = new_point.manhattanDistanceTo(self.destination_point)
        movescore = (new_point.getMoveScore() if not new_point.isGate() else 0) + 1

        return (distance + intersection**exponential_intersection) / (movescore**exponential_movescore) 

    def pathFinder(self):
        """
        Generates a list of all possible paths
        """
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
        """
        Creates a path with a length of n that uses the moveHeuristicScore function to determine the impact of one move in the future
        """
        path = [direction]

        for _ in range(self.n):
            moves = self.createMoveList(iterator_point)
            if moves is None:
                return None
            moves.sort(key=lambda x: x[0])

            path.append(moves[0][2])
            iterator_point = moves[0][1] 
            score = score + moves[0][0]

            finished = [move for move in moves if move[1].manhattanDistanceTo(self.destination_point) == 0]
            if len(finished) > 0:
                return (score, path)

        return (score, path)

    def moveChecker(self, point, direction):
        """
        Checks if a move in a certain direction can be made, and returns moveScore, the new point and the same direction
        """
        if direction in point.relatives:

            if point.grid_segments[direction].used:
                return None

            new_point = point.relatives[direction]

            if new_point.isGate() and new_point is not self.destination_point:
                return None

            point.grid_segments[direction].used = True
            score = self.moveHeuristicScore(new_point)
            point.grid_segments[direction].used = False

            return (score, new_point, direction)
        return None
                    
    def createMoveList(self, point):
        """
        Generates a list of all the possible moves, returns none if empty
        """
        moves = [self.moveChecker(point, direction) for direction in point.relatives.keys()]
        moves = list(filter(None, moves))
        if len(moves) == 0:
            return None
        return moves       

    def selectPoints(self, target, rdm):
        """
        Selects a point of a random wire and it's destination point
        """
        if rdm < .5:
            self.current_point = self.targets[target][1][-1]
            self.destination_point = self.targets[target][0][-1]
        else:
            self.current_point = self.targets[target][0][-1]
            self.destination_point = self.targets[target][1][-1]

    def addToWire(self, target, rdm):
        """
        Adds the point to a temporary list to build up the wire
        """
        if rdm < .5:
            self.targets[target][1].append(self.current_point)
        else:
            self.targets[target][0].append(self.current_point)

    def makeResultFunctionCompatible(self):
        """
        Counts intersections and assigns them to the correct points
        """
        for z in range(self.chip.depth):
            for y in range(self.chip.height):
                for x in range(self.chip.width):
                    point = self.chip.getGridPoint(x,y,z)
                    if not point.isGate():
                        intersections = point.amountOfIntersections()
                        point.intersected = intersections + 1

    def run(self):
        """
        Runs the greedy algorithm, slowly builds up the wires and makes greedy selections based on the Heuristic score
        """
        # Select starting point
        target = choice(list(self.targets.keys()))
        rdm = random()

        self.selectPoints(target, rdm)
        self.addToWire(target, rdm)

        while self.current_point:
            path = self.pathFinder()

            if path is None:
                self.chip.solution = dict()
                return False

            self.current_point = self.current_point.moveTo(path[0][1][0])
            self.addToWire(target, rdm)

            # Checks if newly assigned point is the destination point
            if self.current_point.manhattanDistanceTo(self.destination_point) == 0:
                
                wire = Wire()
                wire.path = self.targets[target][0] + self.targets[target][1][::-1][1:]
                net = [net for net in self.chip.netlist if (net.target[0], net.target[1]) == target][0]
                self.chip.solution[net] = wire

                del self.targets[target]

                # No more targets to wire, algorithm has been finished
                if len(self.targets) == 0:
                    self.makeResultFunctionCompatible()

                    return True
            
            # Pick a new point
            target = choice(list(self.targets.keys()))
            rdm = random()

            self.selectPoints(target, rdm)
        return False