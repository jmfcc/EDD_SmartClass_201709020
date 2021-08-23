#include "../headers/list_task.h"

ListTask::ListTask(){
    this->size = 0;
    this->head = NULL;
    for (int i = 0; i<5; i++){
        for (int j = 0; j<30; j++){
            for (int k = 0; k<9; k++){
                this->myArrTask[i][j][k] = NULL;
            }
        }
    }
    this->generates = 1;
    this->refError = NULL;
    this->refStud = NULL;
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
                    
                    // MatrixNode aux = *myArrTask[m][d][h];
                    // MatrixNode *aux-> = myArrTask[m][d][h];

                    insertTask(myArrTask[m][d][h]->getCardNumber(), myArrTask[m][d][h]->getTaskName(), myArrTask[m][d][h]->getTaskDesc(), myArrTask[m][d][h]->getCourse(), myArrTask[m][d][h]->getDate(), myArrTask[m][d][h]->getHour(), myArrTask[m][d][h]->getStatus(), myArrTask[m][d][h]->getMonth(), myArrTask[m][d][h]->getDay());

                } else {
                    insertTask(0, "", "", "", "", 0, "", 0, 0);
                }
            }
        }
    }
}

void ListTask::insertTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){

    int id_ = this->size + 1;
    
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

void ListTask::insertErrorTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_, string infoErr_){
    NodeTask *newNode = new NodeTask(-1, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    this->refError->queue(newNode, infoErr_);
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

void ListTask::deleteTask(int id_){
    //Not implemented
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
        file<<"\tgraph [dpi = 300];\n";
        // file<<"\tnodo_inicio[shape=point];";
        // file<<"\tnodo_null1[shape=none,label=\"NULL\"]\n";
        
        NodeTask *aux = this->head;
        int count = 0;

        while (aux != NULL) {
            string formatInfo = "ID: " + to_string(aux->getID());
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
                file<<"n"<<nodeNumb<<";\n";
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
                file<<"\n\tn"<<nNode<<"";
                init = false;
            } else {
                file<<"->n"<<nNode;
            }
            nNode++;
        }
        // while (nNode > 0){
        //     if (init){
        //         file<<"\tn"<<nNode<<"";
        //         init = false;
        //     } else {
        //         file<<"->n"<<nNode;
        //     }
        //     nNode--;
        // }

        // file<<"\tnodo_"<<limit-1<<":f1:n";
        // file<<"->nodo_null2:n\n";

        file<<"}\n";
        file.close();
        
        system(commandG.c_str());
        system(commandO.c_str());
        this->generates++;
    }
}