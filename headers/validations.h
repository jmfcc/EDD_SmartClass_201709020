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
bool validaHora(int value_);
bool validaDia(int value_);
bool validaMes(int value_);
//Others
bool cadenaVacia(string value_);

#endif