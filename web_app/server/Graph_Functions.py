import os
from CryptDecrypt import decryptData, decryptData_s

def getRoute():
    # ruta = os.path.dirname(os.path.abspath(__file__)) # Para la ruta del script en ejecución
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    directory = "Reportes_F3"
    fullDir = os.path.join(desktop,directory)
    if not os.path.isdir(fullDir):
        os.mkdir(fullDir)
    return fullDir

# -------------------------------------------------------------
# --------             GRAFICAR ARBOL AVL             ---------
# -------------------------------------------------------------


def graphTreeAVL(root_, viewdecript):
    print("Funcion graficar arbol")
    
    content = ["digraph G{\n\tnode [shape=box];\n", ""]

    if root_.Root != None:
        if viewdecript:
            traversingTreeAVLDecrypt(root_.Root, content)
        else:
            traversingTreeAVL(root_.Root, content)
    else:
        print("El arbol está vacío")
        return

    content[0] += content[1] + "\n}"

    name = "encrypt"
    if viewdecript:
        name = "decrypt"

    print(getRoute())
    f = open(os.path.join(getRoute(),f'grafoAVL{name}.dot'), 'w', encoding="utf-8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + f"\\grafoAVL{name}.dot -o "+getRoute()+ f"\\grafoAVL{name}.svg"
    os.system(prog)
    
    print("El arbol avl fue generado")

def traversingTreeAVL(root_,content):
    # print("Recorriendo")
    if root_ is not None:
        cardnumb = root_.cardnumber
        dpi = root_.dpi
        dpi = dpi[:8] + b"  ...  " + dpi[-8:]
        name = root_.name
        name = name[:8] + b"  ...  " + name[-8:]
        carrer = root_.carrer
        email = root_.email
        email = email[:8] + b"  ...  " + email[-8:]
        password = root_.password
        password = password[:8] + b"  ...  " + password[-8:]
        credits = root_.credits
        age = root_.age
        age = age[:8] + b"  ...  " + age[-8:]
        content[1] += f'\t"{str(hash(root_))}"[label="Carnet: {cardnumb}\\nDPI: {dpi}\\nNombre: {name}\\nCarrera: {carrer}\\nEmail: {email}\\nPassword: {password}\\nCreditos: {credits}\\nEdad: {age}"];\n'

        if root_.left is not None:
            content[1] += '\t"{}" -> "{}"[color=green, label=L];\n'.format(str(hash(root_)),str(hash(root_.left)))
        else:
            content[1] += '\t"{}" -> "nonL{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonL{}"[style=invis];\n'.format(str(hash(root_)))
        if root_.right is not None:
            content[1] += '\t"{}" -> "{}"[color=red, label=R];\n'.format(str(hash(root_)), str(hash(root_.right)))
        else:
            content[1] += '\t"{}" -> "nonR{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonR{}"[style=invis];\n'.format(str(hash(root_)))

        traversingTreeAVL(root_.left, content)
        traversingTreeAVL(root_.right, content)

def traversingTreeAVLDecrypt(root_,content):
    # print("Recorriendo")
    if root_ is not None:
        cardnumb = root_.cardnumber
        dpi = root_.dpi
        name = root_.name
        carrer = root_.carrer
        email = root_.email
        password = root_.password
        credits = root_.credits
        age = root_.age
        print("decrypt")
        dpi = decryptData_s(dpi)
        name = decryptData_s(name)
        email = decryptData_s(email)
        password = decryptData(password)
        # print("en el slice")
        password = password[:12]
        age = decryptData_s(age)
        content[1] += f'\t"{str(hash(root_))}"[label="Carnet: {cardnumb}\\nDPI: {dpi}\\nNombre: {name}\\nCarrera: {carrer}\\nEmail: {email}\\nPassword: {password}\\nCreditos: {credits}\\nEdad: {age}"];\n'

        if root_.left is not None:
            content[1] += '\t"{}" -> "{}"[color=green, label=L];\n'.format(str(hash(root_)),str(hash(root_.left)))
        else:
            content[1] += '\t"{}" -> "nonL{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonL{}"[style=invis];\n'.format(str(hash(root_)))
        if root_.right is not None:
            content[1] += '\t"{}" -> "{}"[color=red, label=R];\n'.format(str(hash(root_)), str(hash(root_.right)))
        else:
            content[1] += '\t"{}" -> "nonR{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonR{}"[style=invis];\n'.format(str(hash(root_)))

        traversingTreeAVLDecrypt(root_.left, content)
        traversingTreeAVLDecrypt(root_.right, content)


# -------------------------------------------------------------
# --------     ***GRAFICAR ARBOL AVL (Cursos)***      ---------
# -------------------------------------------------------------

def graphTreeAVLCourses(root_, name):
    print("Funcion graficar arbol")
    
    content = ["digraph G{\n\tnode [shape=box];\n", ""]

    if root_.Root != None:
        traversingTreeAVLC(root_.Root, content)
    else:
        return "El arbol está vacío"

    content[0] += content[1] + "\n}"

    name = "Cursos"+name

    print(getRoute())
    f = open(os.path.join(getRoute(),f'grafoAVL{name}.dot'), 'w', encoding="utf-8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + f"\\grafoAVL{name}.dot -o "+getRoute()+ f"\\grafoAVL{name}.svg"
    os.system(prog)
    
    print("El arbol avl fue generado")
    return "El arbol avl fue generado"

def traversingTreeAVLC(root_,content):
    # print("Recorriendo")
    if root_ is not None:
        code = root_.code
        name = root_.name
        credits = root_.credits
        pre_code = root_.pre_code
        if pre_code == "":
            pre_code = "----"
        required = "Si" if root_.required else "No"
        content[1] += f'\t"{str(hash(root_))}"[label="Codigo: {code}\\nNombre: {name}\\nCreditos: {credits}\\nPrerrequisitos: {pre_code}\\nObligatorio: {required}"];\n'

        if root_.left is not None:
            content[1] += '\t"{}" -> "{}"[color=green, label=L];\n'.format(str(hash(root_)),str(hash(root_.left)))
        else:
            content[1] += '\t"{}" -> "nonL{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonL{}"[style=invis];\n'.format(str(hash(root_)))
        if root_.right is not None:
            content[1] += '\t"{}" -> "{}"[color=red, label=R];\n'.format(str(hash(root_)), str(hash(root_.right)))
        else:
            content[1] += '\t"{}" -> "nonR{}"[style=invis];\n'.format(str(hash(root_)),str(hash(root_)))
            content[1] += '\t"nonR{}"[style=invis];\n'.format(str(hash(root_)))

        traversingTreeAVLC(root_.left, content)
        traversingTreeAVLC(root_.right, content)

# -------------------------------------------------------------
# --------              GRAFICAR ARBOL B              ---------
# -------------------------------------------------------------

def graphBTree(btree, name_):
    graphic = ["digraph ArbolB{\n", "", ""]
    graphic[0] += "\n\trankdir=TB;\n"
    graphic[0] += '\tnode[color="orange", fillcolor=lightgray, shape=record];\n'
    graphic[0] += '\tgraph[splines=compound];\n'

    traversingBTreeNodes(btree.root, graphic)
    traversingBTreeEdges(btree.root, graphic)

    graphic[0] += graphic[1] + graphic[2] +"\n}\n"

    f = open(getRoute()+'\\grafoBTree_{}.dot'.format(name_), 'w', encoding="utf8")
    # f = open('grafoB.dot', 'w', encoding="utf8")
    try:
        f.write(graphic[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "\\grafoBTree_"+name_+".dot -o "+getRoute()+"\\grafoBTree_"+name_+".svg"
    # prog = "dot -Tsvg grafoB.dot -o grafoB.svg"
    os.system(prog)
    
    print("El arbol b fue generado")

def traversingBTreeNodes(page_, graphic):
    nodes_ = 0
    count = 0
    if page_ != None:
        nodes_ = 0
        for i in range(page_.getCount()):
            if page_.getCode(i) != None:
                nodes_ += 1
                if i != 0:
                    graphic[1] += "|"
                if nodes_ == 1:
                    graphic[1] += '\n\tn{}[label="<f0> |'.format(str(page_.getCode(i)))
                if i == 0:
                    graphic[1] += '<f{}>{}\\n{}|<f{}>'.format(str(i+1),str(page_.getCode(i)),page_.getName(i),str(i+2))
                    count = 3
                else:
                    graphic[1] += '<f{}>{}\\n{}|<f{}>'.format(str(count),str(page_.getCode(i)),page_.getName(i),str(count+1))
                    count+=2
                
                if i == page_.getCount()-1:
                    count = 0
                    graphic[1] += '", group=0];\n'
        traversingBTreeNodes(page_.getPointer(0), graphic)
        traversingBTreeNodes(page_.getPointer(1), graphic)
        traversingBTreeNodes(page_.getPointer(2), graphic)
        traversingBTreeNodes(page_.getPointer(3), graphic)
        traversingBTreeNodes(page_.getPointer(4), graphic)

def traversingBTreeEdges(page_, graphic):
    if page_ != None:
        if page_.getCode(0) != None:
            # if page_.getCode(0) != "":
            if page_.getPointer(0) != None and page_.getPointer(0).getCode(0) != None:
                graphic[2] += '\n\tn{}:f0-> n{}'.format(str(page_.getCode(0)),str(page_.getPointer(0).getCode(0)))
            if page_.getPointer(1) != None and page_.getPointer(1).getCode(0) != None:
                graphic[2] += '\n\tn{}:f2-> n{}'.format(str(page_.getCode(0)),str(page_.getPointer(1).getCode(0)))
            if page_.getPointer(2) != None and page_.getPointer(2).getCode(0) != None:
                graphic[2] += '\n\tn{}:f4-> n{}'.format(str(page_.getCode(0)),str(page_.getPointer(2).getCode(0)))
            if page_.getPointer(3) != None and page_.getPointer(3).getCode(0) != None:
                graphic[2] += '\n\tn{}:f6-> n{}'.format(str(page_.getCode(0)),str(page_.getPointer(3).getCode(0)))
            if page_.getPointer(4) != None and page_.getPointer(4).getCode(0) != None:
                graphic[2] += '\n\tn{}:f8-> n{}'.format(str(page_.getCode(0)),str(page_.getPointer(4).getCode(0)))
        
        traversingBTreeEdges(page_.getPointer(0), graphic)
        traversingBTreeEdges(page_.getPointer(1), graphic)
        traversingBTreeEdges(page_.getPointer(2), graphic)
        traversingBTreeEdges(page_.getPointer(3), graphic)
        traversingBTreeEdges(page_.getPointer(4), graphic)

# -------------------------------------------------------------
# --------          GRAFICAR MATRIZ DISPERSA          ---------
# -------------------------------------------------------------

def graphDMatrix(dmatrix):
    print("Funcion graficar matriz de tareas")
    
    content = ["digraph G{\n\tnode [shape=box];\n\trankdir=LR\n\tedge[dir=both]\n", "", "", "", "", "", "", ""]
    
    if dmatrix.days.head and dmatrix.hours.head :
        traversingDMatrixCols(dmatrix.days.head, content)
        traversingDMatrixRows(dmatrix.hours.head, content)
    else:
        print("La matriz dispersa esta vacía")
        return

    content[0] += content[1] + content[5] + content[4] + content[7] + content[2] + content[3] + content[6] + "\n}"

    f = open(getRoute()+'\\grafoDispMatrix.dot', 'w', encoding="utf8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "\\grafoDispMatrix.dot -o "+getRoute()+"\\grafoDispMatrix.svg"
    os.system(prog)
    
    print("El grafo fue generado")

def traversingDMatrixCols(cols, content): # 1,2,3,4
    dayCol = cols
    content[7] += '\n\tc{}'.format(str(dayCol.day))
    while dayCol != None:
        nodeCell = dayCol.accesNodeCell
        
        content[1]+= '\n\tc{}[label="{}", group=0];'.format(str(dayCol.day), str(dayCol.day))
        
        content[2] += '\n\t{\n\t\trank = same;'
        content[2] += ' c{};'.format(str(dayCol.day))
        
        content[3] += '\n\tc{} -> n{}_{}'.format(str(dayCol.day), str(nodeCell.day), str(nodeCell.hour))
        while nodeCell != None:
            content[4]+= '\n\tn{}_{}[label="{}", group={}];'.format(str(nodeCell.day), str(nodeCell.hour), str(nodeCell.accesListTasks.size), str(nodeCell.hour))
            
            content[2] += ' n{}_{};'.format(str(nodeCell.day), str(nodeCell.hour))
            
            if nodeCell.below is not None:
                content[3] += ' -> n{}_{}'.format(str(nodeCell.below.day), str(nodeCell.below.hour))
            
            nodeCell = nodeCell.below
        content[2] += '\n\t}'
        content[3] += ';'

        if dayCol.next is not None:
            content[7] += ' -> c{}'.format(str(dayCol.next.day))
        dayCol = dayCol.next
    content[7] += ';'

def traversingDMatrixRows(rows, content): #5,6
    hourRow = rows
    content[7] += '\n\tf{}'.format(str(hourRow.hour))
    content[2] += '\n\t{\n\t\trank = same;'
    while hourRow != None:
        nodeCell = hourRow.accesNodeCell

        content[2] += ' f{};'.format(str(hourRow.hour))

        content[5] += '\n\tf{}[label="{}", group={}]'.format(str(hourRow.hour), str(hourRow.hour), str(hourRow.hour))

        content[6] += '\n\tf{} -> n{}_{}'.format(str(hourRow.hour), str(nodeCell.day), str(nodeCell.hour))
        while nodeCell != None:
            if nodeCell.next is not None:
                content[6] += ' -> n{}_{}'.format(str(nodeCell.next.day), str(nodeCell.next.hour))
            nodeCell = nodeCell.next
        content[6] += ';'

        if hourRow.next is not None:
            content[7] += ' -> f{}'.format(str(hourRow.next.hour))

        hourRow = hourRow.next

    content[2] += '\n\t}'
    content[7] += ';'

# -------------------------------------------------------------
# --------            GRAFICAR LISTA DOBLE            ---------
# -------------------------------------------------------------

def graphDoubleList(linkedlist, data):
    print("Funcion graficar lista tareas")
    
    content = "digraph G{\n\tnode [shape=box];\n\trankdir=LR\n"
    
    if not linkedlist.isEmpty():
        content = traversingLinkedL(linkedlist.head, data, content, "")
    else:
        print("La lista de tareas esta vacía")
        return

    content += "\n}"

    f = open(getRoute()+'\\grafoLinkedL.dot', 'w', encoding="utf8")
    try:
        f.write(content)
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "\\grafoLinkedL.dot -o "+getRoute()+"\\grafoLinkedL.svg"
    os.system(prog)
    
    print("El grafo fue generado")

def traversingLinkedL(linkedlist, data, content, links):
    aux = linkedlist
    pos = 0
    while aux is not None:
        content +='\n\tn{}[label="Posicion: {}\\n{}"]'.format(str(pos), str(pos+1), formattingData(data, aux))
        if aux.next is not None:
            links += "\n\tn{} -> n{}".format(str(pos), str(pos+1))
        else:
            content += "\n" + links
        aux = aux.next
        pos += 1
    return content

def formattingData(data, aux):
    content = data
    content += '\\nNombre: {}'.format(aux.name)
    content += '\\nDescripción: {}'.format(aux.description)
    content += '\\nCurso: {}'.format(aux.course)
    content += '\\nEstado: {}'.format(aux.status)
    return content

# -------------------------------------------------------------
# ---------            GRAFICAR TABLA HASH            ---------
# -------------------------------------------------------------

def graphHashTable(hashTable):
    print("Funcion graficar tabla hash")
    
    route_ = getRoute()
    content = ["", "", ""]
    content[0] = "digraph G{\n\tgraph[splines=compound];\n\tnode [shape=record];\n\trankdir=LR;\n"
    
    traversingHashTable(hashTable.hash_list, content)

    content[0] += content[1] + content[2] + "\n}"

    f = open(route_+'\\grafoTablaHash.dot', 'w', encoding="utf8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ route_ + "\\grafoTablaHash.dot -o "+route_+"\\grafoTablaHash.svg"
    os.system(prog)
    
    print("El grafo fue generado")

def traversingHashTable(hash_list, content):
    content[1] = "struct1 [label=\""
    f_count = 0
    init = True
    for cell in hash_list:
        if init:
            init = False
        else:
            content[1] += "|"
        if cell is not None:
            content[1] += f"<f{f_count}>{cell.card_number}"
            if cell.size != 0:
                helperTraversingListHashTable(cell.head, content, f_count)
                f_count += 1
    content[1] += "\"];"
def helperTraversingListHashTable(aux, content, id):
    content[2] += ""
    pos = 0
    init = True
    while aux is not None:
        content[2] += f"\n\tn{id}_{pos}[label=\"Posición: {pos+1}\\nTítulo: {aux.title}\"]"
        if init:
            content[2] += f"\n\tstruct1:<f{id}> -> n{id}_{pos}:w"
            init = False
        else:
            content[2] += f"\n\tn{id}_{pos-1} -> n{id}_{pos}"
        pos += 1
        aux = aux.Next

# -------------------------------------------------------------
# --------        GRAFICAR ARBOL AVL (Cursos)         ---------
# -------------------------------------------------------------

def graphRedCourses(root_, code_):
    print("Funcion graficar red")
    
    # content = ["digraph G{\n\trankdir=LR;\n\tnode [shape=box];\n", [], []]
    content = ["digraph G{\n\trankdir=LR;\n\tgraph[splines=compound];\n\tnode [shape=box];\n", [], []]

    if root_.Root != None:
        # print("No esta vacío")
        n, m = structureRedC(root_, content, code_, 0)
        print(n, m)
    else:
        return "El arbol está vacío"

    content[0] += "".join(content[1]) + "\n}"

    name = "RedCursos"

    print(getRoute())
    f = open(os.path.join(getRoute(),f'grafoAVL{name}.dot'), 'w', encoding="utf-8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + f"\\grafoAVL{name}.dot -o "+getRoute()+ f"\\grafoAVL{name}.svg"
    os.system(prog)
    
    print("El arbol avl fue generado")
    return "El arbol avl fue generado"

def structureRedC(root_,content, code_, group):
    # print("Recorriendo")
    if root_.searchCourse(code_):
        # print(f"encontrado: {code_}")
        course = root_.getCourse(code_)

        id_node = str(hash(course))
        code = course.code
        name = course.name
        credits = course.credits
        pre_code = course.pre_code
        ini, lbl = "", 0
        if pre_code:
            listPreCode = []
            if "," in pre_code:
                listPreCode = pre_code.split(",")
            else:
                listPreCode.append(pre_code)
            c = ["green", "blue", "red", "orange", "black"]
            c_i = 0
            for preCode in listPreCode:
                ini, lbl = structureRedC(root_, content, preCode, group+1)
    
                if not id_node in content[2]:
                    content[2].append(id_node)
                    content[1].append(f'\t"{id_node}"[label="Codigo: {code}\\n{name}"];\n')
                color = f"color={c[c_i]}, fontcolor={c[c_i]}"
                print(color)
                link = f'\t"{ini}":e -> "{id_node}":w[label=\"{lbl}\", {color}, group={group}];\n'
                if not link in content[1]:
                    if ini != "":
                        content[1].append(link)
                c_i += 1
        else:
            if not id_node in content[2]:
                content[2].append(id_node)
                content[1].append(f'\t"{id_node}"[label="Codigo: {code}\\nNombre: {name}"];\n')

        return id_node, credits
    else:
        print(f"Codigo inexistente {code_}")


