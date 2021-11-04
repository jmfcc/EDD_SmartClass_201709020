class NodeCourse:

    def __init__(self, code_, name_, credits_, pre_code_, required_):
        self.code = code_
        self.name = name_
        self.credits = credits_
        self.pre_code = pre_code_
        self.required = required_
        #Pointers
        self.right = None
        self.left = None
        #Height
        self.height = 0

class CoursesAVL:

    def __init__(self):
        self.Root = None

    def Max(self, val1, val2):
        if val1 > val2:
            return val1
        else:
            return val2
        
    def insertData(self, code_, name_, credits_, pre_code_, required_):
        self.Root = self.insert_intern(code_, self.Root, name_, credits_, pre_code_, required_)
    
    def height(self, node):
        if node is not None:
            return node.height
        return -1

    def insert_intern(self, code_, root, name_, credits_, pre_code_, required_):
        if root is None:
            newNode = NodeCourse(code_, name_, credits_, pre_code_, required_)
            return newNode
        else:
            if code_ < root.code:
                root.left = self.insert_intern(code_, root.left, name_, credits_, pre_code_, required_)
                if self.height(root.left) - self.height(root.right)== 2:
                    if code_ < root.left.code:
                        root = self.RI(root)
                    else:
                        root = self.RDI(root)
            elif code_ > root.code:
                root.right = self.insert_intern(code_, root.right, name_, credits_, pre_code_, required_)
                if self.height(root.right) - self.height(root.left)== 2:
                    if code_ > root.right.code:
                        root = self.RD(root)
                    else:
                        root = self.RDD(root)
            else:
                root.code = code_
        root.height = self.Max(self.height(root.left), self.height(root.right)) + 1

        return root

    def delete(self, code_):
        self.Root = self.delete_search(self.Root, code_)

    def delete_search(self, root_, code_):
        if root_ is not None:
            if code_ == root_.code:
                if root_.left is None and root_.right is None:
                    root_ =  None
                elif root_.left is not None and root_.right is None:
                    toDel_, replace = self.search_right_replace(root_.left)
                    if not toDel_:
                        replace.left = root_.left
                    root_ = replace
                    root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
                elif root_.left is None and root_.right is not None:
                    toDel_, replace = self.search_left_replace(root_.right)
                    if not toDel_:
                        replace.right = root_.right
                    root_ = replace
                    root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
                else:
                    toDel_, replace = self.search_right_replace(root_.left)
                    # print("Both", toDel_)
                    if not toDel_:
                        # print(replace.code)
                        replace.left = root_.left
                    replace.right = root_.right
                    root_ = replace
                    root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
            else:
                if code_ < root_.code:
                    root_.left = self.delete_search(root_.left, code_)
                    if self.height(root_.left) == -1 and self.height(root_.right) > 0:
                        root_ = self.RD(root_)
                    elif (self.height(root_.right) - self.height(root_.left)) == 2 or (self.height(root_.right) - self.height(root_.left)) == -2:
                        root_ = self.RD(root_)
                    else:
                        root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
                else:
                    root_.right = self.delete_search(root_.right, code_)
                    if self.height(root_.right) == -1 and self.height(root_.left) > 0:
                        root_ = self.RI(root_)
                    elif (self.height(root_.right) - self.height(root_.left)) == 2 or (self.height(root_.right) - self.height(root_.left)) == -2:
                        root_ = self.RI(root_)
                    else:
                        root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
        return root_
        
    def search_right_replace(self, root_):
        replace_ = None
        toDel = False
        if root_.right is not None:
            # print(root_.right.code)
            toDel, replace_ = self.search_right_replace(root_.right)
            if toDel:
                root_.right = root_.right.left
            root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
            return False, replace_
        else:
            return True, root_
        
    def search_left_replace(self, root_):
        replace_ = None
        toDel = False
        if root_.left is not None:
            toDel, replace_ = self.search_left_replace(root_.left)
            if toDel:
                root_.left = root_.left.right
            root_.height = self.Max(self.height(root_.left), self.height(root_.right)) + 1
            return False, replace_
        else:
            return True, root_

    def balance(self, root_):
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
            print("codigo:",root.code,"  Nombre:", root.name)
            self.pre_orden_intern(root.left)
            self.pre_orden_intern(root.right)

    def in_orden(self):
        self.in_orden_intern(self.Root)

    def in_orden_intern(self, root):
        if root is not None:
            self.in_orden_intern(root.left)
            print("codigo:",root.code,"  Nombre:", root.name)
            self.in_orden_intern(root.right)
    
    def post_orden(self):
        self.post_orden_intern(self.Root)
    
    def post_orden_intern(self, root):
         if root is not None:
            self.post_orden_intern(root.right)
            self.post_orden_intern(root.left)
            print("codigo:",root.code,"  Nombre:", root.name)

    #GetRecordByBynarySearch ----------------------------------------------------------------------
    def getCourse(self, code_):
        return self.getCourse_intern(code_, self.Root)

    def getCourse_intern(self, code_, root_):
        if root_ is not None:
            if code_ == root_.code:
                return root_
            else:
                if code_ < root_.code:
                    return self.getCourse_intern(code_, root_.left)
                else:
                    return self.getCourse_intern(code_, root_.right)
        return None

    #BynarySearch (Bool) ----------------------------------------------------------------------
    def searchCourse(self, code_):
        return self.searchCourse_intern(code_, self.Root)

    def searchCourse_intern(self, code_, root_):
        if root_ is not None:
            if code_ == root_.code:
                return True
            else:
                if code_ < root_.code:
                    return self.searchCourse_intern(code_, root_.left)
                else:
                    return self.searchCourse_intern(code_, root_.right)
        return False