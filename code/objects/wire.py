class Wire():
    def __init__(self):
        self.wire_path = [] #[move]
        self.connected = False

    def __repr__(self):
        return f"{self.wire_path}"

