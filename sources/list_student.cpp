#include "../headers/list_student.h"

ListStudent::ListStudent(){
    this->head = NULL;
    this->refError = NULL;
    this->size = 0;
    this->generates = 1;
}
void ListStudent::setColaRef(Cola *refError_){
    this->refError = refError_;
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
        //Self-Reference
        newNode->setNext(newNode);
        newNode->setPrev(newNode);
        //Asign newNode as head pointer
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

void ListStudent::insertErrorStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_, string infoErr_){
    NodeStudent *newNode = new NodeStudent(cardNumber_, dpi_, name_, career_, email_, password_, credits_, age_);
    this->refError->queue(newNode, infoErr_);
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

bool ListStudent::searchStudentByDPI(string dpi_){
    if (this->size > 0){
        NodeStudent *aux = this->head;
        do {
            if (aux->getDPI() == dpi_){
                return true;
            }
            aux = aux->getNext();
        } while (aux != this->head);
    }
    return false;
}

bool ListStudent::searchStudentByCardNumber(int cardNumber_){
    if (this->size > 0){
        NodeStudent *aux = this->head;
        do {
            if (aux->getCardNumber() == cardNumber_){
                return true;
            }
            aux = aux->getNext();
        } while (aux != this->head);
        
    }
    return false;
}

void ListStudent::graficar(){
    int limit = this->size;
    string commandG = "dot -Tpng students.dot -o statusStudents"+to_string(this->generates)+".png";
    string commandO = "start statusStudents"+to_string(this->generates)+".png";
    if (isEmpty()){
        cout<<"\n     --- NO HAY REGISTROS PARA GRAFICAR ---"<<endl;
    }else{
        ofstream file;
        file.open("students.dot");
        cout<<"\n    - Generando students.dot -"<<endl;
        
        file<<"digraph D {\n";
        file<<"\trankdir=LR\n";
        file<<"\tgraph [dpi = 300];\n";
        file<<"\tnodo_inicio[shape=point];";
        
        NodeStudent *aux = this->head;
        int count = 0;

        do{
            string formatInfo = "DPI: " + aux->getDPI() 
            + "\\nCarnet: " + to_string(aux->getCardNumber())
            + "\\nNombre: " + aux->getName();
            
            file<<"\tnodo_"<<count<<"[shape=record,label=\"{<f0>|<f2>";
            file<<formatInfo;
            file<<"|<f1>}\"];\n";
            
            aux = aux->getNext();
            count++;
        } while (aux != head);

        file<<"\n";
        file<<"\tnodo_inicio->nodo_0[label=\"Primero\"]\n";

        if (limit == 1){
            file<<"\tnodo_0:f1:n->nodo_0:f0:n\n";
            file<<"\tnodo_0:f0:s->nodo_0:f1:s\n";
        }else{
            for (int i = 1; i < limit; i++){
                file<<"\tnodo_"<<i-1<<":f1:n";
                file<<"->";
                file<<"nodo_"<<i<<":f0:n\n";

                file<<"\tnodo_"<<i<<":f0:s";
                file<<"->";
                file<<"nodo_"<<i-1<<":f1:s\n";
            }
            file<<"\tnodo_"<<limit-1<<":f1:n";
            file<<"->nodo_0:f0:n\n";

            file<<"\tnodo_0:f0:s\n";
            file<<"->nodo_"<<limit-1<<":f1:s";
        }
        file<<"}\n";
        file.close();
        
        system(commandG.c_str());
        system(commandO.c_str());
        this->generates++;
    }
}