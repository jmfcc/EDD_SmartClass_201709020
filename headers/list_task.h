#ifndef LISTTASK_H
#define LISTTASK_H

#include "node_task.h"
#include "matrix_node_task.h"
#include "cola.h"
#include "list_student.h"
#include "validations.h"

class ListTask{
private:
    int size;
    ListStudent *refStud;
    Cola *refError;
    NodeTask *head; // List
    MatrixNode *myArrTask[5][30][9]; // Array
    int generates;

    void fillListTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);
public:
    ListTask();

    string getInputID();
    //Reference
    void setColaRef(Cola *refError_);
    void setStudentRef(ListStudent *refStud_);

    bool isEmpty();
    
    int getSize();
    void setSize(string type_);

    void insertTaskArray(int indxM, int indxD, int indxH, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);
    void insertRowMajor();
    void insertTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);
    void insertErrorTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_, string infoErr_);

    void insertTaskByConsole();
    
    void showListContent();
    void showMatrixContent();
    
    void deleteTask();
    void deleteTaskArray(int indxM, int indxD, int indxH);

    void editTaskData();
    //Existence validations
    void searchTask(string cardNumber_, int id_);
    bool isTheDateAvaible(int indxM, int indxD, int indxH);

    //Others
    bool existCardNumber(int cardNumber_);

    void graficar();
};

#endif