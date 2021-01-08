from code.objects.chip import Chip

if __name__ == "__main__":
    chip = Chip(10,10)
    chip.initializeNetlist(0,1)
    chip.makeDict()
    chip.giveResults()


