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
        count_search = 0
        aux = self.head
        while count_search < pos:
            aux = aux.Next
        return aux
