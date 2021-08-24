#include "../headers/list_task.h"

ListTask::ListTask(){
    this->size = 0;
    this->head = NULL;
    for (int i = 0; i<5; i++){ // Llenado de matriz
        for (int j = 0; j<30; j++){
            for (int k = 0; k<9; k++){
                this->myArrTask[i][j][k] = NULL;
            }
        }
    }
    for (int m = 0; m<5; m++){ // Llenado de lista doble
        for (int d = 0; d<30; d++){
            for (int h = 0; h<9; h++){
                int indx = h+9*(d+30*m);
                fillListTask(indx, 0, "", "", "", "", 0, "", 0, 0);
            }
        }
    }
    this->generates = 1;
    this->refError = NULL;
    this->refStud = NULL;
}

string ListTask::getInputID(){
    string id_ = "";
    // bool in = true;
    do {
        id_= "";
        cout<<"   >> Ingresa el ID de la tarea: ";
        getline(cin, id_);
        if (id_ == ""){
            return id_;
        }
    } while (!validaNumero(id_));
    return id_;
}

void ListTask::setColaRef(Cola *refError_){
    this->refError = refError_;
}
void ListTask::setStudentRef(ListStudent *refStud_){
    this->refStud = refStud_;
}

bool ListTask::isEmpty(){
    return this->head == NULL;
}

int ListTask::getSize(){
    return this->size;
}

void ListTask::setSize(string type_){
    if (type_ == "increase"){
        this->size++;
    } else {
        this->size--;
    }
}

void ListTask::insertTaskArray(int indxM, int indxD, int indxH, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){
    this->myArrTask[indxM][indxD][indxH] = new MatrixNode(0, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    //  = newNode;
}

void ListTask::insertRowMajor(){
    for (int m = 0; m<5; m++){
        for (int d = 0; d<30; d++){
            for (int h = 0; h<9; h++){
                int indx = h+9*(d+30*m);
                if (this->myArrTask[m][d][h] != NULL){
                    insertTask(indx, myArrTask[m][d][h]->getCardNumber(), myArrTask[m][d][h]->getTaskName(), myArrTask[m][d][h]->getTaskDesc(), myArrTask[m][d][h]->getCourse(), myArrTask[m][d][h]->getDate(), myArrTask[m][d][h]->getHour(), myArrTask[m][d][h]->getStatus(), myArrTask[m][d][h]->getMonth(), myArrTask[m][d][h]->getDay());

                }
            }
        }
    }
}

void ListTask::fillListTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){

    // int id_ = this->size + 1;
    
    NodeTask *newNode = new NodeTask(id_, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    
    if (isEmpty()){
        //Asign newNode as head
        this->head = newNode;
    } else {
        NodeTask *aux = this->head;
        while (aux->getNext() != NULL){
            aux = aux->getNext();
        }
        aux->setNext(newNode);
        newNode->setPrev(aux);
    }
    setSize("increase");
    // this->size++;
}

void ListTask::insertTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){
    
    NodeTask *aux = this->head;

    while (aux != NULL){
        if (aux->getID() == id_){
            break;
        }
        aux = aux->getNext();
    }
    aux->setCardNumber(cardNumber_);
    aux->setTaskName(taskName_);
    aux->setTaskDesc(taskDesc_);
    aux->setCourse(course_);
    aux->setDate(date_);
    aux->setHour(hour_);
    aux->setStatus(status_);
    aux->setMonth(month_);
    aux->setDay(day_);
}

void ListTask::insertErrorTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_, string infoErr_){
    NodeTask *newNode = new NodeTask(-1, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    this->refError->queue(newNode, infoErr_);
}

void ListTask::insertTaskByConsole(){
    cout<<"\n  ------ Agregar Tarea -----------"<<endl;
    cout<<"  Nota: Para cancelar la operacion, deje un campo vacio y presione enter"<<endl;
    string data[9] = {"", "", "", "", "", "", "", "", ""};
    bool init = true;
    int i = 0;
    while (i < 7) {
        bool isOk = false;
        while (!isOk) {
            switch (i) {
                case 0:
                    cout<<"     >> Ingresa el numero de carnet: ";
                    break;
                case 1:
                    cout<<"     >> Ingresa el nombre de la tarea: ";
                    break;
                case 2:
                    cout<<"     >> Ingresa la descripcion: ";
                    break;
                case 3:
                    cout<<"     >> Ingresa el curso: ";
                    break;
                case 4:
                    cout<<"     >> Ingresa la hora (8 - 16): ";
                    break;
                case 5:
                    cout<<"     >> Ingresa la fecha (YYYY/MM/DD): ";
                    break;
                case 6:
                    cout<<"     >> Ingresa el estado: ";
                    break;
            }
            string input = "";

            getline(cin, input);
            if (input != ""){
                switch (i) {
                    case 0: //Carnet
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaLongitud(input, 9)){
                            cout<<"       --> Error: La longitud del carnet es distinta de la esperada"<<endl;
                        } else if (!refStud->searchStudentByCardNumber(stoi(input))){
                            cout<<"       --> Error: El carnet ingresado no esta registrado"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 4:  // Hora
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaHora(stoi(input))){
                            cout<<"       --> Error: La hora está fuera del rango permitido"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 5:  // Fecha
                        if (!validaFecha(input)){
                            cout<<"       --> Error: Verifique que la fecha este correcta y se encuentre en el rango permitido"<<endl;
                        } else {

                            string month_ = getSeparateMonth(input);
                            string day_ = getSeparateDay(input);
                            if (!isTheDateAvaible(stoi(month_)-7, stoi(day_)-1, stoi(data[4])-8)){
                                cout<<"       --> Error: En esta fecha y hora ya esta registrada una tarea"<<endl;
                                i = 4;
                            } else {
                                data[i] = input;
                                data[7] = month_;
                                data[8] = day_;
                                isOk = true;
                            }
                        }
                        break;
                    case 6:  // Estado
                        if (!validaEstado(input)){
                            cout<<"       --> Error: El estado unicamente puede ser, Pendiente-Realizado-Cumplido-Incumplido"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    default:  // Name, TaskName, TaskDesc, Course
                        data[i] = input;
                        isOk = true;
                        break;
                }
            }else{
                cout<<"     --> Se ha anulado la operacion"<<endl;
                return;
            }
        }
        i++;
    }
    // int indx = h + 9 * ( d + 30 * m );
    int indx = (stoi(data[4])-8) + 9 * ((stoi(data[8])-1) + ( 30 * (stoi(data[7])-7)));
    insertTaskArray(stoi(data[7])-7, stoi(data[8])-1, stoi(data[4])-8, stoi(data[0]), data[1], data[2], data[3], data[5], stoi(data[4]), data[6], stoi(data[7]), stoi(data[8]));

    insertTask(indx, stoi(data[0]), data[1], data[2], data[3], data[5], stoi(data[4]), data[6], stoi(data[7]), stoi(data[8]));
    cout<<"\n   >> Se ha guardado el registro"<<endl;
}

void ListTask::showListContent(){
    cout<<"----------------- LISTA DE TAREAS ------------------"<<endl;
    if (this->size > 0){
        NodeTask *aux = this->head;
        while (aux != NULL){
            aux->showInfo();
            cout<<"-----------------------------------------------------"<<endl;
            aux = aux->getNext();
        }   
    } else {
        cout<<endl;
        cout<<"              - SIN REGISTROS - "<< endl;
        cout<<endl;
    }
}

void ListTask::showMatrixContent(){
    for (int m = 0; m < 5; m++){
        for (int d = 0; d < 30; d++){
            string concat = "";
            if (d < 10){
                concat += "D#"+ to_string(d) + " : ";
            } else {
                concat += "D#"+ to_string(d) + ": ";
            }
            for (int h = 0; h < 9; h++){
                if (this->myArrTask[m][d][h] == NULL){
                    concat += "-";
                } else {
                    concat += "8";
                }
            }
            cout<<concat<<endl;
        }
        cout<<endl;
    }
}

void ListTask::deleteTask(){
    string sid_ = getInputID();
    if (sid_ == ""){
        cout<<"    --> Se ha cancelado la operación"<<endl;
        return;
    }
    
    int id_ = stoi(sid_) - 1;
    if (id_ < 0 || id_ > 1349){
        cout<<"    --> Error: ID fuera de rango"<<endl;
        return;
    }

    NodeTask *aux = this->head;
    while(aux != NULL){
        if (aux->getID() == id_){
            if (aux->getCardNumber() != 0){
                string confirm = "";
                cout<<"    >> Aviso: Esta seguro que desea eliminar la tarea (Y/N)?: ";
                getline(cin, confirm);
                if (confirm == "Y" || confirm == "y"){
                    deleteTaskArray(aux->getMonth(), aux->getDay(), aux->getHour());
                    aux->clearNodeValues();
                }  else {
                    cout<<"     --> Se ha anulado la operacion"<<endl;
                }
            } else {
                cout<<"     --> Error: La tarea seleccionada no existe"<<endl;
            }
        }
        aux = aux->getNext();
    }
}

void ListTask::deleteTaskArray(int indxM, int indxD, int indxH){
    myArrTask[indxM-7][indxD-1][indxH-8] = NULL;
}

void ListTask::editTaskData(){
    string sid_ = getInputID();
    if (sid_ == ""){
        cout<<"    --> Se ha cancelado la operación"<<endl;
        return;
    }
    
    int id_ = stoi(sid_) - 1;
}

void ListTask::searchTask(string cardNumber_, int id_){
    //Not implemented
}

bool ListTask::isTheDateAvaible(int indxM, int indxD, int indxH){
    if (this->myArrTask[indxM][indxD][indxH] == NULL){
        return true;
    }
    return false;   
}
bool ListTask::existCardNumber(int cardNumber_){
    return refStud->searchStudentByCardNumber(cardNumber_);
}

void ListTask::graficar(){
    int limit = this->size;
    string commandG = "dot -Tpng task.dot -o statusTask"+to_string(this->generates)+".png";
    string commandO = "start statusTask"+to_string(this->generates)+".png";
    if (isEmpty()){
        cout<<"\n     --- NO HAY REGISTROS EN LISTA DE TAREAS PARA GRAFICAR ---"<<endl;
    }else{
        ofstream file;
        file.open("task.dot");
        cout<<"\n    - Generando task.dot -"<<endl;
        
        file<<"digraph D {\n";
        file<<"\trankdir=LR\n";
        file<<"\tgraph [dpi = 200];\n";
        file<<"\tedge[dir=both];\n";
        
        NodeTask *aux = this->head;
        int count = 0;

        while (aux != NULL) {
            string formatInfo = "ID: " + to_string(aux->getID()+1);
            if (aux->getCardNumber() != 0){
                formatInfo += "\\nCarnet: " + to_string(aux->getCardNumber())
                + "\\nNombre Tarea: " + aux->getTaskName()
                + "\\nDescripcion: " + aux->getTaskDesc();
            } else {
                formatInfo += "\\nVACIO";
            }
            
            file<<"\tn"<<count<<"[shape=box,label=\"";
            file<<formatInfo;
            file<<"\"];\n";
            
            aux = aux->getNext();
            count++;
        }
        // file<<"\tnodo_null2[shape=none,label=\"NULL\"]\n";
        file<<"\n";
        for (int i = 0; i < 27; i++){
            file<<"\t{\n";
            file<<"\t\trank = same;\n";
            int colCount = 0;
            int nodeNumb = 0;
            while (colCount < 50) {
                if (colCount%2 == 0){
                    nodeNumb = i + (colCount*27);
                } else {
                    nodeNumb = ((colCount+1)*27)-(1+i);
                }
                file<<"\t\tn"<<nodeNumb<<";\n";
                colCount++;
            }

            file<<"\t}\n";
        }

        int nNode = 0;
        bool init = true;
        for (int i = 0; i <= 675; i++){
            if (init){
                file<<"\tn"<<nNode<<"";
                init = false;
            } else {
                file<<"->n"<<nNode;
            }
            nNode++;
        }
        init = true;
        nNode--;
        for (int i = 675; i < 1350; i++){
            if (init){
                file<<";\n\tn"<<nNode<<"";
                init = false;
            } else {
                file<<"->n"<<nNode;
            }
            nNode++;
        }

        nNode--;
        init = true;
        while (nNode >= 675){
            if (init){
                file<<";\n\tn"<<nNode<<"";
                init = false;
            } else {
                file<<"->n"<<nNode;
            }
            nNode--;
        }
        nNode++;
        init = true;
        while (nNode >= 0){
            if (init){
                file<<";\n\tn"<<nNode<<"";
                init = false;
            } else {
                file<<"->n"<<nNode;
            }
            nNode--;
        }


        file<<"\n}\n";
        file.close();
        
        system(commandG.c_str());
        system(commandO.c_str());
        this->generates++;
    }
}