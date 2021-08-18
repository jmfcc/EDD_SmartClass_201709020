#include "../headers/nodo_cola.h"

NodoCola::NodoCola(NodeStudent *errStudent_, string infoErr_, int idErr_){
    this->idErr = idErr_;
    this->errStudent = errStudent_;
    this->type = "ESTUDIANTE";
    this->infoErr = infoErr_;
    this->errTask = NULL;
    this->anterior = NULL;
}

NodoCola::NodoCola(NodeTask *errTask_, string infoErr_, int idErr_){
    this->idErr = idErr_;
    this->errTask = errTask;
    this->type = "TAREA";
    this->infoErr = infoErr_;
    this->errStudent = NULL;
    this->anterior = NULL;
}

int NodoCola::getIDErr(){
    return this->idErr;
}

string NodoCola::getType(){
    return this->type;
}

string NodoCola::getInfoErr(){
    return this->infoErr;
}

NodeStudent *NodoCola::getErrStudent(){
    return this->errStudent;
}
NodeTask *NodoCola::getErrTask(){
    return this->errTask;
}

NodoCola *NodoCola::getAnterior(){
    return this->anterior;
}

void NodoCola::setIDErr(int idErr_){
    this->idErr = idErr_;
}
void NodoCola::setType(string type_){
    this->type = type_;
}
void NodoCola::setInfoErr(string infoErr_){
    this->infoErr = infoErr_;
}
void NodoCola::setErrStudent(NodeStudent *errStudent_){
    this->errStudent = errStudent_;
}
void NodoCola::setErrTask(NodeTask *errTask_){
    this->errTask = errTask_;
}

void NodoCola::setAnterior(NodoCola *anterior_){
    this->anterior = anterior_;
}

void NodoCola::showInfo(){
    cout<<endl;
    cout<<"    || Tipo de error: "<<this->type<<endl;
    cout<<"    || Info. error :  "<<this->infoErr<<endl;
    // cout<<endl;
}