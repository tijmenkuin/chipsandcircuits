from ..objects.wire import Wire

class selfIntersection():
    def __init__(self, wire):
        self.wire = wire
        self.self_intected = False
        self.fixSelfIntersection()
        
    def fixSelfIntersection(self):
        found = False
        for i, point in enumerate(self.wire.path):
            for j, same_point in enumerate(self.wire.path[i + 1:]):
                if point == same_point:
                    found = True
                    self.setSelfIntersected()

                    del self.wire.path[i+1 : i+2+j]
        if found:
            self.fixSelfIntersection()

    def setSelfIntersected(self):
        self.self_intected = True