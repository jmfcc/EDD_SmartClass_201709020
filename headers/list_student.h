#ifndef LISTSTUDENT_H
#define LISTSTUDENT_H

#include <fstream>
#include <string>
#include "node_student.h"
#include "cola.h"

class ListStudent{
private:
    NodeStudent *head;
    Cola *refError;
    int size;
    int generates;
public:
    //Construct
    ListStudent();

    //Reference
    void setColaRef(Cola *refError_);

    //Methods
    bool isEmpty();
    int getSize();
    void setSize(string type_);

    void insertStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_);
    void insertErrorStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_, string infoErr_);
    void showListContent();
    
    void deleteStudent(string dpi_);

    //Existence validations
    bool searchStudentByDPI(string dpi_);
    bool searchStudentByCardNumber(int cardNumber_);

    void graficar();
};

#endif