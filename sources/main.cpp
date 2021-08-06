#include <iostream>
#include <string>

#include "../headers/list_student.h"
#include "../headers/file_reader.h"

using namespace std;

static ListStudent *students = new ListStudent();

int main(){

    readFile("D:\\DEVELOP\\C_C++\\U\\EDD_SmartClass_201709020\\test_files\\Estudiantes.csv");
    string msg = u8" Noooo puede ser, solo quería verlo con tilde áéíóú";
    cout<<msg<<endl;
    cout<<""<<endl;

    students->showListContent();

    students->insertStudent(201709020, "3002613570101", "Jaime Efrain Chiroy Chavez", "Ingeniería en Ciencias y Sistemas", "jaimefrain08@gmail.com", "asdf1234", 100, 25);
    students->insertStudent(201700886, "3502451230508", "Emilia Miramontes", "Ingeniería en Ciencias y Sistemas", "nicols36@hotmail.com", "roxodiciqi", 205, 21);
    students->insertStudent(201501786, "7249529279753", "Juan Curiel", "Ingeniería Industrial", "jernimo.caballero@yahoo.com", "zanolexima", 245, 24);
    students->insertStudent(201709020, "3002613570101", "Jaime Efrain Chiroy Chavez", "Ingeniería en Ciencias y Sistemas", "jaimefrain08@gmail.com", "asdf1234", 100, 25);
    students->insertStudent(201700886, "3502451230508", "Emilia Miramontes", "Ingeniería en Ciencias y Sistemas", "nicols36@hotmail.com", "roxodiciqi", 205, 21);
    students->insertStudent(201501786, "7249529279753", "Juan Curiel", "Ingeniería Industrial", "jernimo.caballero@yahoo.com", "zanolexima", 245, 24);

    students->showListContent();


    string inputUser;
    // cin.ignore(); // 
    getline(cin, inputUser);  // input de cadena con espacios
    // printf(inputUser);
    // cin >> inputUser;  // Input de una cadena sin espacios
    cout << inputUser << endl;

    system("pause");

    return 0;
}