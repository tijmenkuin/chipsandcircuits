class Wire():
    def __init__(self, start):
        self.wire_path = [start] #[move]
        self.connected = False

    def __repr__(self):
        return f"{self.wire_path}"

