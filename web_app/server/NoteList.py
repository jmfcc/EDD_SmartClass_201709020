class NodeNote:
    def __init__(self, title, note):
        self.title = title
        self.note = note
        self.Next = None
        self.Previous = None

class NoteList:
    def __init__(self):
        self.card_number = None
        self.head = None
        self.size = 0
    
    def is_empty(self):
        return self.head == None

    def insert_note(self, title, note):
        new_note = NodeNote(title, note)
        if self.is_empty():
            self.head = new_note
        else:
            self.head.Previous = new_note
            new_note.Next = self.head
            self.head = new_note
        self.size += 1
        
    def search_note(self, pos):
        count_search = 1
        aux = self.head
        while count_search != pos:
            aux = aux.Next
        return aux
    
    def delete_note(self, pos):
        count_search = 1
        if pos == 1:
            self.head = self.head.Next
            if self.head != None:
                self.head.Previous = None
        elif pos == self.size:
            aux = self.head
            while aux.Next != None:
                aux = aux.Next
            aux.Previous.Next = None
            aux = None
        else:
            aux = self.head
            while count_search != pos:
                aux = aux.Next
                count_search += 1
            aux.Previous.Next = aux.Next
            aux.Next.Previous = aux.Previous
            aux = None

    def getFormatData(self):
        aux = self.head
        data = []
        count = 1
        while aux != None:
            datadict = {
                "pos":count,
                "titulo":aux.title,
                "contenido":aux.note
            }
            data.append(datadict.copy())
            aux = aux.Next
            count += 1
        return data

    def validaPos(self, pos):
        if 0 < pos <= self.size:
            return True
        return False

