# A000241
crossing_numbers = [0,0,0,0,0,1,3,9,18,36,60,100,150]

def lowerBound(chip):
    min_distance = 0

    graphs = {}

    for net in chip.netlist:
        g1 = net.target[0]
        g2 = net.target[1]

        min_distance = min_distance + abs(g1.x-g2.x) + abs(g1.y-g2.y) + abs(g1.z-g2.z) 

        if g1.gate_id in graphs:
            graphs[g1.gate_id] = sorted(graphs[g1.gate_id] + [g2.gate_id])
        else:
            graphs[g1.gate_id] = sorted([g1.gate_id, g2.gate_id])
        
        if g2.gate_id in graphs:
            graphs[g2.gate_id] = sorted(graphs[g2.gate_id] + [g1.gate_id])
        else:
            graphs[g2.gate_id] = sorted([g1.gate_id, g2.gate_id])

    print(graphs)
    print(min_distance)