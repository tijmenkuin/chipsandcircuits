class Wire():
    def __init__(self):
        self.path = [] #[move]
        self.connected = False

    def __repr__(self):
        return f"{self.path}"

