# from Graph_Functions import graphDoubleList

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
            while aux.next != None:
                aux = aux.next
            aux.next = newNode
        self.size+=1

    def updateTask(self, name_, description_, course_, status_): # Not Implemented
        if self.isEmpty():
            return "No hay registros en esta fecha"
        else:
            aux = self.head
            while aux.next != None:
                aux = aux.next

    def deleteTask(self, pos): # Not Implemented
        if not self.isEmpty():
            if pos == 1:
                self.head = self.head.next
            elif pos == self.size:
                aux = self.head
                while aux.next is not None:
                    aux = aux.next
                aux = None
            else:
                count = 2
                aux = self.head
                while count <= self.size:
                    if pos == count:
                        aux.next = aux.next.next
                        break
                    count += 1
                    aux = aux.next
            self.size-=1
    
    def getTask(self, pos):
        if not self.isEmpty():
            count = 1
            aux = self.head
            while count <= self.size:
                if pos == count:
                    return aux
                count += 1
                aux = aux.next
    
# myList = ListTask()

# myList.insertTask("task 01", "test 01", "Edd", "Pending")
# myList.insertTask("task 02", "test 02", "Edd", "Acomplished")
# myList.insertTask("task 03", "test 03", "Edd", "Pending")

# graphDoubleList(myList, "")