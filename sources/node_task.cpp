#include "../headers/node_task.h"

NodeTask::NodeTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, string hour_, string status_){
    this->id = id_;
    this->cardNumber = cardNumber_;
    this->taskName = taskName_;
    this->taskDesc = taskDesc_;
    this->course = course_;
    this->date = date_;
    this->hour = hour_;
    this->status = status_;
    this->next = NULL;
    this->prev = NULL;
}


int NodeTask::getID(){
    return this->id;
}
int NodeTask::getCardNumber(){
    return this->cardNumber;
}
string NodeTask::getTaskName(){
    return this->taskName;
}
string NodeTask::getTaskDesc(){
    return this->taskDesc;
}
string NodeTask::getCourse(){
    return this->course;
}
string NodeTask::getDate(){
    return this->date;
}
string NodeTask::getHour(){
    return this->hour;
}
string NodeTask::getStatus(){
    return this->status;
}
NodeTask *NodeTask::getNext(){
    return this->next;
}
NodeTask *NodeTask::getPrev(){
    return this->prev;
}


void NodeTask::setID(int id_){
    this->id = id_;
}
void NodeTask::setCardNumber(int cardNumber_){
    this->cardNumber = cardNumber_;
}
void NodeTask::setTaskName(string taskName_){
    this->taskName = taskName_;
}
void NodeTask::setTaskDesc(string taskDesc_){
    this->taskDesc = taskDesc_;
}
void NodeTask::setCourse(string course_){
    this->course = course_;
}
void NodeTask::setDate(string date_){
    this->date = date_;
}
void NodeTask::setHour(string hour_){
    this->hour = hour_;
}
void NodeTask::setStatus(string status_){
    this->status = status_;
}
void NodeTask::setNext(NodeTask *next_){
    this->next = next_;
}
void NodeTask::setPrev(NodeTask *prev_){
    this->prev = prev_;
}

void NodeTask::showInfo(){
    cout<<" "<<endl;
    cout<<"  >> Carnet:    "<<this->cardNumber<<endl;
    cout<<"  >> ID - Task: "<<this->id<<endl;
    cout<<"  >> Course: "<<this->course<<endl;
    cout<<"  >> Task Name: "<<this->taskName<<endl;
    cout<<" "<<endl;
}