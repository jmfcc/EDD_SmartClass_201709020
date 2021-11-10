import os
# import json
from flask import Flask, json, jsonify, request
from flask_cors import CORS
from Student_AVL import StudentAVL
from Courses_Class import Courses_B
from TablaHash import TablaHash
from Graph_Functions import graphDoubleList, graphTreeAVL, graphDMatrix, graphBTree, graphHashTable, graphTreeAVLCourses, graphRedCourses, graphRedPensum
from analyzers.Syntactic import parser
from analyzers.Syntactic import user_list, task_list

from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp

from CryptDecrypt import applyHashing, encryptData, decryptData_s
from CoursesAVL_Class import CoursesAVL

from cryptography.fernet import Fernet

records = StudentAVL()
# pensum = Courses_B()
pensum = CoursesAVL()
notes = TablaHash()


app = Flask(__name__)
g_key = []
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

def readSVGImage(ruta_):
  file = open(ruta_, "r", encoding="utf-8")
  count = 1
  dataFile = ""
  # dataFile = "<svg width=\"700px\" height=\"700px\""
  for line in file:
    if count > 6:
      dataFile += line
    count += 1
  file.close()
  return dataFile

# #####################################################################################################################
# ########                                           NEW ENDPOINTS F-3                                           ########
# #####################################################################################################################

@app.route("/reporthash", methods=["GET"])
def generateHashTable():
  msg = "Generando tabla hash"
  msg, route_img = graphHashTable(notes)
  if route_img:
    msg = readSVGImage(route_img)
  return jsonify({"response": msg})


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

@app.route("/genkey", methods=["GET"])
def generateKey():
  global g_key
  msg = "Generando una key"
  if g_key:
    msg = "Ya existe una key de encriptación generada"
  else:
    g_key.append(Fernet.generate_key())
    msg = "Clave de encriptación generada"
  return jsonify({"response": msg})


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
        global g_key
        data = records.getStudent(cardnumber_)
        # print(decryptData_s(data.password, g_key[0]), "<--->", applyHashing(passw_.encode()))
        if decryptData_s(data.password, g_key[0]) == applyHashing(passw_.encode()):
          print("simon si es")
          msg = {
            "accesTkn": cardnumber_,
            "expiresIn":"4000",
            "rol": "student"
          }
  return jsonify(msg)

@app.route("/notes", methods=["POST"])
def notePost():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    if not isinstance(cardnumber_, int):
      cardnumber_ = int(cardnumber_)
    title_ = data["Titulo"]
    content_ = data["Contenido"]
    msg = "I'm saving a student note" 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_, title_, content_):
      msg = noteInsert(cardnumber_, title_, content_)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def noteInsert(cardnumber_, title_, content_):
  try:
    cardnumber_s = cardnumber_
    if not isinstance(cardnumber_s, str):
      cardnumber_s = str(cardnumber_s)
    if records.searchStudent(cardnumber_s):
      notes.insert_new_note(cardnumber_, title_, content_)
      return "Se ha guardado el apunte"
    else:
      return "Ah ocurrido un error, recargue la pagina e intentelo nuevamente"
  except:
    return "F, algo fallo"

@app.route("/massivenotesbod", methods=["POST"])
def notebody():
  try:
    data = request.get_json(force=True)
    return noteTraversing(data)
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/massivenotespath", methods=["POST"])
def notepath():
  try:
    data = request.get_json(force=True)
    route_ = data["path"]
    data = readJsonFile(route_)
    return noteTraversing(data)
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def noteTraversing(data):
  err = 0
  users_ = data["usuarios"]
  msg = "I'm saving a student note" 
  if isinstance(users_, list):
    for usr in users_:
      cardnumber_ = usr["carnet"]
      print(type(cardnumber_))
      notes_ = usr["apuntes"]
      if isinstance(notes_, list):
        for nts in notes_:
          title_ = nts["Título"]
          content_ = nts["Contenido"]
          if isValid(cardnumber_, title_, content_):
            msg = noteInsert(cardnumber_, title_, content_)
            if msg[:2] != "Se":
              err += 1
  if err == 0:
    msg = "Se han almacenado todos los apuntes"
  else:
    msg = f"Se detectaron ({err}) errores al insertar los apuntes"
  return jsonify({ "response" : msg})

@app.route("/mynotes", methods=["POST"]) #-----------------------------------------------------
def getNotes():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    if not isinstance(cardnumber_, int):
      cardnumber_ = int(cardnumber_)
    msg = "I'm will send a student notes" 
    #Validation of type -----------------------------------------------
    if isValid(cardnumber_):
      try:
        if records.searchStudent(str(cardnumber_)):
          msg = notes.getNotes(cardnumber_)
        else:
          msg = "Ah ocurrido un error, recargue la pagina e intentelo nuevamente"
      except:
        msg = "F, algo fallo"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/courseassing", methods=["POST"])
def assignCourse():
  try:
    data = request.get_json(force=True)
    cardnumber_ = data["carnet"]
    code_ = data["Codigo"]
    print(type(cardnumber_), cardnumber_)
    if not isinstance(cardnumber_, str):
      cardnumber_ = str(cardnumber_)
    course_ = pensum.getCourse(code_)
    msg = "Assign a course"
    if course_ is not None:
      # print("Voy a asignarlos")
      msg, inc = saveDataCourse(cardnumber_, 2021, 2, code_, course_.name, course_.credits, course_.pre_code, course_.required)
      # print("Ya se asignaron")
      if inc == 0:
        msg = getMyGraphCourses(cardnumber_, 2021, 2, code_)
    else:
      msg = "El curso que intentó asignar no existe"
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
        if type_ == "estudiantejson":
          dataload = readJsonFile(path_)
          students_ = dataload['estudiantes']
          # print("llego a estudiantes")
          if isinstance(students_, list):
            err = 0 
            for dstud in students_:
              # print("itera lista estudiantes")
              cardnumber_ = dstud['carnet']
              if not isinstance(cardnumber_, str):
                # print("parsea carnet a string")
                cardnumber_ = str(cardnumber_)
              dpi_ = dstud['DPI']
              if not isinstance(dpi_, str):
                # print("parsea dpi a string")
                dpi_ = str(dpi_)
              name_ = dstud['nombre']
              carrer_ = dstud['carrera']
              email_ = dstud['correo']
              passw_ = dstud['password']
              age_ = dstud['edad']
              # print("Completa de obtener los datos de estudiante")
              msg = saveDataStudent(cardnumber_, dpi_, name_, carrer_, email_, passw_, 0, age_)
              if msg[:9] == " >> Error":
                err += 1
            if err == 0:
              msg = " >> Info: Se han almacenado todos los registros de estudiantes"
            else:
              msg = f" >> Info: Han ocurrido ({err}) registros que no se pudieron almacenar"
        elif type_ == "estudiante":
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
          if "Estudiantes" in kdata and len(kdata)==1:
            msg = traversingJsonStudentCourses(dataload)
          elif "Cursos" in kdata and len(kdata)==1:
            msg = saveDataPensum(dataload)
          else:
            msg = " >> Error: Formato inválido"
        else:
          msg = " >> Error: No se puede reconocer el tipo solicitado"
      else:
        msg = " >> Error: La ruta del archivo es inválida"
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

@app.route("/reporte", methods=["POST"])
def report():
  try:
    # print("entra", request.get_data())
    data = request.get_json(force=True)
    # print(data)
    type_ = data["tipo"]
    #Validation of type -----------------------------------------------
    msg = "Try generate a report"
    if type_ == 0: # AVL STUDENT REPORT
      if data["enc"]:
        # print("entra al reporte enc")
        msg, route_img = graphTreeAVL(records, False, None)
      else:
        # print("entra al reporte desenc")
        msg, route_img = graphTreeAVL(records, True, g_key[0])
      if route_img:
        # print(route_img)
        msg = readSVGImage(route_img)
        # print(msg)
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
    elif type_ == 3: # B-TREE PENSUM(Modify to AVL)
      msg = graphTreeAVLCourses(pensum, "Pensum")
      # if not pensum.isEmpty(pensum.Root):
        # graphBTree(pensum, "Pensum")
      #   msg = " >> Info: Arbol B de pensum generado"
      # else:
      #   msg = " >> Error: No hay registros en pensum"
    elif type_ == 4: # B-TREE COURSES(Modify to AVL)
      cardnumber_ = data["carnet"]
      if not isinstance(cardnumber_, str):
        cardnumber_ = str(cardnumber_)

      # year_ = int(data["año"])
      # semester_ = int(data["semestre"])
      year_ = 2021
      semester_ = 2
      msg = getMyGraphCourses(cardnumber_, year_, semester_, "")
    elif type_ == 5: # Red Curso (Prerrequisito)
      code_ = data["codigo"]
      msg, route_img = graphRedCourses(pensum, code_)  
      if route_img:
        msg = readSVGImage(route_img) 
    elif type_ == 6: # Red Pensum (Prerrequisito)
      msg, route_img = graphRedPensum(pensum)  
      if route_img:
        msg = readSVGImage(route_img) 
    return jsonify({ "response" : msg })
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def getMyGraphCourses(cardnumber_, year_, semester_, code_):
  msg = ""
  if isValid(cardnumber_, year_, semester_):
    # print("datos validos")
    if records.searchStudent(cardnumber_):
      data = records.getStudent(cardnumber_) # NodeStudent
      # print("se obtuvo al estudiante")
      if not data.years.isEmpty() and data.years.searchYear(year_):
        data = data.years.getYear(year_) # NodeYear
        # print("se obtuvo el año")
        if not data.semesters.isEmpty() and data.semesters.searchSemester(semester_):
          data = data.semesters.getSemester(semester_) # NodeSemester
          # print("se obtuvo el semestre")
          # graphBTree(data.courses, "StudentCourses")
          msg, route_img = graphTreeAVLCourses(data.courses, "Estudiante", code_)
          if route_img:
            msg = readSVGImage(route_img) 
        else:
          msg = f" >> Info: No hay registros del semestre ({semester_}) del año {year_}"
      else:
        msg = f" >> Info: No hay registros del año {year_}"
    else:
      msg = " >> Info: No hay registros del carnet solicitado"
  else:
    msg = " >> Info: Verifique sus datos"
  return msg

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
  global g_key
  # print("save data function")
  if isValid(cardnumber_, dpi_, name_, carrer_, email_, passw_, credits_, age_):
    if records.searchStudent(cardnumber_):
      return " >> Error: El carnet {} ya está registrado".format(cardnumber_)
    else:
      # print("all ok")
      # print("va a pasar el encriptado de password")
      # print("pasa el encriptado de password")
      dpi_ = encryptData(dpi_.encode(),g_key[0])
      name_ = encryptData(name_.encode(),g_key[0])
      email_ = encryptData(email_.encode(),g_key[0])
      passw_ = encryptData(applyHashing(passw_.encode()).encode(),g_key[0])
      # print("a parsear la edad")
      age_ = encryptData(str(age_).encode(),g_key[0])
      # print("ya parseo la edad")
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
    msg = traversingJsonStudentCourses(data)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def traversingJsonStudentCourses(data_):
  studentsList = data_["Estudiantes"]
  msg = "Insertando cursos de estudiantes"
  countErr = 0
  if isinstance(studentsList, list):
    # print("si es lista de estudiantes")
    for studData in studentsList:
      cardnumber_ = studData["Carnet"]
      years_ = studData["Años"]
      if isinstance(years_, list):
        # print("si es lista de años", cardnumber_)
        for yearData in years_:
          year_ = int(yearData["Año"])
          semesters_ = yearData["Semestres"]
          if isinstance(semesters_, list):
            # print("si es lista de semestres", year_)
            for semestData in semesters_:
              semester_ = int(semestData["Semestre"])
              if semester_ < 3 and semester_ > 0:
                courses_ = semestData["Cursos"]
                if isinstance(courses_, list):
                  # print("si es lista de cursos")
                  for courseData in courses_:
                    code_ = courseData["Codigo"]
                    name_ = courseData["Nombre"]
                    credits_ = courseData["Creditos"]
                    pre_code_ = courseData["Prerequisitos"]
                    require_ = courseData["Obligatorio"]
                    msg, inc = saveDataCourse(cardnumber_, year_, semester_, code_, name_, credits_, pre_code_, require_)
                    countErr += inc
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
  else:
    msg = " >> Info: Se han almacenado los cursos (estudiantes)"
  return msg
 
def saveDataCourse(cardnumber_, year_, semester_, code_, name_, credits_, pre_code_, require_):
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
        return " >> Error: Acceso invalido a lista años", 1
      try:
        if not data.semesters.isEmpty() and data.semesters.searchSemester(semester_):
          data = data.semesters.getSemester(semester_) # NodeSemester
        else:
          data.semesters.insertSemester(semester_)
          data = data.semesters.getSemester(semester_) # NodeSemester
      except:
        # print("Tronó en la lista semestres")
        return " >> Error: Acceso invalido a lista años", 1
      try:
        if data.courses.searchCourse(code_):
          return " >> Info: El curso ya está asginado", 0
        else:
          data.courses.insertData(code_, name_, credits_, pre_code_, require_)#--------------------------------------
          return " >> Info: Curso asignado exitosamente", 0
      except:
        return " >> Error: Inserción Fallida", 1
    else:  
      return " >> Error: El carnet no existe", 1
  else:
    return " >> Error: Verifique sus datos", 1

@app.route("/cursosPensum", methods=["POST"])
def coursePensumInsert():
  try:
    data = request.get_json(force=True)
    msg = saveDataPensum(data)
    return jsonify({ "response" : msg})
  except:
    return jsonify({ "response" : "Something goes wrong, verify your data"})

def saveDataPensum(data_):
  courses_ = data_["Cursos"]
  msg = "Insertando curso pensum"
  allOk = 0
  if isinstance(courses_, list):
    for courseData in courses_:
      code_ = courseData["Codigo"]
      name_ = courseData["Nombre"]
      credits_ = courseData["Creditos"]
      pre_code_ = courseData["Prerequisitos"]
      require_ = courseData["Obligatorio"]
      if isValid(code_, name_, credits_, require_):
        pensum.insertData(code_, name_, credits_, pre_code_, require_)
      else:
        allOk += 1
    if allOk == 0:
      msg = " >> Info: La carga de cursos (pensum) ha sido completada"
    else:
      msg = " >> Error: Se registraron {} errores".format(str(allOk))
  else:
    msg = " >> Error: Se esperaba una lista de estudiantes"

  return msg

if __name__ == "__main__":
  app.run("localhost", port=3000)