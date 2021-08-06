#ifndef NODETASK_H
#define NODETASK_H

#include <iostream>
#include <string>

using namespace std;

class NodeTask{
private:
    int id;
    int cardNumber;
    string taskName;
    string taskDesc;
    string course;
    string date;
    string hour;
    string status;
    NodeTask *next;
    NodeTask *prev;

public:
    NodeTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, string hour_, string status_);

    int getID();
    int getCardNumber();
    string getTaskName();
    string getTaskDesc();
    string getCourse();
    string getDate();
    string getHour();
    string getStatus();
    NodeTask *getNext();
    NodeTask *getPrev();

    void setID(int id_);
    void setCardNumber(int cardNumber_);
    void setTaskName(string taskName_);
    void setTaskDesc(string taskDesc_);
    void setCourse(string course_);
    void setDate(string date_);
    void setHour(string hour_);
    void setStatus(string status_);
    void setNext(NodeTask *next_);
    void setPrev(NodeTask *prev_);

    void showInfo();
};

#endif