def lowerBound(chip):
    min_distance = 0
    for net in chip.netlist:
        g1 = net.target[0]
        g2 = net.target[1]
        min_distance = min_distance + abs(g1.x-g2.x) + abs(g1.y-g2.y) + abs(g1.z-g2.z) 
    return min_distance