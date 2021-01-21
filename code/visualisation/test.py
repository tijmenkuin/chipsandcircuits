import plotly.express as px
import plotly.graph_objects as go
import plotly

def visualise(chip):
    X = []
    Y = []
    Z = []
    Id = []

    #the start and end point for each line
    # pairs = [(1,5),(2,5),(3,5),(4,5),(5,5),(6,5)]

    x_lines = [1, 2, 3, 4, 5, 6]
    y_lines = [5, 5, 5, 5, 5, 5]
    z_lines = [0, 0, 0, 0, 0, 0]

    x_lines1 = [1, 1, 2]
    y_lines1 = [5, 5, 5]
    z_lines1 = [2, 3, 3]

    for y in range(chip.height):
        for x in range(chip.width):
            for z in range(chip.depth):
                if chip.getGridPoint(x,y,z).gate_id is not None:
                    Y.append(y)
                    X.append(x)
                    Z.append(z)
                    Id.append(chip.getGridPoint(x,y,z).gate_id)
    
    gates = go.Scatter3d(
                        x=X,
                        y=Y,
                        z=Z,
                        # x='Chip Width', y='Chip Height', z='Chip Depth',
                        surfacecolor='orange', marker_symbol='square',
                        mode='markers',
                        text= Id,
                        name='gates')

        # x_lines.append(None)
        # y_lines.append(None)
        # z_lines.append(None)

    net_list = go.Scatter3d(
        x=x_lines,
        y=y_lines,
        z=z_lines,
        mode='lines',
        name='net_list',surfacecolor='orange'
    )
    
    net_list1 = go.Scatter3d(
        x=x_lines1,
        y=y_lines1,
        z=z_lines1,
        mode='lines',
        name='net_list1',surfacecolor='lightblue'
    )
    fig = go.Figure(data=[gates, net_list, net_list1])
    fig.show()