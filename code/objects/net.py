class Net():
    def __init__(self, gate_id1, gate_id2):
        self.target = [gate_id1,gate_id2]

    def __repr__(self):
        return str(self.target)