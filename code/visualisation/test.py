import plotly.express as px
import plotly.graph_objects as go


def visualise(chip):
    X = []
    Y = []
    Z = []
    Id = []

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

    fig = go.Figure(data=[go.Scatter3d(
        x=X,
        y=Y,
        z=Z,
        marker=dict(
        size=6,
        color=z,
        colorscale='Viridis',
    ),
    line=dict(
        color='darkred',
        width=2
    ),
    marker_symbol='square',
    text= Id
        # mode='lines+markers+text', marker_symbol='square'
    )])

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
    fig.show()
