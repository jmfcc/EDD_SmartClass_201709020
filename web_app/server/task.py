
class NodeTask:

    def __init__(self, name_, description_, course_, status_):
        self.name = name_
        self.description = description_
        self.course = course_
        self.status = status_
        self.next = None
        

class ListTask:

    def __init__(self):
        self.head = None
        self.size = 0

    def getHead(self):
        return self.head

    def isEmpty(self):
        return self.head == None
    
    def insertTask(self, name_, description_, course_, status_):
        newNode = NodeTask(name_, description_, course_, status_)
        if self.isEmpty():
            self.head = newNode
        else:
            aux = self.head
            while aux.getNext() != None:
                aux = aux.getNext()
            aux.setNext(newNode)
        self.size+=1

    def updateTask(self, name_, description_, course_, status_): # Not Implemented
        if self.isEmpty():
            return "No hay registros en esta fecha"
        else:
            aux = self.head
            while aux.getNext() != None:
                aux = aux.getNext()

    def deleteTask(self): # Not Implemented
        pass
        self.size-=1
    
    
