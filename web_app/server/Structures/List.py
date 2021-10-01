from Structures.NodeS import NodeS

class List:
    def __init__(self):
        self.First = None
        self.Last = None

    def getSize(self):
        aux = self.First
        counter = 0
        while aux is not None:
            counter += 1
            aux = aux.Next()

        return counter

    def isEmpty(self):
        return self.First is None

    def getList(self):
        aux = self.First
        while aux is not None:
            print(aux.Carnet + " || " + aux.Nombre + "-" + aux.DPI + "-" + aux.Descripcion + "-" + aux.Correo)
            aux = aux.Next

    def insertValue(self, carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado):
        new_node = NodeS(carnet, dpi, nombre, carrera, password, creditos, edad, correo, descripcion, materia, fecha, hora, estado)

        if self.isEmpty():
            self.Last = new_node
            self.First = self.Last
        else:
            self.Last.Next = new_node
            new_node.Previous = self.Last
            self.Last = new_node

    def clear(self):
        self.First = None
        self.Last = None
