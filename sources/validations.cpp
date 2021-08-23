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

bool validaFecha(string value_){
    if (regex_match(value_, regex("[0-9]{4}/[0-9]{2}/[0-9]{2}"))){
        string dateF[3] = {"", "", ""};
        string token = "";
        int count = 0;
        for (int i = 0; i < value_.length(); i++){
            if (value_[i] != '/'){
                token += value_[i];
            } else {
                dateF[count] = token;
                token = "";
                count++;
            }
        }
        dateF[count] = token;

        if (stoi(dateF[0]) != 2021){
            return false;
        } else if (!validaMes(stoi(dateF[1]))){
            return false;
        } else if (!validaDia(stoi(dateF[2]))){
            return false;
        }
    } else {
        return false;
    }
    return true;
}
