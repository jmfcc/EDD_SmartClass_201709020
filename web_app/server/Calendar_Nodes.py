class NodeColumnDay:
    def __init__(self, day_):
        self.day = day_
        self.next = None
        self.prev = None
        self.accesNodeCell = None

class NodeRowHour:
    def __init__(self, hour_):
        self.hour = hour_
        self.next = None
        self.prev = None
        self.accesNodeCell = None
    
class NodeCellTask:
    def __init__(self, day_, hour_):
        self.day = day_
        self.hour = hour_
        self.next = None
        # self.prev = None
        # self.above = None
        self.below = None
        self.accesListTasks = None
