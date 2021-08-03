#include <iostream>
// #include <windows.h>
// #include <locale.h> // Libreria que contiene la funcion setlocale
#include "../headers/list_student.h"
#include "../headers/file_reader.h"

static ListStudent *students = new ListStudent();

int main(){
    // char cad[256];

    // SetConsoleOutputCP(1252);
    // SetConsoleCP(1252);
    // setlocale(LC_ALL, "es-GT");
    // readFile("D:\\DEVELOP\\C_C++\\U\\EDD_SmartClass_201709020\\test_files\\Estudiantes.csv");

    cout<<" Noooo puede ser, solo quería verlo con tilde"<<endl;
    cout<<""<<endl;

    students->showListContent();

    students->insertStudent(201709020, "3002613570101", "Jaime Efrain Chiroy Chavez", "Ingeniería en Ciencias y Sistemas", "jaimefrain08@gmail.com", "asdf1234", 100, 25);
    students->insertStudent(201700886, "3502451230508", "Emilia Miramontes", "Ingeniería en Ciencias y Sistemas", "nicols36@hotmail.com", "roxodiciqi", 205, 21);
    students->insertStudent(201501786, "7249529279753", "Juan Curiel", "Ingeniería Industrial", "jernimo.caballero@yahoo.com", "zanolexima", 245, 24);
    students->insertStudent(201709020, "3002613570101", "Jaime Efrain Chiroy Chavez", "Ingeniería en Ciencias y Sistemas", "jaimefrain08@gmail.com", "asdf1234", 100, 25);
    students->insertStudent(201700886, "3502451230508", "Emilia Miramontes", "Ingeniería en Ciencias y Sistemas", "nicols36@hotmail.com", "roxodiciqi", 205, 21);
    students->insertStudent(201501786, "7249529279753", "Juan Curiel", "Ingeniería Industrial", "jernimo.caballero@yahoo.com", "zanolexima", 245, 24);

    students->showListContent();

    system("pause");

    return 0;
}