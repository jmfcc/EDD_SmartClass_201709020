#include "../headers/node_studend.h"

//Construct
NodeStudent::NodeStudent(int cardNumber_, int dpi_, string name_, string career_, string email_, string password_, int credits_, int age_){
    this->cardNumber = cardNumber_;
    this->dpi = dpi_;
    this->name = name_;
    this->career = career_;
    this->email = email_;
    this->password = password_;
    this->credits = credits_;
    this->age = age_;
    this->next = NULL;
}

//Methods - Getters
int NodeStudent::getCardNumber(){
    return this->cardNumber;
};
int NodeStudent::getDPI(){
    return this->dpi;
};
string NodeStudent::getName(){
    return this->name;
};
string NodeStudent::getCareer(){
    return this->career;
};
string NodeStudent::getEmail(){
    return this->email;
};
string NodeStudent::getPassword(){
    return this->password;
};
int NodeStudent::getCredits(){
    return this->credits;
};
int NodeStudent::getAge(){
    return this->age;
};
NodeStudent *NodeStudent::getNext(){
    return this->next;
};

//Methods - Setters
void NodeStudent::setCardNumber(int cardNumber_){
    this->cardNumber = cardNumber_;
};
void NodeStudent::setDPI(int dpi_){
    this->dpi = dpi_;
};
void NodeStudent::setName(string name_){
    this->name = name_;
};
void NodeStudent::setCareer(string career_){
    this->career = career_;
};
void NodeStudent::setEmail(string email_){
    this->email = email_;
};
void NodeStudent::setPassword(string password_){
    this->password = password_;
};
void NodeStudent::setCredits(int credits_){
    this->credits = credits_;
};
void NodeStudent::setAge(int age_){
    this->age = age_;
};
void NodeStudent::setNext(NodeStudent *next_){
    this->next = next_;
};