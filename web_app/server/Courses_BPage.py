from Courses_Lists import PointerList, DoubleList

class B_Page:
    
    def __init__(self):
        self.count = 0
        self.maxClaves = 5
        self.pointers = PointerList()
        self.data = DoubleList()

        for i in range(5):
            if i != 4:
                self.data.insertNodeD("", None, None, None, None)
            self.pointers.insertPointer(None)

    def fullPage(self):
        return self.count == self.maxClaves - 1

    def preFullPage(self):
        return self.count == self.maxClaves/2

    def getCount(self):
        return self.count

    def setCount(self, count_):
        self.count = count_
    
    def getMaxClaves(self):
        return self.maxClaves
    
    def setMaxClaves(self, maxClaves_):
        self.maxClaves = maxClaves_

    def getCode(self, pos_):
        return self.data.getData(pos_).getCode()

    def setCode(self, pos_, code_):
        self.data.insertData(code_, pos_)
    
    def getName(self, pos_):
        return self.data.getData(pos_).getName()

    def setName(self, pos_, name_):
        self.data.getData(pos_).setName(name_)

    def getCredits(self, pos_):
        return self.data.getData(pos_).getCredits()
    
    def setCredits(self, pos_, credits_):
        self.data.getData(pos_).setCredits(credits_)

    def getPreCodes(self, pos_):
        return self.data.getData(pos_).getPreCode()
    
    def setPreCodes(self, pos_, pre_code_):
        self.data.getData(pos_).setPreCode(pre_code_)

    def getRequired(self, pos_):
        return self.data.getData(pos_).getRequired()
    
    def setRequired(self, pos_, required_):
        self.data.getData(pos_).setRequired(required_)
    
    def getPointer(self, pos_):
        return self.pointers.getPointer(pos_).getPointer()

    def setPointer(self, pos_, pointer_):
        self.pointers.insertPointerP(pointer_, pos_)