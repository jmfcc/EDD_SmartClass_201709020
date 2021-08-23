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
    NodeTask *newNode = new NodeTask(0, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    this->myArrTask[indxM][indxD][indxH] = newNode;
}

void ListTask::insertTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){

    int id_ = this->size + 1;
    
    NodeTask *newNode = new NodeTask(id_, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_, month_, day_);
    
    if (isEmpty()){
        //Asign newNode as head
        this->head = newNode;
    } else {
        NodeTask *aux = this->head->getPrev();
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
