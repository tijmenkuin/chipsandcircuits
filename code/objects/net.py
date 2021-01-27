class Net():
    def __init__(self, gate1, gate2):
        self.target = [gate1,gate2]
        
        #greedy simul
        self.copy = [gate1,gate2]
        self.wire_0 = []
        self.wire_1 = []

    def wire(self):
        #greedy simul
        self.wire_1.reverse()
        return [self.target[0]] + self.wire_0 + self.wire_1[1:] + [self.target[1]]

    def __repr__(self):
        return str([self.target[0].gate_id,self.target[1].gate_id])
