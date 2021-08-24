#ifndef FILEREADER_H
#define FILEREADER_H

#include <iostream>
#include <string>
#include <fstream>
#include "../headers/list_student.h"
#include "../headers/validations.h"
using namespace std;
//                                   0       1      2         3        7         4           5        6
static string studentFormat[8] = {"Carnet","DPI","Nombre","Carrera","Correo","Password","Creditos","Edad"};

void readFileStudent(string path_, ListStudent *stud);

void splitTextStudent(string text_, string pattern_, string indx_, ListStudent *stud);

string setIndexHeadersStudent(string text_, string pattern_);

int getIndexAssignSH(string name_);

#endif