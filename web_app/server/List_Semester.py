from Courses_Class import Courses_B

class NodeSemester:

    def __init__(self, semester):
        self.semester = semester
        #SpecialPointer
        self.courses = None
        #Pointer
        self.next = None
    
class ListSemester:

    def __init__(self):
        self.head = None
        self.size = 0

    def isEmpty(self):
        return self.head == None
    
    def insertSemester(self, sem):
        newNode = NodeSemester(sem)
        newCoursesTree = Courses_B()
        newNode.courses = newCoursesTree
        if self.isEmpty():
            self.head = newNode
        else:
            if sem < self.head.semester:
                newNode.next = self.head
                self.head = newNode
            else:
                self.head.next = newNode
        self.size += 1
    
    def searchSemester(self, sem):
        aux = self.head
        while aux is not None:
            if sem == aux.semester:
                return True
            aux = aux.next
        return False
    
    def getSemester(self, sem):
        aux = self.head
        while aux is not None:
            if sem == aux.semester:
                return aux
            aux = aux.next
        return None