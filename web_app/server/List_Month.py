from Calendar_Class import CalendarTask

class NodeMonth:
    def __init__(self, month_):
        self.month = month_
        self.next = None
        self.prev = None
        self.calendar = None

class ListMonth:
    def __init__(self):
        self.head = None
    def isEmpty(self):
        return self.head == None
    def insertMonth(self, month_):
        newNode = NodeMonth(month_)
        if self.isEmpty():
            tempCalendar = CalendarTask(month_)
            newNode.calendar = tempCalendar
            self.head = newNode
        else:
            if month_ < self.head:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            else:
                aux = self.head
                while aux.next != None:
                    if month_ < aux.next.month:
                        newNode.next = aux.next
                        aux.next.prev = newNode
                        aux.next = newNode
                        newNode.prev = aux
                        break
                    aux = aux.next
                if aux.next == None:
                    aux.next = newNode
                    newNode.prev = aux

    def searchMonth(self, month_):
        aux = self.head
        while aux is not None:
            if aux.month == month_:
                return True
            aux = aux.next
        return False

    def getMonth(self, month_):
        aux = self.head
        while aux is not None:
            if aux.month == month_:
                return aux
            aux = aux.next
        return None
    
    