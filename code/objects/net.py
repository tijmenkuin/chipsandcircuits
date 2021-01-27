class Net():
    def __init__(self, gate1, gate2):
        self.target = [gate1,gate2]

    def __repr__(self):
        return str([self.target[0].gate_id,self.target[1].gate_id])
