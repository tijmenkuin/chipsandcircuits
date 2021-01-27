"""
Tim Alessie, Hanan Almoustafa, Tijmen Kuin

visualise.py

Chips and Circuits 2021
"""

import plotly.express as px
import plotly.graph_objects as go
import plotly

import random


def visualise(chip):
    """
    Uses the plotly library to generate a visualisation
    For more info on plotly check-out: https://plotly.com/python/
    """

    X_gates = []
    Y_gates = []
    Z_gates = []
    Id_gates = []

    net = []

    x_wires = []
    y_wires = []
    z_wires = []

    X_intersection = []
    Y_intersection  = []
    Z_intersection  = []

    # Reads the solution into lists
    for wire in chip.solution.values():
        x_wire = []
        y_wire = []
        z_wire = []
        for point in wire.path:
            x_wire.append(point.x)
            y_wire.append(point.y)
            z_wire.append(point.z)
        x_wires.append(x_wire)
        y_wires.append(y_wire)
        z_wires.append(z_wire)

    for gate_id in chip.gates:
        Y_gates.append(chip.gates[gate_id].y)
        X_gates.append(chip.gates[gate_id].x)
        Z_gates.append(chip.gates[gate_id].z)
        Id_gates.append(gate_id)
    
    for z in range(chip.depth):
        for y in range(chip.height):
            for x in range(chip.width):
                point = chip.getGridPoint(x,y,z)
                if point.amountOfIntersections():
                    X_intersection.append(x)
                    Y_intersection.append(y)
                    Z_intersection.append(z)

    # Create points on 3D grid
    intersections = go.Scatter3d(
            x=X_intersection,
            y=Y_intersection,
            z=Z_intersection,
            marker_symbol='square',
            mode='markers',
            name='intersections',
            marker=dict(size=3, color='blue'))

    gates = go.Scatter3d(
            x=X_gates,
            y=Y_gates,
            z=Z_gates,
            marker_symbol='square',
            mode='markers+text',
            text= Id_gates,
            name='gates',
            marker=dict(size=8, color='red'),
            textposition="middle center")

    # Create netlist on 3D grid
    net_lists = []
    for i,_ in enumerate(x_wires):
        red = random.randint(0, 255)
        blue = random.randint(0, 255)
        green = random.randint(0, 255)

        temp_netlist = list(chip.solution.keys())

        gate_1 = temp_netlist[i].target[0].gate_id
        gate_2 = temp_netlist[i].target[1].gate_id

        net_name = f"net ({gate_1}, {gate_2})"

        net_list = go.Scatter3d(
            x=x_wires[i],
            y=y_wires[i],
            z=z_wires[i],
            mode='lines',
            name=net_name,
            marker=dict(color=f'rgb({red},{green},{blue})')
        )

        net_lists.append(net_list)

    data = [gates] + [intersections] + [net_list for net_list in net_lists]

    fig = go.Figure(data=data)
    
    # Show figure

    fig.update_layout(height=900,width=1400)
    fig.show()