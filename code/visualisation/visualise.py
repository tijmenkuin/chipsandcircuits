import matplotlib.pyplot as plt
import numpy as np

def visualise(chip, z):
    X = []
    Y = []
    Id = []

    for y in range(chip.height):
        for x in range(chip.width):
            if chip.getGridPoint(x,y,z).gate_id is not None:
                Y.append(y)
                X.append(x)
                Id.append(chip.getGridPoint(x,y,z).gate_id)

        plt.xlim( -1, chip.width + 1)
        plt.ylim(-1, chip.height + 1)

        # np.arange(0, chip.width-1, 1)
        # np.arange(0, chip.height-1, 1)
        # plt.text(X, Y, "chip.getGridPoint(X, Y, 0).gate_id")
        
        plt.scatter(X,Y, marker="s",color='r', lw=9)

        for i, txt in enumerate(Id):
            plt.annotate(txt, (X[i - 1], Y[i - 1]))
        
        plt.grid(True)
        plt.savefig('bar.png')
