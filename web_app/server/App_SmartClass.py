import os
# import json
from flask import Flask, json, jsonify, request
from flask_cors import CORS
from Student_AVL import StudentAVL
from Courses_Class import Courses_B
from TablaHash import TablaHash
from Graph_Functions import graphDoubleList, graphTreeAVL, graphDMatrix, graphBTree, graphHashTable, graphTreeAVLCourses, graphRedCourses
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from CryptDecrypt import applyHashing, encryptData, decryptData
from CoursesAVL_Class import CoursesAVL


records = StudentAVL()
# pensum = Courses_B()
pensum = CoursesAVL()
notes = TablaHash()


app = Flask(__name__)
CORS(app)

# #####################################################################################################################
# ########                                               HELPERS                                               ########
# #####################################################################################################################

def isValid(*args):
  for val in args:
    # print(type(val))
    if isinstance(val, int):
      if val < 0:
        return False
    elif not val:
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

def validatePath(ruta_):
  if ruta_:
    if os.path.isfile(ruta_):
        return True
  return False

def uploadStudentFile(ruta_):
  f = open(ruta_,"r", encoding="utf-8")
  mensaje = f.read()
  f.close()

  parser.parse(mensaje)

def readJsonFile(ruta_):
  file = open(ruta_, "r", encoding="utf8")
  dataFile = json.load(file)
  # print(type(dataFile))
  return dataFile



# #####################################################################################################################
# ########                                        AUTHENTICATION JWT                                           ########
# #####################################################################################################################

class User(object):
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz'),
]

username_table = {u.username: u for u in users}
userid_table = {u.id: u for u in users}

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and safe_str_cmp(user.password.encode('utf-8'), password.encode('utf-8')):
        return user

def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)

app.config['SECRET_KEY'] = 'super-secret'

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return '%s' % current_identity

# #####################################################################################################################
# ########                                           ENDPOINTS-F3                                              ########
# #####################################################################################################################

@app.route("/login", methods=["POST"])
def login():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  passw_ = data["password"]
  
  msg = {
    "accesTkn":"",
    "expiresIn":"",
    "rol":"none"
  }
  if isValid(cardnumber_, passw_):
    if cardnumber_=="admin" and  passw_=="admin":
      msg = {
        "accesTkn":"adminaccess",
        "expiresIn":"5000",
        "rol": "admin"
      }
    else:
      if records.searchStudent(cardnumber_):
        data = records.getStudent(cardnumber_)
        if decryptData(data.password) == applyHashing(passw_.encode()):
          msg = {
            "accesTkn":"studaccess",
            "expiresIn":"4000",
            "rol": "student"
          }
  return jsonify(msg)

@app.route("/notes", methods=["POST"])
def notePost():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    title_ = data["title"]
    content_ = data["content"]
    msg = "I'm saving a student note" 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, title_, content_):
      msg = noteInsert(cardnumber_, title_, content_)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def noteInsert(cardnumber_, title_, content_):
  try:
    if records.searchStudent(cardnumber_):
      notes.insert_new_note(cardnumber_, title_, content_)
      return "Se ha guardado el apunte"
    else:
      return "Ah ocurrido un error, recargue la pagina e intentelo nuevamente"
  except:
    return "F, algo fallo"

@app.route("/notes", methods=["GET"]) #-----------------------------------------
def getNotes():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    title_ = data["title"]
    content_ = data["content"]
    msg = "I'm saving a student note" 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, title_, content_):
      try:
        if records.searchStudent(cardnumber_):
          notes.insert_new_note(cardnumber_, title_, content_)
          msg = "Se ha guardado el apunte"
        else:
          msg = "Ah ocurrido un error, recargue la pagina e intentelo nuevamente"
      except:
        msg = "F, algo fallo"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})




# #####################################################################################################################
# ########                                              ENDPOINTS                                              ########
# #####################################################################################################################

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/carga", methods=["POST"]) 
def loadFile():
  try:
    data = request.get_json(force=True)
    type_ = data["tipo"]
    path_ = data["path"]
    msg = "Cargando un archivo"
    #Load -----------------------------------------------
    if isValid(type_, path_):
      if validatePath(path_):
        if type_ == "estudiante":
          uploadStudentFile(path_)
          aux = user_list.First
          countUerr = 0
          print("ya pasa el ply")
          while aux is not None:
            m = saveDataStudent(aux.Carnet, aux.DPI, aux.Nombre, aux.Carrera, aux.Correo, aux.Password, aux.Creditos, aux.Edad)
            if "Error:" in m:
              print(m)
              countUerr += 1
            aux = aux.Next
          aux2 = task_list.First
          countTerr = 0
          print("pasa el registro de estudiantes")
          while aux2 is not None:
            # print("--------------------------------------------------")
            # print("->",type(aux2.Carnet), "\n->", type(aux2.Nombre), "\n->", type(aux2.Descripcion), "\n->", type(aux2.Materia), "\n->", type(aux2.Fecha), "\n->", type(aux2.Hora), "\n->", type(aux2.Estado))
            m = saveDataTask(aux2.Carnet, aux2.Nombre, aux2.Descripcion, aux2.Materia, aux2.Fecha, aux2.Hora, aux2.Estado)
            if "Error:" in m:
              print(m)
              countTerr += 1
            aux2 = aux2.Next
          if countTerr == 0 and countUerr == 0:
            msg = " >> Info: Se han almacenado todos los registros de estudiantes y sus tareas"
          else:
            msg = " >> Info: Se han detectado ({}) errores de estudiantes y ({}) errores de tareas".format(str(countUerr), str(countTerr))
          user_list.clear()
          task_list.clear()
        elif type_ == "recordatorio":
          pass
        elif type_ == "curso":
          dataload = readJsonFile(path_)
          kdata = dataload.keys()
          if "estudiantes" in kdata and len(kdata)==1:
            msg = saveDataCourse(dataload)
          elif "cursos" in kdata and len(kdata)==1:
            msg = saveDataPensum(dataload)
          else:
            msg = " >> Error: Formato inválido"
        else:
          msg = " >> Error: No se puede reconocer el tipo solicitado"
      else:
        msg = " >> Error: Ruta inválida"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/reporte", methods=["GET"])
def report():
  try:
    data = request.get_json(force=True)
    type_ = data["tipo"]
    #Validation of type -----------------------------------------------
    msg = "Try generate a report"
    if type_ == 0: # AVL REPORT
      graphTreeAVL(records, False)
      graphTreeAVL(records, True)
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
      msg = graphTreeAVLCourses(pensum, "Pensum")
      # if not pensum.isEmpty(pensum.Root):
        # graphBTree(pensum, "Pensum")
      #   msg = " >> Info: Arbol B de pensum generado"
      # else:
      #   msg = " >> Error: No hay registros en pensum"
    elif type_ == 4: # B-TREE COURSES
      cardnumber_ = data["carnet"]
      year_ = int(data["año"])
      semester_ = int(data["semestre"])
      if isValid(cardnumber_, year_, semester_):
        if records.searchStudent(cardnumber_):
          data = records.getStudent(cardnumber_) # NodeStudent
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
            if not data.semesters.isEmpty() and data.semesters.searchSemester(semester_):
              data = data.semesters.getSemester(semester_) # NodeSemester
              # graphBTree(data.courses, "StudentCourses")
              graphTreeAVLCourses(data.courses, "StudentCourses")
              msg = " >> Info: El arbol de cursos ha sido generado"
            else:
              msg = " >> Error: No hay registros del semestre solicitado"
          else:
            msg = " >> Error: No hay registros del año solicitado"
        else:
          msg = " >> Error: No hay registros del carnet solicitado"
      else:
        msg = " >> Error: Verifique sus datos"
    elif type_ == 5:
      code_ = data["codigo"]
      msg = graphRedCourses(pensum, code_)
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
    msg = saveDataStudent(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def saveDataStudent(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_):
  if isValid(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_):
    if records.searchStudent(cardnumber_):
      return " >> Error: El carnet {} ya está registrado".format(cardnumber_)
    else:
      # print("va a pasar el encriptado de password")
      # print("pasa el encriptado de password")
      dpi_ = encryptData(dpi_.encode())
      name_ = encryptData(name_.encode())
      email_ = encryptData(email_.encode())
      passw_ = encryptData(applyHashing(passw_.encode()))
      age_ = encryptData(str(age_).encode())
      records.insert(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_)
      # notes.add_to_table(int(cardnumber_))
      return " >> Info: Datos del estudiante almacenados correctamente" 
  else:
    print("\n--",cardnumber_,"\n--", dpi_,"\n--", name_,"\n--", carrer_,"\n--", email_,"\n--", passw_,"\n--", credits_,"\n--", age_)
    return " >> Error: Verifique sus datos"

@app.route("/estudiante", methods=["PUT"])
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

@app.route("/estudiante", methods=["DELETE"]) 
def studentDelete():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    msg = "Eliminando a un estudiante"
    if isValid(cardnumber_):
      if records.searchStudent(cardnumber_):
        records.delete(cardnumber_)
      else:
        msg = " >> Error: El estudiante no existe"
    else:
      msg = " >> Error: Verifique sus datos"
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
    msg = saveDataTask(cardnumber_, name_, desc_, course_, date_, hour_, status_)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def saveDataTask(cardnumber_, name_, desc_, course_, date_, hour_, status_):
  if isValid(cardnumber_, name_, desc_, course_, date_, hour_, status_):
    if records.searchStudent(cardnumber_):
      data = records.getStudent(cardnumber_) # NodeStudent
      valid, day_, month_, year_ = splitDate(date_)
      # print(day_, month_, year_)
      if valid:
        try:
          if not data.years.isEmpty() and data.years.searchYear(year_):
            data = data.years.getYear(year_) # NodeYear
          else:
            data.years.insertYear(year_)
            data = data.years.getYear(year_) # NodeYear
        except:
          print("En la lista años")
          return " >> Error: Acceso invalido a lista años"
        try:
          if data.months.searchMonth(month_):
            data = data.months.getMonth(month_) # NodeMonth
          else:
            data.months.insertMonth(month_)
            data = data.months.getMonth(month_) # NodeMonth
        except:
          print("En la lista meses")
          return " >> Error: Acceso invalido a meses"
        try:
          hour_ = splitHour(hour_)
          data.calendar.insertNewTask(hour_, day_, name_, desc_, course_, status_)
          return " >> Info: Tarea almacenada {}/{}/{}  {}:00".format(str(day_), str(month_), str(year_), str(hour_))
        except:
          print("En el calendario")
          return " >> Error: Acceso invalido a meses"
      else:
        return " >> Error: La fecha {} no tiene el formato correcto".format(date_)
    else:  
      return " >> Error: El carnet no existe {}".format(str(cardnumber_))
  else:
    return " >> Error: Verifique sus datos"

@app.route("/recordatorios", methods=["PUT"])
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
@app.route("/cursosEstudiante", methods=["POST"])
def courseStudentInsert():
  try:
    data = request.get_json(force=True)
    msg = saveDataCourse(data)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def saveDataCourse(data_):
  studentsList = data_["estudiantes"]
  msg = "Insertando cursos de estudiantes"
  countErr = 0
  if isinstance(studentsList, list):
    # print("si es lista de estudiantes")
    for studData in studentsList:
      cardnumber_ = studData["carnet"]
      years_ = studData["años"]
      if isinstance(years_, list):
        # print("si es lista de años", cardnumber_)
        for yearData in years_:
          year_ = int(yearData["año"])
          semesters_ = yearData["semestres"]
          if isinstance(semesters_, list):
            # print("si es lista de semestres", year_)
            for semestData in semesters_:
              semester_ = int(semestData["semestre"])
              if semester_ < 3 and semester_ > 0:
                courses_ = semestData["cursos"]
                if isinstance(courses_, list):
                  # print("si es lista de cursos")
                  for courseData in courses_:
                    code_ = courseData["codigo"]
                    name_ = courseData["nombre"]
                    credits_ = courseData["creditos"]
                    pre_code_ = courseData["prerequisitos"]
                    require_ = courseData["obligatorio"]
                    if isValid(cardnumber_, year_, semester_, code_, name_, credits_, require_):
                      if records.searchStudent(cardnumber_):
                        data = records.getStudent(cardnumber_) # NodeStudent
                        try:
                          if not data.years.isEmpty() and data.years.searchYear(year_):
                            data = data.years.getYear(year_) # NodeYear
                          else:
                            data.years.insertYear(year_)
                            data = data.years.getYear(year_) # NodeYear
                        except:
                          # print("Tronó en la lista años")
                          msg = " >> Error: Acceso invalido a lista años"
                        try:
                          if not data.semesters.isEmpty() and data.semesters.searchSemester(semester_):
                            data = data.semesters.getSemester(semester_) # NodeSemester
                          else:
                            data.semesters.insertSemester(semester_)
                            data = data.semesters.getSemester(semester_) # NodeSemester
                        except:
                          # print("Tronó en la lista semestres")
                          msg = " >> Error: Acceso invalido a lista años"
                        try:
                          data.courses.insertData(code_, name_, credits_, pre_code_, require_)
                          # print("Se inserto ---------------------")
                          msg = " >> Info: Datos almacenados"
                        except:
                          msg = " >> Error: Inserción Fallida"
                          countErr += 1
                      else:  
                        msg = " >> Error: El carnet no existe"
                        countErr += 1
                    else:
                      msg = " >> Error: Verifique sus datos"
                      countErr += 1
                else:
                  msg = " >> Error: Se esperaba una lista de cursos"
                  countErr += 1
              else:
                msg = " >> Error: El semestre está fuera de rango"
                countErr += 1
          else:
            msg = " >> Error: Se esperaba una lista de semestres"
            countErr += 1
      else:
        msg = " >> Error: Se esperaba una lista de años"
        countErr += 1
  else:
    msg = " >> Error: Se esperaba una lista de estudiantes"
    countErr += 1
  if countErr != 0:
    return " >> Error: Se registraron {} errores".format(str(countErr))
  return msg

@app.route("/cursosPensum", methods=["POST"])
def coursePensumInsert():
  try:
    data = request.get_json(force=True)
    msg = saveDataPensum(data)
    
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def saveDataPensum(data_):
  courses_ = data_["cursos"]
  msg = "Insertando curso pensum"
  allOk = 0
  if isinstance(courses_, list):
    for courseData in courses_:
      code_ = courseData["codigo"]
      name_ = courseData["nombre"]
      credits_ = courseData["creditos"]
      pre_code_ = courseData["prerequisitos"]
      require_ = courseData["obligatorio"]
      if isValid(code_, name_, credits_, require_):
        pensum.insertData(code_, name_, credits_, pre_code_, require_)
      else:
        allOk += 1
    if allOk == 0:
      msg = " >> Info: La carga de cursos ha sido completada"
    else:
      msg = " >> Error: Se registraron {} errores".format(str(allOk))
  else:
    msg = " >> Error: Se esperaba una lista de estudiantes"

  return msg

if __name__ == "__main__":
  app.run("localhost", port=3000)