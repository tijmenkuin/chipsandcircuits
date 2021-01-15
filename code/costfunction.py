from .objects.chip import Chip

def costfunction(chip):
    total = 0
    for wire in chip.solution.values():
        total += len(wire.path) - 1

    total += chip.amount_intersections * 300
    return total
