import csv

class CSVWriter():
    """
    Writes a csv-file for a given solution, takes 4 extra arguments for orderly inventory

    NOTE : Before usage make sure the directories in writeResults-method exist !!
    """
    def __init__(self, solution, algorithm, chip, netlist, score):
        self.solution = solution
        self.score = score

        self.algorithm = algorithm
        self.score = score
        self.chip = chip
        self.netlist = netlist

        self.writeResults()

    def writeResults(self):
        with open(f"solutions/{self.algorithm}/chip_{self.chip}/netlist_{self.netlist}/{self.score}.csv", "w", newline="") as outfile:
            thewriter = csv.writer(outfile)
            thewriter.writerow(['net','wires'])

            for net, wire in self.solution.items():
                thewriter.writerow([f"({net.target[0].gate_id},{net.target[1].gate_id})", wire])

            thewriter.writerow([f"chip_{self.chip}_net_{self.netlist}", self.score])
            return thewriter