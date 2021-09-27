class DoubleNode:

    def __init__(self, code_, name_, credits_, pre_code_, required_):
        self.code = code_
        self.name = name_
        self.credits = credits_
        self.pre_code = pre_code_
        self.required = required_
        self.next = None
        self.prev = None

    def getCode(self):
        return self.code
    def getName(self):
        return self.name
    def getCredits(self):
        return self.credits
    def getPreCode(self):
        return self.pre_code
    def getRequired(self):
        return self.required
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

    def setCode(self, val_):
        self.code = val_
    def setName(self, val_):
        self.name = val_
    def setCredits(self, val_):
        self.credits = val_
    def setPreCode(self, val_):
        self.pre_code = val_
    def setRequired(self, val_):
        self.required = val_
    def setNext(self, val_):
        self.next = val_
    def setPrev(self, val_):
        self.prev = val_

class NodePointer:

    def __init__(self, pointer_):
        self.pointer = pointer_
        self.next = None
        self.prev = None

    def getPointer(self):
        return self.pointer
    def getNext(self):
        return self.next
    def getPrev(self):
        return self.prev

    def setPointer(self, val_):
        self.pointer = val_
    def setNext(self, val_):
        self.next = val_
    def setPrev(self, val_):
        self.prev = val_

