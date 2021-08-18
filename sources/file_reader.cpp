#include "../headers/file_reader.h"

void readFileStudent(string path_, ListStudent *stud){
    cout<<" >> Path File: "<<path_<<endl;

    string myText; //For lines of the file
    ifstream myFile(path_); // Open the file
    bool init = true;
    string indexHeaders = "";
    // string texto[] = new string[5];
    while(getline(myFile, myText)){
        // cout<<myText<<endl;
        if (init == true){
            init = false;
            indexHeaders = setIndexHeadersStudent(myText, ",");
        }else{
            splitTextStudent(myText, ",", indexHeaders, stud);
            // cout << " ------------------------" << endl;
        }
    }

    myFile.close();
    // delete [] indexHeaders;
}

void splitTextStudent(string text_, string pattern_, string indx_, ListStudent *stud){
    size_t pos = 0;
    string captura;
    string studentData[8];
    int count = 0;
    while ((pos = text_.find(pattern_)) != string::npos) { //Evalua y captura la posicion del patron buscado
        captura = text_.substr(0, pos); //Obtiene el texto entre el inicio de cadena y el la posición capturada
        // cout << captura << endl;
        studentData[count] = captura; //Agrega a la lista temporal el valor capturado/obtenido
        text_.erase(0, pos + pattern_.length()); // Elimina de la cadena el texto entre el inicio de la cadena hasta la posición del patrón mas la longitud del patron
        count++; //Aumento el contador
    }
    studentData[count] = text_; //dado que el texto restante no posee el "delimitador" al final, este utlimo texto se almacena fuera del ciclo
    
    //Funcion que castea a enteron un string
    int listPos[8] = {0,0,0,0,0,0,0,0};
    for (int i = 0; i < 8; i++){
        listPos[i] = indx_[i]-'0'; // Obtiene el orden de indice para enviar los datos a su parametro correcto
    }
    
    if (!validaLongitud(studentData[listPos[0]], 9)){
        string msg = "El carnet no tiene la cantidad de digitos esperados";
        stud->insertErrorStudent(0, studentData[listPos[1]], studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (!validaNumero(studentData[listPos[0]])){
        string msg = "El carnet posee valores no numericos";
        stud->insertErrorStudent(0, studentData[listPos[1]], studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (!validaLongitud(studentData[listPos[1]],13)){
        string msg = "El dpi no tiene la cantidad de digitos esperados";
        stud->insertErrorStudent(std::stoi(studentData[listPos[0]]), "0", studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (!validaNumero(studentData[listPos[1]])){
        string msg = "El dpi posee valores no numericos";
        stud->insertErrorStudent(std::stoi(studentData[listPos[0]]), "0", studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (stud->searchStudentByCardNumber(std::stoi(studentData[listPos[0]]))){
        string msg = "El carnet ya está registrado";
        stud->insertErrorStudent(0, studentData[listPos[1]], studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (stud->searchStudentByDPI(studentData[listPos[1]])){
        string msg = "El dpi ya esta registrado";
        stud->insertErrorStudent(std::stoi(studentData[listPos[0]]), "0", studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } 
    else if (!validaCorreo(studentData[listPos[4]])){
        string msg = "El correo posee un formato incorrecto";
        stud->insertErrorStudent(std::stoi(studentData[listPos[0]]), "0", studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]), msg);
        return;
    } else{
        stud->insertStudent(std::stoi(studentData[listPos[0]]), studentData[listPos[1]], studentData[listPos[2]], studentData[listPos[3]], studentData[listPos[4]], studentData[listPos[5]], std::stoi(studentData[listPos[6]]), std::stoi(studentData[listPos[7]]));
    }
    // students->showListContent();
    // system("pause");
}

string setIndexHeadersStudent(string text_, string pattern_){
    int *iHS_ = new int[8];
    string iHS = "";
    size_t pos = 0;
    string token;
    int index = 0;
    while ((pos = text_.find(pattern_)) != string::npos) {
        token = text_.substr(0, pos);
        int i = getIndexAssignSH(token);
        iHS_[i] = index;
        // cout << token << endl;
        text_.erase(0, pos + pattern_.length());
        index ++;
    }
    // cout << text_ << endl;
    int i = getIndexAssignSH(text_);
    iHS_[i] = index;
    for (int i = 0; i<8; i++){
        iHS += to_string(iHS_[i]);
    }
    return iHS;
}

int getIndexAssignSH(string name_){
    for (int i = 0; i < 8; i++){
        if (name_ == studentFormat[i]){
            return i;
        }
    }
    return -1;
}
