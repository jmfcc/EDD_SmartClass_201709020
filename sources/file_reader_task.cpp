#include "../headers/file_reader_task.h"

// void readFileTask(string path_, MatrixNode *refMatx, ListTask *tsk){
void readFileTask(string path_, ListTask *tsk){
    cout<<" >> Path File: "<<path_<<endl;

    string myText; //For lines of the file
    ifstream myFile(path_); // Open the file
    bool init = true;
    string indexHeaders = "";
    // string texto[] = new string[5];
    // int countTest = 1;
    while(getline(myFile, myText)){
        // cout<<myText<<endl;
        if (myText != ""){
            if (init == true){
                init = false;
                indexHeaders = setIndexHeadersTask(myText, ",");
            }else{
                splitTextTask(myText, ",", indexHeaders, tsk);
                // cout <<countTest<<" ------------------------" << endl;
                // countTest++;
            }
        }
    }

    myFile.close();
    tsk->insertRowMajor();
    // delete [] indexHeaders;
}

void splitTextTask(string text_, string pattern_, string indx_, ListTask *tsk){
    size_t pos = 0;
    string captura;
    string taskData[9];
    int count = 0;
    while ((pos = text_.find(pattern_)) != string::npos) { //Evalua y captura la posicion del patron buscado
        captura = text_.substr(0, pos); //Obtiene el texto entre el inicio de cadena y el la posición capturada
        // cout << captura << endl;
        taskData[count] = captura; //Agrega a la lista temporal el valor capturado/obtenido
        text_.erase(0, pos + pattern_.length()); // Elimina de la cadena el texto entre el inicio de la cadena hasta la posición del patrón mas la longitud del patron
        count++; //Aumento el contador
    }
    taskData[count] = text_; //dado que el texto restante no posee el "delimitador" al final, este utlimo texto se almacena fuera del ciclo
    
    //Funcion que castea a enteron un string
    int listPos[9] = {3,4,5,6,7,2,8,0,1};
    // for (int i = 0; i < 9; i++){
    //     listPos[i] = indx_[i]-'0'; // Obtiene el orden de indice para enviar los datos a su parametro correcto
    // }
    
    string msg = "";
    string msgConsole = "";

    if (!validaNumero(taskData[listPos[0]])){
        msg += "\\nEl carnet posee valores no numericos ("+taskData[listPos[0]]+")";
        msgConsole += "\n\t\tEl carnet posee valores no numericos ("+taskData[listPos[0]]+")";
        taskData[listPos[0]] = "0";
    } else if (!validaLongitud(taskData[listPos[0]], 9)){
        msg += "\\nEl carnet no tiene la cantidad de digitos esperados ("+taskData[listPos[0]]+")";
        msgConsole += "\n\t\tEl carnet no tiene la cantidad de digitos esperados ("+taskData[listPos[0]]+")";
        // taskData[listPos[0]] = "0";
    } else if (!tsk->existCardNumber(stoi(taskData[listPos[0]]))){
        msg += "\\nEl carnet no esta registrado ("+taskData[listPos[0]]+")";
        msgConsole += "\n\t\tEl carnet no esta registrado ("+taskData[listPos[0]]+")";
        // taskData[listPos[0]] = "0";
    }

    if (!validaNumero(taskData[listPos[5]])){
        msg += "\\nError de hora, se esperaba un valor numerico ("+taskData[listPos[5]]+")";
        msgConsole += "\n\t\tError de hora, se esperaba un valor numerico ("+taskData[listPos[5]]+")";
        taskData[listPos[5]] = "0";
    } else if (!validaHora(stoi(taskData[listPos[5]]))){
        msg += "\\nLa hora esta fuera del horario permitido ("+taskData[listPos[5]]+")";
        msgConsole += "\n\t\tLa hora esta fuera del horario permitido ("+taskData[listPos[5]]+")";
        // taskData[listPos[5]] = "0";
    }

    if (!validaNumero(taskData[listPos[7]])){
        msg += "\\nError de mes, se esperaba un valor numerico ("+taskData[listPos[7]]+")";
        msgConsole += "\n\t\tError de mes, se esperaba un valor numerico ("+taskData[listPos[7]]+")";
        taskData[listPos[7]] = "0";
    } else if (!validaMes(stoi(taskData[listPos[7]]))){
        msg += "\\nEl mes se encuentra fuera del rango permitido ("+taskData[listPos[7]]+")";
        msgConsole += "\n\t\tEl mes se encuentra fuera del rango permitido ("+taskData[listPos[7]]+")";
        // taskData[listPos[7]] = "0";
    }

    if (!validaNumero(taskData[listPos[8]])){
        msg += "\\nError de dia, se esperaba un valor numerico ("+taskData[listPos[8]]+")";
        msgConsole += "\n\t\tError de dia, se esperaba un valor numerico ("+taskData[listPos[8]]+")";
        taskData[listPos[8]] = "0";
    } else if (!validaDia(stoi(taskData[listPos[8]]))){
        msg += "\\nEl dia se encuentra fuera del rango permitido ("+taskData[listPos[8]]+")";
        msgConsole += "\n\t\tEl dia se encuentra fuera del rango permitido ("+taskData[listPos[8]]+")";
        // taskData[listPos[8]] = "0";
    }
    
    if (!validaFecha(taskData[listPos[4]])){
        msg += "\\nLa fecha no es valida ("+taskData[listPos[4]]+")";
        msgConsole += "\n\t\tLa fecha no es valida ("+taskData[listPos[4]]+")";
        // taskData[listPos[4]] = "";
    } else if (!tsk->isTheDateAvaible(stoi(taskData[listPos[7]])-7, stoi(taskData[listPos[8]])-1, stoi(taskData[listPos[5]])-8)){
        msg += "\\nYa hay una tarea en la misma fecha y hora ("+taskData[listPos[4]]+" "+taskData[listPos[5]]+":00)";
        msgConsole += "\n\t\tYa hay una tarea en la misma fecha y hora ("+taskData[listPos[4]]+" "+taskData[listPos[5]]+":00)";
        // taskData[listPos[4]] = "";
        // taskData[listPos[5]] = "0";
        // taskData[listPos[7]] = "0";
        // taskData[listPos[8]] = "0";
    }

    if (!validaEstado(taskData[listPos[6]])){
        msg += "\\nEl estado no es valido ("+taskData[listPos[6]]+")";
        msgConsole += "\n\t\tEl estado no es valido ("+taskData[listPos[6]]+")";
        // taskData[listPos[6]] = "";
    }

    if (msg == "") {
        // int inxTest = (stoi(taskData[listPos[5]])-8) + 9 * ((stoi(taskData[listPos[8]])-1) + 30 * (stoi(taskData[listPos[7]])-7));
        // cout<<"Normalito - "<<inxTest+1<<endl;
        tsk->insertTaskArray(stoi(taskData[listPos[7]])-7, stoi(taskData[listPos[8]])-1, stoi(taskData[listPos[5]])-8, stoi(taskData[listPos[0]]), taskData[listPos[1]], taskData[listPos[2]], taskData[listPos[3]], taskData[listPos[4]], stoi(taskData[listPos[5]]), taskData[listPos[6]], stoi(taskData[listPos[7]]), stoi(taskData[listPos[8]]));
    } else {
        // cout<<"Uno se va a errores"<<endl;
        tsk->insertErrorTask(stoi(taskData[listPos[0]]), taskData[listPos[1]], taskData[listPos[2]], taskData[listPos[3]], taskData[listPos[4]], stoi(taskData[listPos[5]]), taskData[listPos[6]], stoi(taskData[listPos[7]]), stoi(taskData[listPos[8]]), msg, msgConsole);
    }
    // Tasks->showListContent();
    // system("pause");
}

string setIndexHeadersTask(string text_, string pattern_){
    int *iHT_ = new int[9];
    string iHT = "";
    size_t pos = 0;
    string token;
    int index = 0;
    while ((pos = text_.find(pattern_)) != string::npos) {
        token = text_.substr(0, pos);
        int i = getIndexAssignTH(token);
        iHT_[i] = index;
        // cout << token << endl;
        text_.erase(0, pos + pattern_.length());
        index ++;
    }
    // cout << text_ << endl;
    int i = getIndexAssignTH(text_);
    iHT_[i] = index;
    for (int i = 0; i<9; i++){
        iHT += to_string(iHT_[i]);
    }
    return iHT;
}

int getIndexAssignTH(string name_){
    for (int i = 0; i < 9; i++){
        if (name_ == TaskFormat[i]){
            return i;
        }
    }
    return -1;
}
