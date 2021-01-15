from code.objects.chip import Chip
from code.visualisation.test import visualise


chip = Chip(10 ,10)
chip.initializeGates(0)
# chip.getGridPoint(1, 5, 0).gate_id = 1
# chip.getGridPoint(2, 5, 0).gate_id = 2
# chip.getGridPoint(3, 5, 0).gate_id = 3
# chip.getGridPoint(4, 5, 0).gate_id = 4
# chip.getGridPoint(5, 5, 0).gate_id = 5
# chip.getGridPoint(6, 5, 0).gate_id = 6
chip.initializeNetlist(0,3)

visualise(chip)
