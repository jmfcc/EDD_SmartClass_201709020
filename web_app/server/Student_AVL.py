from List_Year import ListYear
# from Graph_Functions import graphTreeAVL

class NodeStudent:

    def __init__(self, cardnumber_, dpi_, name_, carrer_, email_, password_, credits_, age_):
        #Data Student
        self.cardnumber = cardnumber_
        self.dpi = dpi_
        self.name = name_
        self.carrer = carrer_
        self.email = email_
        self.password = password_
        self.credits = credits_
        self.age = age_
        #Ponter Years
        self.years = None
        #Pointers
        self.right = None
        self.left = None
        #Height
        self.height = 0

class StudentAVL:

    def __init__(self):
        self.Root = None

    def Max(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2
        
    def insert(self, cardnumber_, dpi_, name_, carrer_, email_, password_, credits_, age_):
        self.Root = self.insert_intern(cardnumber_, self.Root, dpi_, name_, carrer_, email_, password_, credits_, age_)
    
    def height(self, node):
        if node is not None:
            return node.height
        return -1

    def insert_intern(self, cardnumber_, root, dpi_, name_, carrer_, email_, password_, credits_, age_):
        if root is None:
            newNode = NodeStudent(cardnumber_, dpi_, name_, carrer_, email_, password_, credits_, age_)
            newListYear = ListYear()
            newNode.years = newListYear
            return newNode
        else:
            if cardnumber_ < root.cardnumber:
                root.left = self.insert_intern(cardnumber_, root.left, dpi_, name_, carrer_, email_, password_, credits_, age_)
                if self.height(root.left) - self.height(root.right)== 2:
                    if cardnumber_ < root.left.cardnumber:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif cardnumber_ > root.cardnumber:
                root.right = self.insert_intern(cardnumber_, root.right, dpi_, name_, carrer_, email_, password_, credits_, age_)
                if self.height(root.right) - self.height(root.left)== 2:
                    if cardnumber_ > root.right.cardnumber:
                        root = self.RD(root)
                    else:
                        root = self.RDD(root)
            else:
                root.cardnumber = cardnumber_
        root.height = self.Max(self.height(root.left), self.height(root.right)) + 1

        return root

    def delete_student(self, cardnumber):
        pass

    #Rotations ------------------------------------------------------------------------
    def RI(self, node):
        aux = node.left
        node.left = aux.right
        aux.right = node
        node.height = self.Max(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.Max(self.height(aux.left), self.height(aux.right)) + 1
        return aux

    def RD(self, node):
        aux = node.right
        node.right = aux.left
        aux.left = node
        node.height = self.Max(self.height(node.left), self.height(node.right)) + 1
        aux.height = self.Max(self.height(aux.left), self.height(aux.right)) + 1
        return aux

    def RDI(self, node):
        node.left = self.RD(node.left)
        return self.RI(node)

    def RDD(self, node): # RID
        node.right = self.RI(node.right)
        return self.RD(node)

    #Traversing AVL Tree -------------------------------------------------------------
    def pre_orden(self):
        self.pre_orden_intern(self.Root)
    
    def pre_orden_intern(self, root):
        if root is not None:
            print("Carnet:",root.cardnumber,"  Nombre:", root.name)
            self.pre_orden_intern(root.left)
            self.pre_orden_intern(root.right)

    def in_orden(self):
        self.in_orden_intern(self.Root)

    def in_orden_intern(self, root):
        if root is not None:
            self.in_orden_intern(root.left)
            print("Carnet:",root.cardnumber,"  Nombre:", root.name)
            self.in_orden_intern(root.right)
    
    def post_orden(self):
        self.post_orden_intern(self.Root)
    
    def post_orden_intern(self, root):
         if root is not None:
            self.post_orden_intern(root.right)
            self.post_orden_intern(root.left)
            print("Carnet:",root.cardnumber,"  Nombre:", root.name)

    #GetRecordByBynarySearch ----------------------------------------------------------------------
    def getStudent(self, cardnumber_):
        return self.getStudent_intern(cardnumber_, self.Root)

    def getStudent_intern(self, cardnumber_, root_):
        if root_ is not None:
            if cardnumber_ == root_.cardnumber:
                return root_
            else:
                if cardnumber_ < root_.cardnumber:
                    return self.getStudent_intern(cardnumber_, root_.left)
                else:
                    return self.getStudent_intern(cardnumber_, root_.right)
        return None

    #BynarySearch (Bool) ----------------------------------------------------------------------
    def searchStudent(self, cardnumber_):
        return self.searchStudent_intern(cardnumber_, self.Root)

    def searchStudent_intern(self, cardnumber_, root_):
        if root_ is not None:
            if cardnumber_ == root_.cardnumber:
                return True
            else:
                if cardnumber_ < root_.cardnumber:
                    return self.searchStudent_intern(cardnumber_, root_.left)
                else:
                    return self.searchStudent_intern(cardnumber_, root_.right)
        return False

    #DeleteStudent -----------------------------------------------------------------------
    
            # -------- NOT IMPLEMENTED ------------

    #Others ----------------------------------------------------------------------------
    
            # -------- NOT IMPLEMENTED ------------


# studentTree = StudentAVL()
# studentTree.insert(201709020, 0, "Jaime", "Sistemas", "jaime@gmail.com", "asdf", 100, 25)
# studentTree.insert(201709283, 0, "Fulano", "Sistemas", "fulano@gmail.com", "asdf", 100, 25)
# studentTree.insert(201402113, 0, "Mengano", "Sistemas", "mengano@gmail.com", "asdf", 100, 25)
# studentTree.insert(201013171, 0, "Vinicio", "Sistemas", "vinicio@gmail.com", "asdf", 100, 25)
# studentTree.insert(200611000, 0, "Norma", "Sistemas", "norma@gmail.com", "asdf", 100, 25)
# studentTree.insert(202001808, 0, "Fabian", "Sistemas", "fabian@gmail.com", "asdf", 100, 25)
# studentTree.insert(202007708, 0, "Melchor", "Sistemas", "melchor@gmail.com", "asdf", 100, 25)
# studentTree.insert(201904442, 0, "Rigoberto", "Sistemas", "rigoberto@gmail.com", "asdf", 100, 25)

# studentTree.in_orden()
# print("----------------------------------------")
# # studentTree.pre_orden()
# # print("----------------------------------------")
# # studentTree.post_orden()
# print()

# record = studentTree.getStudent(202007708)
# if record != None:
#     print(record.email)
#     record.name = "Modify On Extern Node"
#     if record.years.head == None:
#         print(" --- None Years Records ---")
# else:
#     print(" >> Error: 0 matches")

# print()
# print("----------------------------------------")
# graphTreeAVL(studentTree)
# # studentTree.in_orden()
