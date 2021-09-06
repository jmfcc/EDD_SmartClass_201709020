from Calendar_Nodes import NodeCellTask, NodeColumnDay, NodeRowHour
from Calendar_Headers import ListHeaderDay, ListHeaderHour
from task import ListTask

class CalendarTask:
    def __init__(self, month_):
        self.month = month_
        self.days = ListHeaderDay()
        self.hours = ListHeaderHour()

    def insertNewCellData(self, hour, day):
        newNodeCell = NodeCellTask(day, hour)  # ---- Celda con apuntador a lista tareas
        
        # INSERT BY DAY (COLS)
        columnDay = self.days.getHeaderDay(day)
        if columnDay == None:
            columnDay = NodeColumnDay(day)
            self.days.setHeaderDay(columnDay)

            newListTask = ListTask()   # ------------- Creando LISTA DE TAREAS
            newNodeCell.accesListTasks = newListTask # ----
            columnDay.accesNodeCell = newNodeCell # Asignando Nodo Celda
        else:
            if hour == columnDay.accesNodeCell.hour:  # if the node already exist only add the new task
                pass
            elif hour < columnDay.accesNodeCell.hour:
                newListTask = ListTask()   # ------------- Creando LISTA DE TAREAS
                newNodeCell.accesListTasks = newListTask # ----

                newNodeCell.below = columnDay.accesNodeCell
                columnDay.accesNodeCell = newNodeCell
            else:
                aux = columnDay.accesNodeCell
                while aux.below != None:
                    if hour == aux.below.hour: # if the node already exist only add the new task
                        break
                    elif hour < aux.below.hour:
                        newListTask = ListTask()   # ------------- Creando LISTA DE TAREAS
                        newNodeCell.accesListTasks = newListTask # ----

                        newNodeCell.below = aux.below
                        aux.below = newNodeCell
                        break
                    aux = aux.below
                if aux.below == None:
                    newListTask = ListTask()   # ------------- Creando LISTA DE TAREAS
                    newNodeCell.accesListTasks = newListTask # ----

                    aux.below = newNodeCell
        
        # INSERT BY HOUR (ROWS)
        rowHour = self.hours.getHeaderHour(hour) # rowHour = NodeRowHour()
        if rowHour == None:
            rowHour = NodeRowHour(hour)
            rowHour.accesNodeCell = newNodeCell
            self.hours.setHeaderHour(rowHour)
        else:
            if day == rowHour.accesNodeCell.day:
                pass
            elif day < rowHour.accesNodeCell.day:
                newNodeCell.next = rowHour.accesNodeCell
                rowHour.accesNodeCell = newNodeCell
            else:
                aux = rowHour.accesNodeCell
                while aux.next != None:
                    if day == aux.next.day:
                        break
                    elif day < aux.next.day:
                        newNodeCell.next = aux.next
                        aux.next = newNodeCell
                        break
                    aux = aux.next
                if aux.next == None:
                    aux.next = newNodeCell

    def getCellCalendar(self, hour, day):
        col = self.days.getHeaderDay(day)
        # col = NodeColumnDay()
        if col != None:
            aux = col.accesNodeCell
            # aux = NodeCellTask()
            while aux != None:
                if aux.hour == hour:
                    return aux
                aux = aux.below
        return None

    def insertNewTask(self, hour, day, name, desc, course, status):
        toInserTask = self.getCellCalendar(hour, day)
        # toInserTask = NodeCellTask()
        if toInserTask == None:
            self.insertNewCellData(hour, day)
            toInserTask = self.getCellCalendar(hour, day)
        toInserTask.accesListTasks.insertTask(name, desc, course, status) # añadiendo tarea

    def recorreDiaHora(self):
        dayCol = self.days.head
        # dayCol = NodeColumnDay()
        while dayCol != None:
            hourRow = dayCol.accesNodeCell
            # hourRow = NodeCellTask()
            while hourRow != None:
                text = "D: "+str(hourRow.day) + ", H: " + str(hourRow.hour)
                print(text, end="\t\t")
                hourRow = hourRow.below
            print("")
            dayCol = dayCol.next
    def recorreHoraDia(self):
        hourRow = self.hours.head
        # hourRow = NodeRowHour()
        while hourRow != None:
            dayCol = hourRow.accesNodeCell
            # dayCol = NodeCellTask()
            while dayCol != None:
                text = "H: " + str(dayCol.hour)+ ", D: "+str(dayCol.day) 
                print(text, end="\t\t")
                dayCol = dayCol.next
            print("")
            hourRow = hourRow.next


# myCalendar = CalendarTask(8)
# myCalendar.insertNewTask(8, 8, "Tarea1", "Ingresada para el 8/8 - 8:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(11, 7, "Tarea2", "Ingresada para el 7/8 - 11:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(14, 12, "Tarea3", "Ingresada para el 12/8 - 14:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(16, 23, "Tarea4", "Ingresada para el 23/8 - 16:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(8, 9, "Tarea5", "Ingresada para el 9/8 - 8:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(7, 12, "Tarea6", "Ingresada para el 12/8 - 7:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(14, 9, "Tarea7", "Ingresada para el 9/8 - 14:00", "EDD", "Cumplida")
# myCalendar.insertNewTask(9, 23, "Tarea8", "Ingresada para el 23/8 - 9:00", "EDD", "Cumplida")

# # myCalendar.recorreDiaHora()
# myCalendar.recorreHoraDia()