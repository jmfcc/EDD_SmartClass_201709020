from List_Month import ListMonth
from List_Semester import ListSemester

class NodeYear:

    def __init__(self, year):
        self.year = year
        #SpecialPointers
        self.months = None
        self.semesters = None
        #Pointers
        self.next = None
        self.prev = None

class ListYear:

    def __init__(self):
        self.head = None
    
    def isEmpty(self):
        return self.head == None
    
    def insertYear(self, year):
        #Make a node year and assign a list of months
        newNode = NodeYear(year)
        l_month = ListMonth()
        l_semest = ListSemester()
        newNode.months = l_month
        newNode.semesters = l_semest

        if self.isEmpty():
            self.head = newNode
        else:
            if year < self.head.year:
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            else:
                aux = self.head
                while aux.next is not None:
                    if year < aux.next.year:
                        newNode.next = aux.next
                        aux.next.prev = newNode
                        aux.next = newNode
                        newNode.prev = aux
                        break
                    aux = aux.next

                if aux.next is None:
                    aux.next = newNode
                    newNode.prev = aux

    def searchYear(self, year):
        aux = self.head
        while aux is not None:
            if aux.year == year:
                return True
            aux = aux.next 
        return False           

    def getYear(self, year):
        aux = self.head
        while aux is not None:
            if aux.year == year:
                return aux
            aux = aux.next 
        return None
            

