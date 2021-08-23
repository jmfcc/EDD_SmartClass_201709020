#include "../headers/matrix_node_task.h"

MatrixNode::MatrixNode(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_){
    this->id = id_;
    this->cardNumber = cardNumber_;
    this->taskName = taskName_;
    this->taskDesc = taskDesc_;
    this->course = course_;
    this->date = date_;
    this->hour = hour_;
    this->status = status_;
    this->month = month_;
    this->day = day_;
}


int MatrixNode::getID(){
    return this->id;
}
int MatrixNode::getCardNumber(){
    return this->cardNumber;
}
string MatrixNode::getTaskName(){
    return this->taskName;
}
string MatrixNode::getTaskDesc(){
    return this->taskDesc;
}
string MatrixNode::getCourse(){
    return this->course;
}
string MatrixNode::getDate(){
    return this->date;
}
int MatrixNode::getHour(){
    return this->hour;
}
string MatrixNode::getStatus(){
    return this->status;
}
int MatrixNode::getMonth(){
    return this->month;
}
int MatrixNode::getDay(){
    return this->day;
}

void MatrixNode::setID(int id_){
    this->id = id_;
}
void MatrixNode::setCardNumber(int cardNumber_){
    this->cardNumber = cardNumber_;
}
void MatrixNode::setTaskName(string taskName_){
    this->taskName = taskName_;
}
void MatrixNode::setTaskDesc(string taskDesc_){
    this->taskDesc = taskDesc_;
}
void MatrixNode::setCourse(string course_){
    this->course = course_;
}
void MatrixNode::setDate(string date_){
    this->date = date_;
}
void MatrixNode::setHour(int hour_){
    this->hour = hour_;
}
void MatrixNode::setStatus(string status_){
    this->status = status_;
}
void MatrixNode::setMonth(int month_){
    this->month = month_;
}
void MatrixNode::setDay(int day_){
    this->day = day_;
}

void MatrixNode::showInfo(){
    cout<<" "<<endl;
    cout<<"  >> Carnet:    "<<this->cardNumber<<endl;
    cout<<"  >> ID - Task: "<<this->id<<endl;
    cout<<"  >> Course: "<<this->course<<endl;
    cout<<"  >> Task Name: "<<this->taskName<<endl;
    cout<<" "<<endl;
}