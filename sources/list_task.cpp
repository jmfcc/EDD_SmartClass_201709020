#include "../headers/list_task.h"

ListTask::ListTask(){
    this->size = 0;
    this->head = NULL;
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

void ListTask::insertTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, string hour_, string status_){

    int id_ = this->size + 1;
    
    NodeTask *newNode = new NodeTask(id_, cardNumber_, taskName_, taskDesc_, course_, date_, hour_, status_);
    
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

void ListTask::deleteTask(int id_){
    //Not implemented
}

void ListTask::searchTask(string cardNumber_, int id_){
    //Not implemented
}
