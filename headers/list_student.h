#include "node_studend.h"

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

    void insertStudent(int cardNumber_, int dpi_, string name_, string career_, string email_, string password_, int credits_, int age_);

    void showListContent();
    
    void deleteStudent(int dpi_);

    //Existence validations
    void findStudentDPI(int dpi_);
    void findStudentCardNumber(int cardNumber_);

};