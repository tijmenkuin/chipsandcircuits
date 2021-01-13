import matplotlib.pyplot as plt
import numpy as np

def visualise(chip, z):
    X = []
    Y = []
    Id = []

    # Create a blank figure with labels
    # p = figure(plot_width = chip.width, plot_height = chip.height,
    # title = '3D visualisation',
    # x_axis_label = 'X', y_axis_label = 'Y')
    fig = plt.figure()
    ax = plt.axes(projection="3d")

    for y in range(chip.height):
        for x in range(chip.width):
            if chip.getGridPoint(x,y,z).gate_id is not None:
                Y.append(y)
                X.append(x)
                Id.append(chip.getGridPoint(x,y,z).gate_id)

    # plt.xlim( -1, chip.width + 1, 1)
    # plt.ylim(-1, chip.height + 1, 1)
        # p.square(X, Y, size = 12, color = 'red', alpha = 0.6)

    np.arange(0, chip.width-1, 1)
    np.arange(0, chip.height-1, 1)
        # plt.text(X, Y, "chip.getGridPoint(X, Y, 0).gate_id")
        
    
    ax.scatter3D(X, Y, Z, c=Z, cmap='hsv')
    # plt.scatter(X,Y, )

    for i, txt in enumerate(Id):
        plt.annotate(txt, (X[i], Y[i]))
    
    # plt.grid(True)
    # plt.savefig('baz.png')

    # Show the plot
    plt.show()