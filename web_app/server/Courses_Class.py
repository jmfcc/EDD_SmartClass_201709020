from Courses_BPage import B_Page
import os

class Courses_B:

    def __init__(self):
        #Root
        self.root = None    #B-Page
        #Data Nodes BTree
        self.code = None
        self.name = None
        self.credits = None
        self.pre_codes = None
        self.required = None
        #Pointers
        self.aux1 = False
        self.aux2 = None  # B-Page
        self.toUp = False
        self.status = False
        self.compare = False
        #To Generate Graphcs
        self.graphic = ""

    def isEmpty(self, root_):
        return (root_ == None or root_.getCount() == 0)
    
    def insertData(self, code_, name_, credits_, pre_codes_, required_):
        self.__insertData(self.root, code_, name_, credits_, pre_codes_, required_)
    
    def __insertData(self, root_, code_, name_, credits_, pre_codes_, required_):
        self.insert(root_, code_, name_, credits_, pre_codes_, required_)
        if self.toUp:
            self.root = B_Page()
            self.root.setCount(1)
            self.root.setCode(0, self.code)
            self.root.setName(0, self.name)
            self.root.setCredits(0, self.credits)
            self.root.setPreCodes(0, self.pre_codes)
            self.root.setRequired(0, self.required)

            self.root.setPointer(0, root_)
            self.root.setPointer(1, self.aux2)

    def insert(self, root, code_, name_, credits_, pre_codes_, required_):
        pos = 0
        self.status = False
        
        if self.isEmpty(root) and self.compare == False:
            self.toUp = True

            self.code = code_
            self.name = name_
            self.credits = credits_
            self.pre_codes = pre_codes_
            self.required = required_

            self.aux2 = None
        
        else:
            pos = self.searchBNode(code_, root)
            if self.compare == False:
                if self.status:
                    self.toUp = False
                else:
                    self.insert(root.getPointer(pos), code_, name_, credits_, pre_codes_, required_)

                    if self.toUp:
                        if root.getCount() < 4:
                            self.toUp = False
                            self.insertLeaf(root, pos, self.code, self.name, self.credits, self.pre_codes, self.required)
                        else:
                            self.toUp = True
                            self.divideBPage(root, pos, self.code, self.name, self.credits, self.pre_codes, self.required)
            else:
                print("Dato Repetido", code_)
                self.compare = False
            
    def searchBNode(self, code_, root_):
        auxCount = 0
        if code_ < root_.getCode(0):
            self.status = False
            auxCount = 0
        else:
            while auxCount != root_.getCount():
                if code_ == root_.getCode(auxCount):
                    self.compare = True
                auxCount += 1
            
            auxCount = root_.getCount()

            while code_ < root_.getCode(auxCount-1) and auxCount > 1:
                auxCount -= 1
                self.status = True if (code_ == root_.getCode(auxCount-1)) else False

        return auxCount

    def insertLeaf(self, root_, pos_, code_, name_, credits_, pre_codes_, required_):
        auxC = root_.getCount()
        while auxC != pos_:
            if auxC != 0:
                root_.setCode(auxC, root_.getCode(auxC-1))
                root_.setName(auxC, root_.getName(auxC-1))
                root_.setCredits(auxC, root_.getCredits(auxC-1))
                root_.setPreCodes(auxC, root_.getPreCodes(auxC-1))
                root_.setRequired(auxC, root_.getRequired(auxC-1))
                root_.setPointer(auxC+1, root_.getPointer(auxC))
            auxC -= 1
        
        root_.setCode(pos_, code_)
        root_.setName(pos_, name_)
        root_.setCredits(pos_, credits_)
        root_.setPreCodes(pos_, pre_codes_)
        root_.setRequired(pos_, required_)
        root_.setPointer(pos_+1, self.aux2)
        root_.setCount(root_.getCount()+1)

    def divideBPage(self, root_, pos_, code_, name_, credits_, pre_codes_, required_):
        pos2 = 0
        posMed = 0
        if pos_ <= 2:
            posMed = 2
        else:
            posMed = 3
        
        rightPage = B_Page()
        pos2 = posMed + 1

        while pos2 != 5:
            if (pos2 - posMed) != 0:
                rightPage.setCode((pos2-posMed)-1, root_.getCode(pos2-1))
                rightPage.setName((pos2-posMed)-1, root_.getName(pos2-1))
                rightPage.setCredits((pos2-posMed)-1, root_.getCredits(pos2-1))
                rightPage.setPreCodes((pos2-posMed)-1, root_.getPreCodes(pos2-1))
                rightPage.setRequired((pos2-posMed)-1, root_.getRequired(pos2-1))
                rightPage.setPointer(pos2-posMed, root_.getPointer(pos2))
            
            pos2 += 1

        rightPage.setCount(4-posMed)
        root_.setCount(posMed)

        if pos_<= 2:
            self.aux1 = True
            self.insertLeaf(root_, pos_, code_, name_, credits_, pre_codes_, required_)
        else:
            self.aux1 = True
            self.insertLeaf(rightPage, (pos_-posMed), code_, name_, credits_, pre_codes_, required_)
        
        self.code = root_.getCode(root_.getCount()-1)
        self.name = root_.getName(root_.getCount()-1)
        self.credits = root_.getCredits(root_.getCount()-1)
        self.pre_codes = root_.getPreCodes(root_.getCount()-1)
        self.required = root_.getRequired(root_.getCount()-1)

        rightPage.setPointer(0, root_.getPointer(root_.getCount()))

        root_.setCount(root_.getCount() - 1)
        self.aux2 = rightPage

        if self.aux1:
            root_.setCode(3, "")
            root_.setName(3,"")
            root_.setCredits(3,"")
            root_.setPreCodes(3,"")
            root_.setRequired(3,"")
            root_.setPointer(4, None)

            root_.setCode(2, "")
            root_.setName(2,"")
            root_.setCredits(2,"")
            root_.setPreCodes(2,"")
            root_.setRequired(2,"")
            root_.setPointer(3, None)
        
    
                        
