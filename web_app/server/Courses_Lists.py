from Courses_Nodes import NodePointer, DoubleNode

class PointerList:

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0
    
    def isEmpty(self):
        return self.first == None

    def insertPointer(self, pointer_):
        newNode = NodePointer(pointer_)
        if self.count < 5:
            if self.isEmpty():
                self.first = newNode
                self.last = newNode
            else:
                self.last.setNext(newNode)
                newNode.setPrev(self.last)
                self.last = newNode
            self.count += 1
    
    def insertPointerP(self, page_, pos_):
        aux = self.first
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getNext()
        aux.setPointer(page_)
    
    def getPointer(self, pos_):
        aux = self.first
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getNext()
        return aux

    def getFirst(self):
        return self.first
    
    def setFirst(self, first_):
        self.first = first_
    
    def getCount(self):
        return self.count

    def setCount(self, count_):
        self.count = count_

class DoubleList:

    def __init__(self):
        self.first = None
        self.last = None
        self.count = 0

    def isEmpty(self):
        return self.first == None
    
    def insertNodeD(self, code_, name_, credits_, pre_code_, required_):
        newNode = DoubleNode(code_, name_, credits_, pre_code_, required_)
        if self.count < 4:
            if self.isEmpty():
                self.first = newNode
                self.last = newNode
            else:
                self.last.setNext(newNode)
                newNode.setPrev(self.last)
                self.last = newNode

            self.count += 1

    def insertData(self, code_, pos_):
        aux = self.first
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getNext()
        aux.setCode(code_)
        
    def getData(self, pos_):
        aux = self.first
        while pos_ != 0:
            pos_ -= 1
            aux = aux.getNext()
        return aux
    
    def showData(self):
        aux = self.first
        while aux != None:
            print("Dato",aux.getCode())
            aux = aux.getNext()
