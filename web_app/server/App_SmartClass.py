from flask import Flask, json, jsonify, request, Response
from flask_cors import CORS
from Student_AVL import StudentAVL

records = StudentAVL()

app = Flask(__name__)
CORS(app)

@app.route("/")
def helloWorld():
  return "Hello, cross-origin-world!"

@app.route("/carga", methods=["POST"])
def loadFile():
  data = request.get_json(force=True)
  type_ = data["tipo"]
  path_ = data["path"]
  #Load -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm loading:" + path_ })

@app.route("/reporte", methods=["GET"])
def report():
  data = request.get_json(force=True)
  type_ = data["tipo"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm generate a report type:" + type_ })

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD ESTUDIANTES                                                     ---
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/estudiante", methods=["POST"])
def studentInsert():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  dpi_ = data["DPI"]
  name_ = data["nombre"]
  carrer_ = data["carrera"]
  email_ = data["correo"]
  passw_ = data["password"]
  credits_ = data["creditos"]
  age_ = data["edad"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm saving a student with cardnumber:" + cardnumber_ })

@app.route("/estudiante", methods=["UPDATE"])
def studentUpdate():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  dpi_ = data["DPI"]
  name_ = data["nombre"]
  carrer_ = data["carrera"]
  email_ = data["correo"]
  passw_ = data["password"]
  credits_ = data["creditos"]
  age_ = data["edad"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm updating a student with cardnumber:" + cardnumber_ })

@app.route("/estudiante", methods=["DELETE"])
def studentDelete():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm deleting a student with cardnumber:" + cardnumber_ })

@app.route("/estudiante", methods=["GET"])
def studentSelect():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm will return the record of student with cardnumber:" + cardnumber_ })

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD RECORDATORIOS                                                   ---
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/recordatorios", methods=["POST"])
def taskInsert():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  name_ = data["nombre"]
  desc_ = data["descripcion"]
  course_ = data["materia"]
  date_ = data["fecha"]
  hour_ = data["hora"]
  status_ = data["estado"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm will add a task for student with cardnumber:" + cardnumber_ })

@app.route("/recordatorios", methods=["UPDATE"])
def taskUpdate():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  name_ = data["nombre"]
  desc_ = data["descripcion"]
  course_ = data["materia"]
  date_ = data["fecha"]
  hour_ = data["hora"]
  status_ = data["estado"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm will update a task for student with cardnumber:" + cardnumber_ })

@app.route("/recordatorios", methods=["GET"])
def taskSelect():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  date_ = data["fecha"]
  hour_ = data["hora"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm will select a task for student with cardnumber:" + cardnumber_ })

@app.route("/recordatorios", methods=["DELETE"])
def taskDelete():
  data = request.get_json(force=True)
  cardnumber_ = data["carnet"]
  date_ = data["fecha"]
  hour_ = data["hora"]
  #Validation of type -----------------------------------------------
  #     ----- NOT IMPLEMENTED -----------
  #     ----- NOT IMPLEMENTED -----------
  return jsonify({ "response" : "I'm will delete a task for student with cardnumber:" + cardnumber_ })

# ---------------------------------------------------------------------------------------------------------------------
# ---                                          CRUD CURSOS                                                          ---    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ---------------------------------------------------------------------------------------------------------------------
@app.route("/cursosEstudiante", methods=["POST"])
def courseInsert():
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




if __name__ == "__main__":
  app.run("localhost", port=3000)