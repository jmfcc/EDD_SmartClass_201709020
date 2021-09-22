import os

def getRoute():
    ruta = os.path.dirname(os.path.abspath(__file__))
    return ruta+"\\img\\"

# -------------------------------------------------------------
# --------             GRAFICAR ARBOL AVL             ---------
# -------------------------------------------------------------

def graphTreeAVL(root_):
    print("Funcion graficar arbol")
    
    content = ["digraph G{\n\tnode [shape=circle];\n", ""]

    if root_.Root != None:
        traversingTreeAVL(root_.Root, content)
    else:
        print("El arbol está vacío")
        return

    content[0] += content[1] + "\n}"

    print(getRoute())
    f = open(getRoute()+'grafoAVL.dot', 'w', encoding="utf8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "grafoAVL.dot -o "+getRoute()+"grafoAVL.svg"
    os.system(prog)
    
    print("El arbol avl fue generado")

def traversingTreeAVL(root_,content):
    # print("Recorriendo")
    if root_ is not None:
        content[1] += '\t"{}"[label=" {}\\n{}\\n{}"];\n'.format(str(hash(root_)),str(root_.cardnumber), root_.name, root_.carrer)

        if root_.left is not None:
            content[1] += '\t"{}" -> "{}";\n'.format(str(hash(root_)),str(hash(root_.left)))
        if root_.right is not None:
            content[1] += '\t"{}" -> "{}";\n'.format(str(hash(root_)), str(hash(root_.right)))

        traversingTreeAVL(root_.left, content)
        traversingTreeAVL(root_.right, content)


# -------------------------------------------------------------
# --------              GRAFICAR ARBOL B              ---------
# -------------------------------------------------------------



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

    f = open(getRoute()+'grafoDispMatrix.dot', 'w', encoding="utf8")
    try:
        f.write(content[0])
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "grafoDispMatrix.dot -o "+getRoute()+"grafoDispMatrix.svg"
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

    f = open(getRoute()+'grafoLinkedL.dot', 'w', encoding="utf8")
    try:
        f.write(content)
    finally:
        f.close()

    prog = "dot -Tsvg "+ getRoute() + "grafoLinkedL.dot -o "+getRoute()+"grafoLinkedL.svg"
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