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
    int hour;
    string status;
    int month;
    int day;
    NodeTask *next;
    NodeTask *prev;

public:
    NodeTask(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);

    int getID();
    int getCardNumber();
    string getTaskName();
    string getTaskDesc();
    string getCourse();
    string getDate();
    int getHour();
    string getStatus();
    int getMonth();
    int getDay();

    NodeTask *getNext();
    NodeTask *getPrev();

    void setID(int id_);
    void setCardNumber(int cardNumber_);
    void setTaskName(string taskName_);
    void setTaskDesc(string taskDesc_);
    void setCourse(string course_);
    void setDate(string date_);
    void setHour(int hour_);
    void setStatus(string status_);
    void setMonth(int month_);
    void setDay(int day_);
    void setNext(NodeTask *next_);
    void setPrev(NodeTask *prev_);

    void showInfo();
};

#endif