#include "../headers/list_student.h"

ListStudent::ListStudent(){
    this->head = NULL;
    this->size = 0;
}

bool ListStudent::isEmpty(){
    return this->head == NULL;
}
int ListStudent::getSize(){
    return this->size;
}

void ListStudent::setSize(string type_){
    if (type_ == "increase"){
        this->size++;
    } else {
        this->size--;
    }
}

void ListStudent::insertStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_){
    NodeStudent *newNode = new NodeStudent(cardNumber_, dpi_, name_, career_, email_, password_, credits_, age_);
    
    if (isEmpty()){
        //Reference itself
        newNode->setNext(newNode);
        newNode->setPrev(newNode);
        //Asign newNode as head
        this->head = newNode;
    } else {
        NodeStudent *aux = this->head->getPrev();
        aux->setNext(newNode);
        newNode->setPrev(aux);
        newNode->setNext(this->head);
        this->head->setPrev(newNode);
    }
    setSize("increase");
    // this->size++;
}

void ListStudent::showListContent(){
    cout<<"--------------- LISTA DE ESTUDIANTES ----------------"<<endl;
    if (this->size > 0){
        int counter = 0;
        while (counter < this->size){
            counter++;
            this->head->showInfo();
            cout<<"-----------------------------------------------------"<<endl;
            this->head = this->head->getNext();
        }   
    } else {
        cout<<"              - SIN REGISTROS - "<< endl;
        cout<<endl;
    }
}

void ListStudent::deleteStudent(string dpi_){
    //Not implemented
}

void ListStudent::findStudentDPI(string dpi_){
    //Not implemented
}

void ListStudent::findStudentCardNumber(int cardNumber_){
    //Not implemented
}
