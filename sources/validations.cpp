#include "../headers/validations.h"

bool validaLongitud(string value_, int longitud_){
    return value_.length() == longitud_;
}
bool validaNumero(string value_){
    for (int i = 0; i < value_.length(); i++){
        if (!isdigit(value_[i])){
            return false;
        }
    }
    return true;
}
bool validaCorreo(string value_){
    return regex_match(value_, regex("[a-z0-9]+(\\.[a-z0-9]+)*@[a-z0-9]+(\\.[a-z0-9]+)*\\.(com|es|org)"));
}
bool cadenaVacia(string value_){
    bool empty = true;
    for (int i = 0; i < value_.length(); i++){
        if (!isspace(value_[i])){
            empty = false;
            break;
        }
    }
    return empty;
}

bool validaHora(int value_){
    if (value_ >= 8 and value_ <=16){
        return true;
    }
    return false;
}
bool validaDia(int value_){
    if (value_ >= 1 and value_ <=30){
        return true;
    }
    return false;
}
bool validaMes(int value_){
    if (value_ >= 7 and value_ <=11){
        return true;
    }
    return false;
}

bool validaEstado(string value_){
    string typesStatus[4] = {"Pendiente", "Realizado", "Incumplido", "Cumplido"};
    for (int i = 0; i < 4; i++){
        if (value_ == typesStatus[i]){
            return true;
        }
    }
    return false;
}
