#ifndef LISTSTUDENT_H
#define LISTSTUDENT_H

#include <fstream>
#include <string>
#include "node_student.h"

class ListStudent{
private:
    NodeStudent *head;
    int size;
    int generates;
public:
    //Construct
    ListStudent();

    //Methods
    bool isEmpty();
    int getSize();
    void setSize(string type_);

    void insertStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_);

    void showListContent();
    
    void deleteStudent(string dpi_);

    //Existence validations
    void searchStudentDPI(string dpi_);
    void searchStudentCardNumber(int cardNumber_);

    void graficar();
};

#endif