from datetime import date
from os import name
from flask import Flask, json, jsonify, request, Response
from flask_cors import CORS
from Student_AVL import StudentAVL
from Graph_Functions import graphDoubleList, graphTreeAVL, graphDMatrix

records = StudentAVL()

app = Flask(__name__)
CORS(app)

# #####################################################################################################################
# ########                                               HELPERS                                               ########
# #####################################################################################################################

def isValid(*args):
  for val in args:
    if not val:
      return False
  return True

def splitDate(date_):
  if date_.count("/") == 2:
    sep = date_.split("/")
    return True, int(sep[0]), int(sep[1]), int(sep[2])
  return False, "", "", ""

def splitHour(hour_):
  if hour_.count(":") == 1:
    sep = hour_.split(":")
    return int(sep[0])
  return ""

# #####################################################################################################################
# ########                                              ENDPOINTS                                              ########
# #####################################################################################################################

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/carga", methods=["POST"]) ################################################
def loadFile():
  try:
    data = request.get_json(force=True)
    type_ = data["tipo"]
    path_ = data["path"]
    #Load -----------------------------------------------
    #     ----- NOT IMPLEMENTED -----------
    #     ----- NOT IMPLEMENTED -----------
    return jsonify({ "response" : "I'm loading:" + path_ })
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/reporte", methods=["GET"]) ###############################################
def report():
  try:
    data = request.get_json(force=True)
    type_ = data["tipo"]
    #Validation of type -----------------------------------------------
    msg = "Try generate a report"
    if type_ == 0: # AVL REPORT
      graphTreeAVL(records)
      msg = " >> Info: Arbol AVL de estudiantes generado exitosamente"
    elif type_ == 1: # DISP MATRIX TASK
      cardnumber_ = data["carnet"]
      year_ = data["año"]
      month_ = data["mes"]
      #----------------------------------------------------------------
      if isValid(cardnumber_, year_, month_):
        if records.searchStudent(cardnumber_):
          data = records.getStudent(cardnumber_) # NodeStudent
          if not data.years.isEmpty() and data.years.searchYear(int(year_)):
            data = data.years.getYear(int(year_)) # NodeYear
            if not data.months.isEmpty() and data.months.searchMonth(month_):
              data = data.months.getMonth(month_) # NodeMonth
              # data = data.calendar.getCellCalendar(hour_, day_) # NodeCellTask
              graphDMatrix(data.calendar)
              msg = " >> Info: Grafo matriz de tareas generado exitosamente"
            else:
              msg = " >> Error: no hay registros del mes {}".format(str(year_))
          else:
            msg = " >> Error: no hay registros del año {}".format(str(year_))
        else:
          msg = " >> Error: No hay registros de {}".format(str(cardnumber_))
      else:
        msg = " >> Error: Verifique sus datos"
    elif type_ == 2: # LINKEDLIST TASK
      cardNumber_ = data["carnet"]
      year_ = data["año"]
      month_ = data["mes"]
      day_ = data["dia"]
      hour_ = data["hora"]
      if isValid(cardNumber_, year_, month_, day_, hour_):
        if records.searchStudent(cardNumber_):
          data = records.getStudent(cardNumber_) # NodeStudent
          if not data.years.isEmpty() and data.years.searchYear(int(year_)):
            data = data.years.getYear(int(year_)) # NodeYear
            if not data.months.isEmpty() and data.months.searchMonth(month_):
              data = data.months.getMonth(month_) # NodeMonth
              data = data.calendar.getCellCalendar(hour_, day_) # NodeCellTask
              if data is not None:
                dataStud = 'Carne: {}\\nFecha: {}/{}/{}\\nHora: {}:00'.format(cardNumber_, str(day_), str(month_), str(year_), str(hour_))
                graphDoubleList(data.accesListTasks, dataStud)
                msg = " >> Info: Lista de tareas generado exitosamente"
              else:
                msg = " >> Error: no hay registros en la fecha {}/{}/{} y hora {}:00".format(str(day_), str(month_), str(year_), str(hour_))
            else:
              msg = " >> Error: no hay registros del mes {}".format(str(year_))
          else:
            msg = " >> Error: no hay registros del año {}".format(str(year_))
        else:
          msg = " >> Error: No hay registros de {}".format(str(cardNumber_))
      else:
        msg = " >> Error: Verifique sus datos"
    elif type_ == 3: # B-TREE PENSUM
      pass
    elif type_ == 4: # B-TREE COURSES
      pass
    return jsonify({ "response" : msg })
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD ESTUDIANTES                                                     ---
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/estudiante", methods=["POST"])
def studentInsert():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    dpi_ = data["dpi"]
    name_ = data["nombre"]
    carrer_ = data["carrera"]
    email_ = data["correo"]
    passw_ = data["password"]
    credits_ = data["creditos"]
    age_ = data["edad"]
    msg = "I'm saving a student data " 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_):
      if records.searchStudent(cardnumber_):
        msg = " >> Info: El carnet {} ya está registrado".format(cardnumber_)
      else:
        records.insert(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_)
        msg = " >> Info: Datos del estudiante almacenados correctamente" 
    else:
      msg = " >> Error: Verifique sus datos"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/estudiante", methods=["UPDATE"])
def studentUpdate():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    dpi_ = data["DPI"]
    name_ = data["nombre"]
    carrer_ = data["carrera"]
    email_ = data["correo"]
    passw_ = data["password"]
    credits_ = data["creditos"]
    age_ = data["edad"]
    msg = "I'm update a student data " 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_) # NodeStudent
        data.dpi = dpi_
        data.name = name_
        data.carrer = carrer_
        data.email = email_
        data.password = passw_
        data.credits = credits_
        data.age = age_
        msg = " >> Info: Datos de estudiante actualizados correctamente" 
      else:
        msg = " >> Error: No hay registros del carnet {}".format(cardnumber_)
    else:
      msg = " >> Error: Verifique sus datos"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/estudiante", methods=["DELETE"])  ###########################################
def studentDelete():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    #Validation of type -----------------------------------------------
    #     ----- NOT IMPLEMENTED -----------
    return jsonify({ "response" : "I'm deleting a student with cardnumber:" + cardnumber_ })
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/estudiante", methods=["GET"])
def studentSelect():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    msg = "Get the data of student"
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_)
        msg = {
          "carnet": data.cardnumber,
          "dpi": data.dpi,
          "nombre": data.name,
          "carrera": data.carrer,
          "correo": data.email,
          "password": data.password,
          "creditos": data.credits,
          "edad": data.age
        }
      else:
        msg = " >> Error: No hay registros del carnet {}".format(cardnumber_)
    else:
      msg = " >> Error: Verifique sus datos"
    #     ----- NOT IMPLEMENTED -----------
    #     ----- NOT IMPLEMENTED -----------
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD RECORDATORIOS                                                   ---
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/recordatorios", methods=["POST"])
def taskInsert():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    name_ = data["nombre"]
    desc_ = data["descripcion"]
    course_ = data["materia"]
    date_ = data["fecha"]
    hour_ = data["hora"]
    status_ = data["estado"]
    msg = "I'm will add a task for student"
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, name_, desc_, course_, date_, hour_, status_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_) # NodeStudent
        valid, day_, month_, year_ = splitDate(date_)
        if valid:
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
          else:
            data.years.insertYear(year_)
            data = data.years.getYear(year_) # NodeYear
          if not data.months.isEmpty() and data.months.searchMonth(month_):
            data = data.months.getMonth(month_) # NodeMonth
          else:
            data.months.insertMonth(month_)
            data = data.months.getMonth(month_) # NodeMonth
          hour_ = splitHour(hour_)
          data.calendar.insertNewTask(hour_, day_, name_, desc_, course_, status_)
          msg = " >> Info: Tarea almacenada {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
        else:
          msg = " >> Error: La fecha {} no tiene el formato correcto".format(date_)
      else:  
        msg = " >> Error: El carnet no existe"
    else:
      msg = " >> Error: Verifique sus datos"

    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/recordatorios", methods=["UPDATE"])
def taskUpdate():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    name_ = data["nombre"]
    desc_ = data["descripcion"]
    course_ = data["materia"]
    date_ = data["fecha"]
    hour_ = data["hora"]
    status_ = data["estado"]
    pos_ = data["posicion"]
    msg = "Actualzando una tarea"
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, name_, desc_, course_, date_, hour_, status_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_) # NodeStudent
        valid, day_, month_, year_ = splitDate(date_)
        if valid:
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
            if not data.months.isEmpty() and data.months.searchMonth(month_):
              hour_ = splitHour(hour_)
              data = data.months.getMonth(month_) # NodeMonth
              data = data.calendar.getCellCalendar(hour_, day_) # NodeCellTask
              if data is not None:
                taskData = data.accesListTasks.getTask(pos_) # NodeTask
                taskData.name = name_
                taskData.description = desc_
                taskData.course = course_
                taskData.status = status_
                msg = " >> Info: Se han actualizado los datos de la tarea"
              else:
                msg = " >> Error: no hay registros en la fecha {}/{}/{} y hora {}:00".format(str(day_), str(month_), str(year_), str(hour_))
            else:
              msg = " >> Error: No hay tarea registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
          else:
            msg = " >> Error: No hay tareas registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
        else:
          msg = " >> Error: La fecha {} no tiene el formato correcto".format(date_)
      else:  
        msg = " >> Error: El carnet no existe"
    else:
      msg = " >> Error: Verifique sus datos"
    #     ----- NOT IMPLEMENTED -----------
    #     ----- NOT IMPLEMENTED -----------
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/recordatorios", methods=["GET"])
def taskSelect():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    date_ = data["fecha"]
    hour_ = data["hora"]
    pos_ = data["posicion"]
    msg = "Obteniendo una tarea"
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, date_, hour_, pos_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_) # NodeStudent
        valid, day_, month_, year_ = splitDate(date_)
        if valid:
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
            if not data.months.isEmpty() and data.months.searchMonth(month_):
              hour_ = splitHour(hour_)
              data = data.months.getMonth(month_) # NodeMonth
              data = data.calendar.getCellCalendar(hour_, day_) # NodeCellTask
              if data is not None:
                taskData = data.accesListTasks.getTask(pos_) # NodeTask
                msg = {
                  "Carnet":cardnumber_,
                  "Fecha":date_,
                  "Hora": str(hour_)+":00",
                  "Nombre":taskData.name,
                  "Descripcion":taskData.description,
                  "Curso":taskData.course,
                  "Estado":taskData.status
                }
              else:
                msg = " >> Error: no hay registros en la fecha {}/{}/{} y hora {}:00".format(str(day_), str(month_), str(year_), str(hour_))
            else:
              msg = " >> Error: No hay tarea registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
          else:
            msg = " >> Error: No hay tareas registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
        else:
          msg = " >> Error: La fecha {} no tiene el formato correcto".format(date_)
      else:  
        msg = " >> Error: El carnet no existe"
    else:
      msg = " >> Error: Verifique sus datos"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/recordatorios", methods=["DELETE"])
def taskDelete():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    date_ = data["fecha"]
    hour_ = data["hora"]
    pos_ = data["posicion"]
    msg = "Eliminando una tarea"
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, date_, hour_, pos_):
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_) # NodeStudent
        valid, day_, month_, year_ = splitDate(date_)
        if valid:
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
            if not data.months.isEmpty() and data.months.searchMonth(month_):
              data = data.months.getMonth(month_) # NodeMonth
              hour_ = splitHour(hour_)
              msg = data.calendar.deleteReminder(hour_, day_, pos_)
            else:
              msg = " >> Error: No hay tarea registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
          else:
            msg = " >> Error: No hay tareas registradas para {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
        else:
          msg = " >> Error: La fecha {} no tiene el formato correcto".format(date_)
      else:  
        msg = " >> Error: El carnet no existe"
    else:
      msg = " >> Error: Verifique sus datos"

    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD CURSOS                                                          ---
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/cursosEstudiante", methods=["POST"])  ########################################
def courseInsert():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["Carnet"]
    name_ = data["Nombre"]
    desc_ = data["Descripcion"]
    course_ = data["Materia"]
    date_ = data["Fecha"]
    hour_ = data["Hora"]
    status_ = data["Estado"]
    #Validation of type -----------------------------------------------
    #     ----- NOT IMPLEMENTED -----------
    #     ----- NOT IMPLEMENTED -----------
    return jsonify({ "response" : "I'm will add a task for student with cardnumber:" + cardnumber_ })
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})




if __name__ == "__main__":
  app.run("localhost", port=3000)