#ifndef FILEREADERTASK_H
#define FILEREADERTASK_H

#include <iostream>
#include <string>
#include <fstream>
#include "../headers/list_task.h"
#include "../headers/validations.h"
using namespace std;

//                                3        4          5           6         7      2       8       0      1
static string TaskFormat[9] = {"Carnet","Nombre","Descripcion","Materia","Fecha","Hora","Estado","Mes", "Dia"};

void readFileTask(string path_, ListTask *task_);
// void readFileTask(string path_, MatrixNode *refMatx, ListTask *task_);

void splitTextTask(string text_, string pattern_, string indx_, ListTask *task_);

string setIndexHeadersTask(string text_, string pattern_);

int getIndexAssignTH(string name_);

#endif