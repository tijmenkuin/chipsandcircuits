from .objects.chip import Chip

def costfunction(chip):
    total = 0
    for wire in chip.outputdict.values():
        total += len(wire.wire_path) - 1

    total += chip.amount_intersections
    return total
