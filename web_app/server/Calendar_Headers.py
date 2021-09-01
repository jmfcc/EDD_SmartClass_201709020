from Calendar_Nodes import NodeColumnDay, NodeRowHour, NodeCellTask


class ListHeaderDay:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getHeaderDay(self, day_):
        aux = self.head
        while aux != None:
            if aux.day == day_:
                return aux
            aux = aux.next
        return None
    
    def setHeaderDay(self, newNHD):
        if self.isEmpty():
            self.head = newNHD
        elif newNHD.day < self.head.day:
            newNHD.next = self.head
            self.head.prev = newNHD
            self.head = newNHD
        else:
            aux = self.head
            while aux.next != None:
                if newNHD.day < aux.next.day:  # 23 - 12 14 25
                    newNHD.next = aux.next
                    aux.next.prev = newNHD
                    newNHD.prev = aux
                    aux.next = newNHD
                    break
                aux = aux.next
            if aux.next == None:
                aux.next = newNHD
                newNHD.prev = aux

class ListHeaderHour:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def getHeaderHour(self, hour_):
        aux = self.head
        while aux != None:
            if aux.hour == hour_:
                return aux
            aux = aux.next
        return None
    
    def setHeaderHour(self, newNHH):
        if self.isEmpty():
            self.head = newNHH
        elif newNHH.hour < self.head.hour:
            newNHH.next = self.head
            self.head.prev = newNHH
            self.head = newNHH
        else:
            aux = self.head
            while aux.next != None:
                if newNHH.hour < aux.next.hour:  # 23 - 12 14 25
                    newNHH.next = aux.next
                    aux.next.prev = newNHH
                    newNHH.prev = aux
                    aux.next = newNHH
                    break
                aux = aux.next
            if aux.next == None:
                aux.next = newNHH
                newNHH.prev = aux


                