#include <iostream>
#include <string>

using namespace std;

class NodeStudent{
private:
    int cardNumber;
    string dpi;
    string name;
    string career;
    string email;
    string password;
    int credits;
    int age;
    NodeStudent *next;
    NodeStudent *prev;

public:
    //Construct
    NodeStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_);

    //Methods - Getters
    int getCardNumber();
    string getDPI();
    string getName();
    string getCareer();
    string getEmail();
    string getPassword();
    int getCredits();
    int getAge();
    NodeStudent *getNext();
    NodeStudent *getPrev();

    //Methods - Setters
    void setCardNumber(int cardNumber_);
    void setDPI(string dpi_);
    void setName(string name_);
    void setCareer(string career_);
    void setEmail(string email_);
    void setPassword(string password_);
    void setCredits(int credits_);
    void setAge(int age_);
    void setNext(NodeStudent *next_);
    void setPrev(NodeStudent *prev_);

    void showInfo();
};