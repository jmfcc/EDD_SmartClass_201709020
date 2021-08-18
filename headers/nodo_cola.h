#ifndef NODOCOLA_H
#define NODOCOLA_H

#include <iostream>
#include <string>
#include "node_student.h"
#include "node_task.h"

using namespace std;

class NodoCola{
private:
    int idErr;
    string type; //Student or task
    string infoErr;
    NodeStudent *errStudent;
    NodeTask *errTask;

    NodoCola *anterior;

public:
    NodoCola(NodeStudent *errStudent_, string infoErr_, int idErr_);
    NodoCola(NodeTask *errTask_, string infoErr_, int idErr_);

    int getIDErr();
    string getType();
    string getInfoErr();
    NodeStudent *getErrStudent();
    NodeTask *getErrTask();

    NodoCola *getAnterior();

    void setIDErr(int idErr_);
    void setType(string type_);
    void setInfoErr(string infoErr_);
    void setErrStudent(NodeStudent *errStudent_);
    void setErrTask(NodeTask *errTask_);
    
    void setAnterior(NodoCola *anterior_);

    void showInfo();
};


#endif