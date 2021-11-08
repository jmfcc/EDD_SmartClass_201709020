from NoteList import NoteList
# from Graph_Functions import graphHashTable
class TablaHash:

    def __init__(self):
        self.table_size = 7
        self.hash_list = [None,None,None,None,None,None,None]

    def get_table(self):
        print("-"*30)
        for i in range(self.table_size):
            info = ""
            if self.hash_list[i] != None:
                info = str(self.hash_list[i].card_number) + " - #Notas: " + str(self.hash_list[i].size)
            if i < 10:
                print(" " + str(i) + ") " + info)
            else:
                print(str(i) + ") " + info)
        print("-"*30)

    def calculate_relative_position(self, pos_increment):
        return pos_increment%self.table_size

    def add_to_table(self, card_number):
        list_notes = NoteList()
        list_notes.card_number = card_number
        self.add_hash_index(list_notes)

    def add_hash_index(self, list_notes):
        position = self.get_position_table(list_notes.card_number)
        if self.hash_list[position] == None:
            self.hash_list[position] = list_notes
        else:
            ciclado = 1
            position_init = position
            while True:
                if self.hash_list[position] == None:
                    self.hash_list[position] = list_notes
                    # print(" >> Insertado en: ", position)
                    break
                else:
                    if self.hash_list[position].card_number == list_notes.card_number:
                        return
                    # print(" >> Colision con indice: ", position, " -- Del carnet: ", list_notes.card_number)
                # print(" >> Calculo cuadratico: ", position_init, "- aumento:", ciclado**2)
                position = self.calculate_relative_position(position_init + ciclado**2)
                # print(" >> Calculo posición relativa: ", position)
                
                if ciclado > 75:
                    print("Ciclado > 75(veces)")
                    return
                ciclado += 1   
        self.do_rehash()

    def do_rehash(self):
        if self.get_percent_use() >= 0.50:
            # self.get_table()
            # print("-"*12 + " REHASH " + "-"*12)
            to_rehash = self.hash_list.copy()
            self.hash_list.clear()
            self.table_size = self.get_next_prime(self.table_size)
            for i in range(self.table_size):
                self.hash_list.append(None)
            #--------rehash -----------------------
            for data in to_rehash:
                if data != None:
                    self.add_hash_index(data)

    def insert_new_note(self, card_number, title, note):
        self.add_to_table(card_number)
        position = self.get_position_table(card_number)
        if self.hash_list[position] == None:
            # print("No se encontró el carnet")
            return "Error la posición esta vacía (rehashing incorrecto)"
        else:
            ciclado = 1
            position_init = position
            while True:
                if self.hash_list[position] != None:
                    if self.hash_list[position].card_number == card_number:
                        self.hash_list[position].insert_note(title, note)
                        # print(" >> Nota insertada en: ", position, " -- para: ", card_number)
                        break
                    # else:
                        # print(" >> Colision con indice: ", position, " -- Del carnet: ", card_number)
                else:
                    # print(" >> No hay colision con indice: ", position, " -- El hash del carnet: ", card_number, " no existe")
                    return "Error no hay un carnet {} registrado".format(str(card_number))
                # print(" >> Calculo cuadratico: ", position_init, "- aumento:", ciclado**2)
                position = self.calculate_relative_position(position_init + ciclado**2)
                # print(" >> Calculo posición relativa: ", position)
                
                if ciclado > 75:
                    print("Ciclado > 75(veces)")
                    return "Ciclado"
                ciclado += 1

    def get_position_table(self, card_number):
        return card_number % self.table_size

    def get_next_prime(self, initial_size):
        return self.next_prime(initial_size+1)
    
    def get_percent_use(self):
        counter = 0
        for i in range(self.table_size):
            if self.hash_list[i] != None:
                counter += 1
        return counter/self.table_size

    def next_prime(self, value):
        if value%2 == 0:
            return self.next_prime(value+1)
        else:
            for i in range(2, value//2):
                if value%i == 0:
                    return self.next_prime(value+1)
        return value

    def getNotes(self, cardnumber_):
        dataNotes = self.getNotesBySearch(cardnumber_)
        if isinstance(dataNotes, NoteList):
            return dataNotes.getFormatData()
        return dataNotes
        
    def delNote(self, cardnumber_, pos_):
        dataNotes = self.getNotesBySearch(cardnumber_)
        if isinstance(dataNotes, NoteList):
            if dataNotes.validaPos(pos_):
                dataNotes.delete_note(pos_)
                return "Nota eliminada"
            else:
                return "Index fuera de rango"
        return dataNotes

    def getNotesBySearch(self, cardnumber_):
        position = self.get_position_table(cardnumber_)
        if self.hash_list[position] == None:
            # print("No se encontró el carnet")
            return "--- Sin apuntes ---"
        else:
            ciclado = 1
            position_init = position
            while True:

                if self.hash_list[position] != None:
                    if self.hash_list[position].card_number == cardnumber_:
                        return self.hash_list[position]
                else:
                    return "Error no hay un carnet {} registrado".format(str(cardnumber_))
                position = self.calculate_relative_position(position_init + ciclado**2)

                if ciclado > 75:
                    print("Ciclado > 75(veces)")
                    return "Ciclado"
                ciclado += 1

# -----------------------------------------------------------------------------
# -----------------------------TESTING-----------------------------------------
# -----------------------------------------------------------------------------

# hash_test = TablaHash()
# hash_test.insert_new_note(200848002,"titulo1","nota1")
# hash_test.insert_new_note(201092489,"titulo1","nota1")
# hash_test.insert_new_note(201402040,"titulo1","nota1")
# hash_test.insert_new_note(201800304,"titulo1","nota1")
# hash_test.insert_new_note(201800304,"titulo2","nota2")
# hash_test.insert_new_note(201403055,"titulo1","nota1")
# hash_test.insert_new_note(201202304,"titulo1","nota1")
# hash_test.insert_new_note(201304492,"titulo1","nota1")
# hash_test.insert_new_note(201403055,"titulo2","nota2")
# hash_test.insert_new_note(200848002,"titulo2","nota2")
# hash_test.insert_new_note(201092489,"titulo2","nota2")
# hash_test.insert_new_note(201402040,"titulo2","nota2")
# hash_test.insert_new_note(201402040,"titulo3","nota3")
# hash_test.insert_new_note(201800304,"titulo3","nota3")
# hash_test.insert_new_note(201202304,"titulo2","nota2")
# hash_test.insert_new_note(201304492,"titulo2","nota2")
# hash_test.insert_new_note(201403055,"titulo3","nota3")
# hash_test.insert_new_note(201535789,"titulo1","nota1")
# hash_test.insert_new_note(201230524,"titulo1","nota1")
# hash_test.insert_new_note(201709020,"titulo1","nota1")
# hash_test.insert_new_note(201949742,"titulo1","nota1")
# hash_test.insert_new_note(202000402,"titulo1","nota1")
# hash_test.insert_new_note(201504801,"titulo1","nota1")
# hash_test.insert_new_note(201202304,"titulo3","nota3")
# hash_test.insert_new_note(201304492,"titulo3","nota3")
# hash_test.insert_new_note(201402040,"titulo4","nota4")
# hash_test.insert_new_note(200220144,"titulo1","nota1")
# hash_test.insert_new_note(201709020,"titulo2","nota2")
# hash_test.insert_new_note(201949742,"titulo2","nota2")
# hash_test.insert_new_note(202000402,"titulo2","nota2")
# hash_test.insert_new_note(201709020,"titulo3","nota3")
# hash_test.insert_new_note(201800304,"titulo4","nota4")
# hash_test.insert_new_note(201800304,"titulo5","nota5")
# hash_test.insert_new_note(201402040,"titulo5","nota5")
# hash_test.insert_new_note(201709020,"titulo4","nota4")
# # hash_test.get_table()
# print(hash_test.getNotes(201709020))
# ------------ Prime Generator Test ---------------------
# val_list = [3]
# for i in range(125):
#     val_list.append(hash_test.get_next_prime(val_list[-1]))
# print(val_list)

# Demo de blockchain
# https://andersbrownworth.com/blockchain/blockchain

# graphHashTable(hash_test)   