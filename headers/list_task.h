#ifndef LISTTASK_H
#define LISTTASK_H

#include "node_task.h"
#include "cola.h"
#include "list_student.h"
#include "validations.h"

class ListTask{
private:
    int size;
    ListStudent *refStud;
    Cola *refError;
    NodeTask *head; // List
    NodeTask *myArrTask[5][30][9]; // Array
    int generates;

public:
    ListTask();

    //Reference
    void setColaRef(Cola *refError_);
    void setStudentRef(ListStudent *refStud_);

    bool isEmpty();
    
    int getSize();
    void setSize(string type_);

    void insertTaskArray(int indxM, int indxD, int indxH, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);

    void insertTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);
    void insertErrorTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_, string infoErr_);

    void showListContent();
    void showMatrixContent();
    
    void deleteTask(int id_);

    //Existence validations
    void searchTask(string cardNumber_, int id_);
    bool isTheDateAvaible(int indxM, int indxD, int indxH);

    //Others
    bool existCardNumber(int cardNumber_);
};

#endif