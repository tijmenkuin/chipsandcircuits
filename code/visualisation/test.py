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
    # Create a blank figure with labels
    # df = px.data(X, Y, Z)

    for y in range(chip.height):
        for x in range(chip.width):
            for z in range(chip.depth):
                if chip.getGridPoint(x,y,z).gate_id is not None:
                    Y.append(y)
                    X.append(x)
                    Z.append(z)
                    Id.append(chip.getGridPoint(x,y,z).gate_id)
    
    #create the coordinate list for the lines
    # for p in pairs:
    #     for i in range(2):
    #         x_lines.append(X[p[i]])
    #         y_lines.append(Y[p[i]])
    #         z_lines.append(Z[p[i]])
    
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

    # fig = go.Figure(data=[go.Scatter3d(
    #     x=X,
    #     y=Y,
    #     z=Z,
    #     marker=dict(
    #     size=6,
    #     color=z,
    #     colorscale='Viridis',
    # ),
    # line=dict(
    #     color='darkred',
    #     width=2
    # ),
    # marker_symbol='square',
    # text= Id
    #     # mode='lines+markers+text', marker_symbol='square'
    # )])
    
    # fig = go.Figure(data=[go.Scatter3d(x=[3, 4], y=[3, 4], z=[3, 5])])

    # for i, txt in enumerate(Id):

    #     fig.update_layout(
    #     scene=dict(
    #         annotations=[
    #         dict(
    #             showarrow=False,
    #             text=Id[i],
    #             opacity=0.7)]
    #     ))

    
    # fig = go.line_3d(data=[go.Scatter3d(
    #     x=X,
    #     y=Y,
    #     z=Z, x="x", y="pop", z="year")

    # for i, txt in enumerate(Id):
    #         fig.annotate(txt, (X[i], Y[i], Z[i]))
    # tight layout
    # fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))


    # fig = px.scatter_3d(X, Y, Z, x='sepal_length', y='sepal_width', z='petal_width',
    #                     color='petal_length', symbol='species')
    fig = go.Figure(data=[gates, net_list, net_list1])
    fig.show()