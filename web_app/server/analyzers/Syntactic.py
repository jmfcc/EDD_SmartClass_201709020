
from analyzers.Lex import tokens
from Structures.List import List
from Structures.Node import Node

# Lists for save the information about users and tasks
user_list = List()
task_list = List()

# This node allows to store information about one user or task
element_node = Node()

# dictionary of names
names = {}

def p_statement_group(t):
    'statement : LQUESTION TELEMENTS RQUESTION elementos LQUESTION DOLAR TELEMENTS RQUESTION'
    print('Ok')

def p_elementos_group(t):
    """elementos : elementos elemento
                 | elemento
    """
    # t[0] = t[1]
    # if len(t) == 2:
    #     t[0] = [t[1]]
    # else:
    #     t[0] = t[1]
    #     t[0].append(t[2])

def p_elemento(t):
    'elemento : LQUESTION TELEMENT  tipoElemento RQUESTION items LQUESTION DOLAR TELEMENT RQUESTION'

    if t[3] == "user":
        user_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              int(element_node.Creditos), int(element_node.Edad), element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado)
    else:
        task_list.insertValue(element_node.Carnet, element_node.DPI, element_node.Nombre, element_node.Carrera, element_node.Password,
                              element_node.Creditos, element_node.Edad, element_node.Correo, element_node.Descripcion, element_node.Materia,
                              element_node.Fecha, element_node.Hora, element_node.Estado)
    element_node.clean_values()

def p_tipoElemento(t):
    """tipoElemento : TTYPE EQUALS NORMSTRING
    """
    t[0] = t[3].replace('"', '').replace(' ', '')


def p_items(t):
    """items : items item
    """
    t[0] = t[2]

def p_items_2(t):
    """items : item
    """
    t[0] = t[1]

def p_item(t):
    """item : LQUESTION TITEM tipeItem EQUALS valueItem DOLAR RQUESTION
    """
    if t[3].lower() == "carnet":
        element_node.Carnet = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "dpi":
        element_node.DPI = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "nombre":
        element_node.Nombre = t[5].replace('"', '')
    elif t[3].lower() == "carrera":
        element_node.Carrera = t[5].replace('"', '')
    elif t[3].lower() == "password":
        element_node.Password = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "creditos":
        element_node.Creditos = t[5].replace('"', '')
    elif t[3].lower() == "edad":
        element_node.Edad = t[5].replace('"', '')
    elif t[3].lower() == "correo":
        element_node.Correo = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "descripcion":
        element_node.Descripcion = t[5].replace('"', '')
    elif t[3].lower() == "materia":
        element_node.Materia = t[5].replace('"', '')
    elif t[3].lower() == "fecha":
        element_node.Fecha = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "hora":
        element_node.Hora = t[5].replace('"', '').replace(' ', '')
    elif t[3].lower() == "estado":
        element_node.Estado = t[5].replace('"', '').replace(' ', '')

    t[0] = element_node

def p_valueItem(t):
    """valueItem : NORMSTRING
                 | NUMBER
                 """
    t[0] = t[1]

def p_tipeItem(t):
    """tipeItem : TCARNET
                | TDPI
                | TNOMBRE
                | TCARRERA
                | TPASSWORD
                | TCREDITOS
                | TEDAD
                | TDESCRIPCION
                | TMATERIA
                | TFECHA
                | THORA
                | TESTADO
                | TCORREO
                """
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc()