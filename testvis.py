from code.objects.chip import Chip
from code.visualisation.test import visualise


size = SizeDeterminator(0)
    
chip = Chip(size.getWidth(), size.getHeight())

chip.initializeGates(0)
chip.initializeNetlist(0,3)

visualise(chip)
