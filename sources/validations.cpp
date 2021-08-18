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