#ifndef LISTTASK_H
#define LISTTASK_H

#include "node_task.h"

class ListTask{
private:
    int size;
    NodeTask *head;

public:
    ListTask();

    bool isEmpty();
    
    int getSize();
    void setSize(string type_);

    void insertTask(int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, string hour_, string status_);

    void showListContent();
    
    void deleteTask(int id_);

    //Existence validations
    void searchTask(string cardNumber_, int id_);
    

};

#endif