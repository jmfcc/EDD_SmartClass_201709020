#include "node_student.h"

class ListStudent{
private:
    NodeStudent *head;
    int size;

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
    void findStudentDPI(string dpi_);
    void findStudentCardNumber(int cardNumber_);

};