
# class A_Ster(self):
#     """
#     Intialise open and closed lists
#     Make the start Node current
#     Calculate heuristic distance of start Node to destination (h)
#     Calculate f value for start Node (f = g + h, where g = 0)
#     While current Node is not the destention
#         For each Node adjacent to current 
#             If Node not in closed list and not in open list then
#                 Add Node to open list
#                 Calculate distance from start (g)
#                 Calculate heuristic distance to destination (h)
#                 Calculae f value (f = g + h)
#                 If new f value < existing f value or there is no existin gf value then
#                     Update f value
#                     set parent to be the current Node
#                 End if
#             End if
#         Next adjacent Node
#         Add current Node to cllosed list
#         remove Node with lowest f value from open list and make it current
#     End while
#     """
    
#     def __init__(self):
#         self.open_list = open_list
#         self.closed_list = closed_list
#         open_list = []
#         self.g_value = g_value
#         self.f_value = f_value


#     def manhattenDistance(gridpoint1, gridpoint2):     # heuristic
#         self.gridpoint1 = gridpoint1
# 	    self.gridpoint2 = gridpoint2
# 	return abs(gridpoint1.x - gridpoint2.x) + abs(gridpoint2.y - gridpoint2.y)

#     def algorithm(self, start, end):
#         self.start = start
#         self.end = end
#         self.current_node = current_node
#         self.current_index = current_index
#         self.parent = parent
#         parent = {}
#         open_list.append(start)

#         g_value = {}
#         g_value[start] = 0
#         f_value = {}
#         f_value[start] = manhattenDistance(start, end)

#         # Loop until you find the end
#         while len(open_list) > 0:

#             # Get the current node
#             current_node = open_list[0]
#             current_index = 0
#             for index, item in enumerate(open_list):
#                 if item.f_value < current_node.f_value:
#                     current_node = item
#                     current_index = index

#             # Pop current off open list, add to closed list
#             open_list.pop(current_index)
#             closed_list.append(current_node)

#             # Found the goal
#             if current_node == end:
#                 path = []
#                 current = current_node
#                 while current is not None:
#                     path.append(current.g_value)
#                     current = current.parent
#                 return path[::-1] # Return reversed path

#             # # Generate children
#             # children = []
#             # self.pathFinder.found_paths = relatives
#             # for new_position in relatives: # Adjacent squares

#             #     # Get node position
#             #     node_position = (current_node.g_value[0] + new_position[0], current_node.g_value[1] + new_position[1])

#             # # Loop through children
#             # for child in children:

#             #     # Child is on the closed list
#             #     for closed_child in closed_list:
#             #         if child == closed_child:
#             #             continue

#             #     # Create the f, g, and h values
#             #     child.g = current_node.g + 1
#             #     child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
#             #     child.f = child.g + child.h

#             #     # Child is already in the open list
#             #     for open_node in open_list:
#             #         if child == open_node and child.g > open_node.g:
#             #             continue

#             #     # Add the child to the open list
#             #     open_list.append(child)

# # .................


#     def run(self):
#         start = None 
#         end = None

#         self.run = run
#         run = True

#         while run:
#             algorithm(start, end)
# --------------------------------------------
from ..objects.chip import Wire
import random

class ASearch():
    def __init__(self, chip):
        self.chip = chip
        self.queue = dict()
        self.came_from = dict()

    def run(self):
        """
        Loops over netlist, and finds paths. After found resets the necessary in chip.
        Returns True is solution is found, else false
        """
        for net in self.chip.netlist:
            if net not in self.chip.solution:
                new_wire = self.findPath(net)
                if new_wire == []:
                    return False
                
                wire = Wire()
                for point in new_wire:
                    wire.addPoint(point)
                
                self.chip.solution[net] = wire
                self.markPath(wire)

                self.queue = dict()
                self.came_from = dict()
        return True

    def findPath(self, net):
        """
        Returns cheapest path that connects net
        """
        start_point = net.target[0]
        end_point = net.target[1]

        self.chip.giveHeuristicValues3(end_point, start_point)
        self.chip.giveDefaultGScores()

        self.queue[start_point] = start_point.heuristic_value

        start_point.gscore = 0
        start_point.fscore = start_point.heuristic_value

        while self.queue != {}:
            current = min(self.queue, key=self.queue.get)
            
            if current == end_point:
                return self.reconstructPath(current)
            
            del self.queue[current]

            for relative in current.reachableRelatives(end_point):
                tentative_gScore = current.gscore + 1 + 300 * relative.isIntersected2()

                
                if tentative_gScore < relative.gscore:
                    self.came_from[relative] = current
                    relative.gscore = tentative_gScore
                    relative.fscore = relative.gscore + relative.heuristic_value
                    
                    if relative not in self.queue.keys():
                        self.queue[relative] = relative.fscore
        return []

    def reconstructPath(self, point):
        """
        Builds the path given the parents parents of final point
        """
        total_path = [point]

        while point in self.came_from.keys():
            point = self.came_from[point]
            total_path.insert(0, point)

        return total_path

    def markPath(self, wire):
        """
        Marks the used gridsegments and pass gridpoints for a wire
        """
        for point, neighbour in zip(wire.path, wire.path[1:]):
            for move, relative in point.relatives.items():
                if neighbour == relative:
                    point.grid_segments[move].used = True
                    break

        for point in wire.path:
            if not point.isGate():
                point.intersect()