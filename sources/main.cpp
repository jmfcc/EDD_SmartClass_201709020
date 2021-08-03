#include <iostream>
#include "../headers/list_student.h"

int main(){

    ListStudent *students = new ListStudent();

    students->showListContent();

    students->insertStudent(201709020, "3002613570101", "Jaime Efrain Chiroy Chavez", "Ingeniería en Ciencias y Sistemas", "jaimefrain08@gmail.com", "asdf1234", 100, 25);
    students->insertStudent(201700886, "3502451230508", "Emilia Miramontes", "Ingeniería en Ciencias y Sistemas", "nicols36@hotmail.com", "roxodiciqi", 205, 21);
    students->insertStudent(201501786, "7249529279753", "Juan Curiel", "Ingeniería Industrial", "jernimo.caballero@yahoo.com", "zanolexima", 245, 24);

    students->showListContent();

    return 0;
}