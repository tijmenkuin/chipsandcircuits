from ..objects.wire import Wire

class selfIntersection():
    def __init__(self, wire):
        self.wire = wire
        self.fixes = dict()
        self.amount_fixes = 0

        self.fixSelfIntersection()

    def fixSelfIntersection(self):
        found = False
        fix = []

        for i, point in enumerate(self.wire.path):
            for j, same_point in enumerate(self.wire.path[i + 1:]):
                if point == same_point:
                    found = True
                    self.amount_fixes += 1
                    
                    for point in self.wire.path[i+1 : i+2+j]:
                        fix.append(point)
                    
                    self.fixes[self.amount_fixes] = fix
                    del self.wire.path[i+1 : i+2+j]
                    break
            if found:
                break
        
        if found:
            self.fixSelfIntersection()