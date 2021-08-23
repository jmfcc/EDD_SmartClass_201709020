#ifndef VALIDATIONS_H
#define VALIDATIONS_H

#include <iostream>
#include <string>
#include <regex>

using namespace std;
//Students
bool validaLongitud(string value_, int longitud_);
bool validaNumero(string value_);
bool validaCorreo(string value_);
//Tasks
bool validaHora(int value_); // 8 - 16 
bool validaDia(int value_); // 1 - 30
bool validaMes(int value_); // 7 - 11
bool validaEstado(string value_);
//Others
bool cadenaVacia(string value_);

#endif