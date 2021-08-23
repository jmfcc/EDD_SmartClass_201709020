#ifndef MATRIXNODETASK_H
#define MATRIXNODETASK_H

#include <iostream>
#include <string>

using namespace std;

class MatrixNode{
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

public:
    MatrixNode(int id_, int cardNumber_, string taskName_, string taskDesc_, string course_, string date_, int hour_, string status_, int month_, int day_);

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
    
    void showInfo();
};

#endif