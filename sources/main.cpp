#include <iostream>
#include <windows.h>
#include <string>

#include "../headers/file_reader.h"
#include "../headers/file_reader_task.h"
#include "../headers/list_student.h"
#include "../headers/list_task.h"
#include "../headers/cola.h"
// #include "../headers/validations.h"

// using namespace std;

static Cola *errors = new Cola();
static ListTask *tasks = new ListTask();
static ListStudent *students = new ListStudent();

void menu();
void mySwitch(int);
int getIntegerInput();
string getExistFileURLInput();
void fixErrors();
void generateFile();

int main(){
    system("cls");
    students->setColaRef(errors);
    tasks->setColaRef(errors);
    tasks->setStudentRef(students);
    // errors->setRefStudent(students);
    // errors->setRefTask(tasks);

    // SetConsoleOutputCP(CP_UTF8);
    menu();

    return 0;
}

void menu(){
    while (true){
        cout<<"\n-------------------------------------------------------"<<endl;
        cout<<"-------------- S M A R T - C L A S S ------------------"<<endl;
        cout<<"-------------------------------------------------------"<<endl<<endl;
        cout<<"  [1] Cargar archivo - Usuarios\n";
        cout<<"  [2] Cargar archivo - Tareas\n"; 
        cout<<"  [3] Operaciones Manuales (Usuarios)\n";
        cout<<"  [4] Operaciones Manuales (Tareas)\n";
        cout<<"  [5] Corregir errores en cola\n";
        cout<<"  [6] Reportes\n  [7] Salir\n"<<endl;
        cout<<"   >> Elija una opcion: ";
        int opcion;
        opcion = getIntegerInput();
        if (opcion != -1){
            if (opcion > 0 && opcion < 7){
                cout<<endl;
                mySwitch(opcion);
                system("pause");
                system("cls");
            } else if (opcion == 7){
                cout<<"   >> Finalizando programa"<<endl;
                system("pause");
                break;
            } else {
                cout<<"   >> Error: Opcion invalida\n"<<endl;
                system("pause");
                system("cls");
            }
        } else {
                cout<<"   >> Error: Debe ingresar un valor numerico\n"<<endl;
                system("pause");
                system("cls");
        }
        
    }
}

void mySwitch(int opcion){
    string param01;
    string confirm_ = "";
    int edad_ = 0;
    int opt = 0;
    switch (opcion){
        case 1:
            cout<<"   >> Ingresa el la ruta del archivo: ";
            // cin>>nombre_;
            param01 = getExistFileURLInput();
            if (param01 != ""){
                readFileStudent(param01, students);
            }
            break;
        case 2: // Cargar masiva - Tareas
            cout<<"   >> Ingresa el la ruta del archivo: ";
            // cin>>nombre_;
            param01 = getExistFileURLInput();
            if (param01 != ""){
                readFileTask(param01, tasks);
            }
            break;
        case 3: // Ingreso Manual - Usuarios
            cout<<"     1 - Agregar un nuevo estudiante"<<endl;
            cout<<"     2 - Editar registro de estudiante"<<endl;
            cout<<"     3 - Eliminar registro de estudiante"<<endl;
            cout<<"     4 - Regresar al menu principal"<<endl;
            do {
                cout<<"     >> Ingresa una opcion: ";
                opt = getIntegerInput();
                if (opt < 1 || opt > 4){
                    cout<<"      --> Error: Debe elegir un numero de opcion correcta"<<endl;
                }
            } while (opt < 1 || opt > 4);
            
            if (opt == 1){
                students->insertStudentByConsole();
            } else if (opt == 2){
                students->editStudentData();
            } else if (opt == 3){
                students->deleteStudent();
            }
            break;
        case 4: // Ingreso Manual - Tareas
            cout<<"     1 - Agregar una nueva tarea"<<endl;
            cout<<"     2 - Editar tarea"<<endl;
            cout<<"     3 - Eliminar tarea"<<endl;
            cout<<"     4 - Regresar al menu principal"<<endl;
            do {
                cout<<"     >> Ingresa una opcion: ";
                opt = getIntegerInput();
                if (opt < 1 || opt > 4){
                    cout<<"      --> Error: Debe elegir un numero de opcion correcta"<<endl;;
                }
            } while (opt < 1 || opt > 4);
            
            if (opt == 1){
                tasks->insertTaskByConsole();
            } else if (opt == 2){
                tasks->editTaskData();
            } else if (opt == 3){
                tasks->deleteTask();
            }
            break;
        case 5:  // Correccion de errores
            if (errors->getSize() == 0){
                cout<<"      >> Info: La cola de errores esta vacia "<<endl;
                return;
            }
            cout<<"      >> Desea iniciar con la correccion de errores (Y/N)? ";
            getline(cin, confirm_);
            if (confirm_ != "" && (confirm_ == "Y" || confirm_ == "y")){
                // cout<<"Demole pues"<<endl;
                fixErrors();
            } else {
                cout<<"      >> Info: Recuerde que la lista de errores debe estar vacia, para generar el archivo de salida"<<endl;
            }
            break;
        case 6:  // Reportes
            cout<<"\n     1 - Reporte lista estudiantes"<<endl;
            cout<<"     2 - Reporte lista tareas (linealizada)"<<endl;
            cout<<"     3 - Busqueda de tarea"<<endl;
            cout<<"     4 - Calculo de posicion"<<endl;
            cout<<"     5 - Cola de errores"<<endl;
            cout<<"     6 - Generar codigo de salida"<<endl;
            cout<<"     7 - Regresar al menu principal"<<endl;
            do {
                cout<<"     >> Ingresa una opcion: ";
                opt = getIntegerInput();
                if (opt < 1 || opt > 7){
                    cout<<"      --> Error: Debe elegir un numero de opcion correcta"<<endl;;
                }
            } while (opt < 1 || opt > 7);
            
            if (opt == 1){
                students->graficar();
            } else if (opt == 2){
                tasks->graficar();
            } else if (opt == 3){
                tasks->reportTask();
            } else if (opt == 4){
                tasks->calculatePosition();
            } else if (opt == 5){
                errors->graficar();
            } else if (opt == 6){
                if (errors->getSize() == 0){
                    //generar archivo de salida
                    generateFile();
                } else {
                    cout<<"    >> Info: El reporte no se puede generar porque hay ("<<errors->getSize()<<") errores en cola"<<endl;
                }
                // Not implemented
            }
            // tasks->showMatrixContent();
            break;
    }
}

int getIntegerInput(){
    int value = -1;
    string valueInput;
    // cin.ignore();
    getline(cin, valueInput);
    if (valueInput == ""){
        return value;
    }else{
        for (int i = 0; i < valueInput.length(); i++){
            if (!isdigit(valueInput[i])){
                return value;
            }
        }
    }
    value = std::stoi(valueInput);        
    return value;
}

bool fileExists(string const& name ) {
    ifstream f(name.c_str());
    return f.good();
}

string getExistFileURLInput(){
    string valueInput = "";
    try {
        // cin.ignore();
        getline(cin, valueInput);
        if (fileExists(valueInput)){
            return valueInput;
        }else{
            cout<<"   >> Error: El archivo no existe"<<endl;
            return "";
        }
    }
    catch(const std::exception& e) {
        std::cerr << e.what() << '\n';
    }
}

void fixStudent(NodoCola *toFix_){
    NodeStudent *aux = toFix_->getErrStudent();
    bool edit = true;
    string option = "";
    while (edit) {
        toFix_->showInfo();
        cout<<"\n  --------- Editar Estudiante -----------"<<endl;
        cout<<"   Nota: Para cancelar una modificacion, deje el campo vacio y presione enter"<<endl;
        cout<<"\n   1 - Carnet (Actual):      "<<aux->getCardNumber()<<endl;
        cout<<"   2 - DPI (Actual):         "<<aux->getDPI()<<endl;
        cout<<"   3 - Nombre (Actual):      "<<aux->getName()<<endl;
        cout<<"   4 - Carrera (Actual):     "<<aux->getCareer()<<endl;
        cout<<"   5 - Correo (Actual):      "<<aux->getEmail()<<endl;
        cout<<"   6 - Contrasenia (Actual): "<<aux->getPassword()<<endl;
        cout<<"   7 - Creditos (Actual):    "<<aux->getCredits()<<endl;
        cout<<"   8 - Edad (Actual):        "<<aux->getAge()<<endl;
        cout<<"   9 - Finalizar edicion"<<endl;
        do
        {
            option = "";
            cout<<"   >> Selecciona una opcion: ";
            getline(cin, option);
            if (option == ""){
                cout<<"     --> Error: Debe seleccionar una opcion"<<endl;
                option = "x";
            } else if (!validaNumero(option)){
                cout<<"     --> Error: La opcion debe ser numerica"<<endl;
            } else if (!validaLongitud(option, 1)){
                cout<<"     --> Error: Opcion invalida"<<endl;
                option += "error";
            }else if (stoi(option) > 9 || stoi(option) < 0){
                cout<<"     --> Error: Debe seleccionar una opción valida (2-8)"<<endl;
                option += "error";
            }
        } while (!validaNumero(option));

        switch (stoi(option)-1) {
            case 0:
                cout<<"     >> Ingresa el carnet: ";
                break;
            case 1:
                cout<<"     >> Ingresa el DPI: ";
                break;
            case 2:
                cout<<"     >> Ingresa el nombre: ";
                break;
            case 3:
                cout<<"     >> Ingresa la carrera: ";
                break;
            case 4:
                cout<<"     >> Ingresa el correo: ";
                break;
            case 5:
                cout<<"     >> Ingresa la contrasenia: ";
                break;
            case 6:
                cout<<"     >> Ingresa el numero de creditos: ";
                break;
            case 7:
                cout<<"     >> Ingresa la edad: ";
                break;
            case 8:
                return;
        }
        
        string input = "";
        getline(cin, input);
        if (input != ""){
            switch (stoi(option)-1) {
                case 0:  // Carnet
                    if (!validaNumero(input)){
                        cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                    } else if (!validaLongitud(input, 9)) {
                        cout<<"       --> Error: Se esperanba una longitud de 9 digitos"<<endl;
                    } else {
                        aux->setCardNumber(stoi(input));
                    }
                    break;
                case 1:  // DPI
                    if (!validaNumero(input)){
                        cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                    } else if (!validaLongitud(input, 13)) {
                        cout<<"       --> Error: Se esperanba una longitud de 13 digitos"<<endl;
                    } else {
                        aux->setDPI(input);
                    }
                    break;
                case 2:  // Name
                    aux->setName(input);
                    break;
                case 3:  // Career
                    aux->setCareer(input);
                    break;
                case 4:  // Email
                    if (!validaCorreo(input)){
                        cout<<"       --> Error: Debe ingresar un correo valido"<<endl;
                    } else {
                        aux->setEmail(input);
                    }
                    break;
                case 5:  // Password
                    aux->setPassword(input);
                    break;
                case 6:  // Credits
                    if (!validaNumero(input)){
                        cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                    } else {
                        aux->setCredits(stoi(input));
                    }
                    break;
                case 7: // Age
                    if (!validaNumero(input)){
                        cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                    } else {
                        aux->setAge(stoi(input));
                    }
                    break;
                case 8:  // Finalizar
                    edit = false;
                    break;
            }
        }else{
            cout<<"     --> Debe ingresar algun valor"<<endl;
        }
        system("pause");
    }
}
void fixTask(NodoCola *toFix_){
    NodeTask *aux = toFix_->getErrTask();
    bool edit = true;
    string option = "";
    while (edit) {
        toFix_->showInfo();
        cout<<"\n  --------- Editar Tarea -----------"<<endl;
        cout<<"   Nota: Para cancelar una modificacion, deje el campo vacio y presione enter"<<endl;
        cout<<"\n         -- ID :                 "<<aux->getID()<<endl;
        cout<<"   1 - Carnet (Actual):          "<<aux->getCardNumber()<<endl;
        cout<<"   2 - Nombre de tarea (Actual): "<<aux->getTaskName()<<endl;
        cout<<"   3 - Descripcion (Actual):     "<<aux->getTaskDesc()<<endl;
        cout<<"   4 - Materia (Actual):         "<<aux->getCourse()<<endl;
        cout<<"   5 - Fecha (Actual):           "<<aux->getDate()<<endl;
        cout<<"   6 - Hora (Actual):            "<<aux->getHour()<<":00"<<endl;
        cout<<"   7 - Estado (Actual):          "<<aux->getStatus()<<endl;
        cout<<"   8 - Finalizar edicion"<<endl;
        do
        {
            option = "";
            cout<<"   >> Selecciona una opcion: ";
            getline(cin, option);
            if (option == ""){
                cout<<"     --> Error: Debe seleccionar una opcion"<<endl;
                option = "x";
            } else if (!validaNumero(option)){
                cout<<"     --> Error: La opcion debe ser numerica"<<endl;
            } else if (!validaLongitud(option, 1)){
                cout<<"     --> Error: Opcion invalida"<<endl;
                option += "error";
            } else if (stoi(option) > 8 || stoi(option) < 1){
                cout<<"     --> Error: La opcion debe ser del rango de 1-8"<<endl;
                option += "error";
            }
        } while (!validaNumero(option));
        
        bool isOk = false;
        while (!isOk) {
            switch (stoi(option)-1) {
                case 0:
                    cout<<"     >> Ingresa el numero de carnet: ";
                    break;
                case 1:
                    cout<<"     >> Ingresa el nombre de la tarea: ";
                    break;
                case 2:
                    cout<<"     >> Ingresa la descripcion: ";
                    break;
                case 3:
                    cout<<"     >> Ingresa el curso: ";
                    break;
                case 4:
                    cout<<"     >> Ingresa la fecha (YYYY/MM/DD): ";
                    break;
                case 5:
                    cout<<"     >> Ingresa la hora (8 - 16): ";
                    break;
                case 6:
                    cout<<"     >> Ingresa el estado: ";
                    break;
                case 7:
                    return;
            }

            string input = "";
            getline(cin, input);
            if (input != ""){
                switch (stoi(option)-1) {
                    case 0: //Carnet
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaLongitud(input, 9)){
                            cout<<"       --> Error: La longitud del carnet es distinta de la esperada"<<endl;
                        } else if (!students->searchStudentByCardNumber(stoi(input))){
                            cout<<"       --> Error: El carnet ingresado no esta registrado"<<endl;
                        } else {
                            aux->setCardNumber(stoi(input));
                            isOk = true;
                        }
                        break;
                    case 1:  // Nombre Tarea
                        aux->setTaskName(input);
                        isOk = true;
                        break;
                    case 2:  // Desc. Tarea
                        aux->setTaskDesc(input);
                        isOk = true;
                        break;
                    case 3:  // Materia
                        aux->setCourse(input);
                        isOk = true;
                        break;
                    case 4:  // Fecha
                        if (!validaFecha(input)){
                            cout<<"       --> Error: Verifique que la fecha este correcta y se encuentre en el rango permitido"<<endl;
                        } else {
                            string month_ = getSeparateMonth(input);
                            string day_ = getSeparateDay(input);
                            int indx = (aux->getHour() - 8) + 9 * ( (stoi(day_) - 1) + 30 * (stoi(month_) - 7) );
                            // int indx = h + 9 * ( d + 30 * m );
                            if (aux->getDate() == input){
                                cout<<"       --> Info: Se ha ingresado la misma fecha registrada"<<endl;
                            } else if (!tasks->avaibleDateTask(indx)){
                                cout<<"       --> Error: En esta fecha y hora ya esta registrada una tarea"<<endl;
                            } else {
                                aux->setDate(input);
                                aux->setMonth(stoi(month_));
                                aux->setDay(stoi(day_));
                                // int id_ = aux->getID();
                                // //Inserto en la nueva "ubicación" de la tarea
                                // // insertTaskArray(stoi(month_)-7, stoi(day_)-1, aux->getHour()-8, aux->getCardNumber(), aux->getTaskName(), aux->getTaskDesc(), aux->getCourse(), input, aux->getHour(), aux->getStatus(), stoi(month_), stoi(day_));
                                // // insertTask(indx, aux->getCardNumber(), aux->getTaskName(), aux->getTaskDesc(), aux->getCourse(), input, aux->getHour(), aux->getStatus(), stoi(month_), stoi(day_));
                                // //Muevo mi auxiliar hacia la tarea insertada
                                // NodeTask *temp = this->head;
                                // while(temp != NULL){
                                //     if (temp->getID() == indx){
                                //         aux = temp;
                                //         break;
                                //     }
                                //     temp = temp->getNext();
                                // }
                                // deleteTaskFromEdit(id_);
                            }
                            isOk = true;
                        }
                        break;
                    case 5:  // Hora
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaHora(stoi(input))){
                            cout<<"       --> Error: La hora esta fuera del rango permitido"<<endl;
                        } else {
                            int indx = (stoi(input) - 8) + 9 * ( (aux->getDay() - 1) + 30 * (aux->getMonth() - 7) );
                            if (aux->getHour() == stoi(input)){
                                cout<<"       --> Info: Se ha ingresado la misma hora registrada"<<endl;
                            } else if (!tasks->avaibleDateTask(indx)){
                                cout<<"       --> Error: En esta fecha y hora ya esta registrada una tarea"<<endl;
                            } else {
                                aux->setHour(stoi(input));
                                // int id_ = aux->getID();
                                // //Inserto en la nueva "ubicación" de la tarea
                                // insertTaskArray(aux->getMonth()-7, aux->getDay()-1, stoi(input)-8, aux->getCardNumber(), aux->getTaskName(), aux->getTaskDesc(), aux->getCourse(), aux->getDate(), stoi(input), aux->getStatus(), aux->getMonth(), aux->getDay());
                                // insertTask(indx, aux->getCardNumber(), aux->getTaskName(), aux->getTaskDesc(), aux->getCourse(), aux->getDate(), stoi(input), aux->getStatus(), aux->getMonth(), aux->getDay());
                                // //Muevo mi auxiliar hacia la tarea insertada
                                // NodeTask *temp = this->head;
                                // while(temp != NULL){
                                //     if (temp->getID() == indx){
                                //         aux = temp;
                                //         break;
                                //     }
                                //     temp = temp->getNext();
                                // }
                                // deleteTaskFromEdit(id_);
                            }
                            isOk = true;
                        }
                        break;
                    case 6:  // Estado
                        if (!validaEstado(input)){
                            cout<<"       --> Error: El estado unicamente puede ser, Pendiente-Realizado-Cumplido-Incumplido"<<endl;
                        } else {
                            aux->setStatus(input);
                            isOk = true;
                        }
                        break;
                }
            }else{
                cout<<"     --> Se ha anulado la operacion"<<endl;
                isOk = true;
            }
        }
    }
}

//Preguntar si se desea iniciar con la correccion
void fixErrors(){
    bool fix = true;
    string mode = "";
    //Corregir datos de la cabeza
    NodoCola *toFix = errors->getNodeError();
    while (fix) {
        cout<<"\n  -------------- Correccion de errores ---------------"<<endl;
        cout<<"   Nota: Para cancelar la operacion, deje el campo vacio y presione enter"<<endl;
        toFix->showInfo();
        cout<<"\n\t1 - Insertar a su respectiva lista\n\t2 - Editar"<<endl;
        cout<<"\n\t\t >> Selecciona una opcion: ";
        getline(cin, mode);
        if (mode == ""){
            return;
        } else if (!validaNumero(mode)){
            cout<<"    -->  Se ha cancelado la operacion";
            return;
        } else if (stoi(mode) < 1 && stoi(mode) > 2){
            cout<<"    -->  Opcion invalida";
        } else {
            if (stoi(mode)==1){
                //Validar cambios a guardar
                if (toFix->getType() == "ESTUDIANTE"){
                    string msgUpdate = "";
                    string msgUpdateC = "";
                    NodeStudent *aux = toFix->getErrStudent();
                    if (aux->getCardNumber() == 0){
                        msgUpdate += "\\nNo hay un carnet valido";
                        msgUpdateC += "\n\t\tNo hay un carnet valido";
                    } else if (!validaLongitud(to_string(aux->getCardNumber()), 9)){
                        msgUpdate += "\\nEl carnet no tiene la cantidad de digitos esperados ("+to_string(aux->getCardNumber())+")";
                        msgUpdateC += "\n\t\tEl carnet no tiene la cantidad de digitos esperados ("+to_string(aux->getCardNumber())+")";
                    } else if (students->searchStudentByCardNumber(aux->getCardNumber())){
                        msgUpdate += "\\nEl carnet ya esta registrado ("+to_string(aux->getCardNumber())+")";
                        msgUpdateC += "\n\t\tEl carnet ya esta registrado ("+to_string(aux->getCardNumber())+")";
                    }
                    if (aux->getDPI() == "0"){
                        msgUpdate += "\\nNo hay un DPI valido";
                        msgUpdateC += "\n\t\tNo hay un DPI valido";
                    } else if (!validaLongitud(aux->getDPI(), 13)){
                        msgUpdate += "\\nEl DPI no tiene la cantidad de digitos esperados ("+aux->getDPI()+")";
                        msgUpdateC += "\n\t\tEl DPI no tiene la cantidad de digitos esperados ("+aux->getDPI()+")";
                    } else if (students->searchStudentByDPI(aux->getDPI())){
                        msgUpdate += "\\nEl DPI ya esta registrado ("+aux->getDPI()+")";
                        msgUpdateC += "\n\t\tEl DPI ya esta registrado ("+aux->getDPI()+")";
                    }
                    if (!validaCorreo(aux->getEmail())){
                        msgUpdate += "\\nEl correo posee un formato incorrecto ("+aux->getEmail()+")";
                        msgUpdateC += "\n\t\tEl correo posee un formato incorrecto ("+aux->getEmail()+")";
                    }
                    if (msgUpdate == ""){
                        students->insertStudent(aux->getCardNumber(), aux->getDPI(), aux->getName(), aux->getCareer(), aux->getEmail(), aux->getPassword(), aux->getCredits(), aux->getAge());
                        cout<<"    >> El registro del estudiante ha sido almacenada exitosamente"<<endl;
                        errors->dequeue();
                        system("pause");
                        if (errors->getSize() == 0){
                            cout<<"    >> La cola de errores esta vacia"<<endl;
                            return;
                        } else {
                            toFix = errors->getNodeError();
                        }
                    }else{
                        cout<<"    >> El registro contiene errores, verifique los datos, se ha actualizado la informacion del error"<<endl;
                        toFix->setInfoErr(msgUpdate);
                        toFix->setInfoErrConsole(msgUpdateC);
                        system("pause");
                    }
                } else {
                    string msgUpdate = "";
                    string msgUpdateC = "";
                    NodeTask *aux = toFix->getErrTask();
                    if (aux->getCardNumber() == 0){
                        msgUpdate += "\\nEl carnet no es valido ("+to_string(aux->getCardNumber())+")";
                        msgUpdateC += "\n\t\tEl carnet no es valido ("+to_string(aux->getCardNumber())+")";
                    } else if (!validaLongitud(to_string(aux->getCardNumber()), 9)){
                        msgUpdate += "\\nEl carnet no tiene la cantidad de digitos esperados ("+to_string(aux->getCardNumber())+")";
                        msgUpdateC += "\n\t\tEl carnet no tiene la cantidad de digitos esperados ("+to_string(aux->getCardNumber())+")";
                    } else if (!tasks->existCardNumber(aux->getCardNumber())){
                        msgUpdate += "\\nEl carnet no esta registrado ("+to_string(aux->getCardNumber())+")";
                        msgUpdateC += "\n\t\tEl carnet no esta registrado ("+to_string(aux->getCardNumber())+")";
                    }

                    if (aux->getHour()==0){
                        msgUpdate += "\\nError de hora, invalido ("+to_string(aux->getHour())+")";
                        msgUpdateC += "\n\t\tError de hora, invalido ("+to_string(aux->getHour())+")";
                    } else if (!validaHora(aux->getHour())){
                        msgUpdate += "\\nLa hora esta fuera del horario permitido ("+to_string(aux->getHour())+")";
                        msgUpdateC += "\n\t\tLa hora esta fuera del horario permitido ("+to_string(aux->getHour())+")";
                    }

                    if (aux->getMonth() == 0){
                        msgUpdate += "\\nError de mes, invalido ("+to_string(aux->getMonth())+")";
                        msgUpdateC += "\n\t\tError de mes, invalido ("+to_string(aux->getMonth())+")";
                    } else if (!validaMes(aux->getMonth())){
                        msgUpdate += "\\nEl mes se encuentra fuera del rango permitido ("+to_string(aux->getMonth())+")";
                        msgUpdateC += "\n\t\tEl mes se encuentra fuera del rango permitido ("+to_string(aux->getMonth())+")";
                    }

                    if (aux->getDay() == 0){
                        msgUpdate += "\\nError de dia, invalido ("+to_string(aux->getDay())+")";
                        msgUpdateC += "\n\t\tError de dia, invalido ("+to_string(aux->getDay())+")";
                    } else if (!validaDia(aux->getDay())){
                        msgUpdate += "\\nEl dia se encuentra fuera del rango permitido ("+to_string(aux->getDay())+")";
                        msgUpdateC += "\n\t\tEl dia se encuentra fuera del rango permitido ("+to_string(aux->getDay())+")";
                    }
                    
                    if (!validaFecha(aux->getDate())){
                        msgUpdate += "\\nLa fecha no es valida ("+aux->getDate()+")";
                        msgUpdateC += "\n\t\tLa fecha no es valida ("+aux->getDate()+")";
                    } else if (!tasks->isTheDateAvaible(aux->getMonth()-7, aux->getDay()-1, aux->getHour()-8)){
                        msgUpdate += "\\nYa hay una tarea en la misma fecha y hora ("+aux->getDate()+" "+to_string(aux->getHour())+":00)";
                        msgUpdateC += "\n\t\tYa hay una tarea en la misma fecha y hora ("+aux->getDate()+" "+to_string(aux->getHour())+":00)";
                    }

                    if (!validaEstado(aux->getStatus())){
                        msgUpdate += "\\nEl estado no es valido ("+aux->getStatus()+")";
                        msgUpdateC += "\n\t\tEl estado no es valido ("+aux->getStatus()+")";
                    }

                    if (msgUpdate == ""){
                        int index = (aux->getHour()-8) + (9 *( (aux->getDay()-1) + (30 * (aux->getMonth()-7)) ) );
                        tasks->insertTask(index, aux->getCardNumber(), aux->getTaskName(), aux->getTaskDesc(), aux->getCourse(), aux->getDate(), aux->getHour(), aux->getStatus(), aux->getMonth(), aux->getDay());
                        cout<<"    >> La tarea ha sido almacenada exitosamente"<<endl;
                        errors->dequeue();
                        system("pause");
                        if (errors->getSize() == 0){
                            cout<<"    >> La cola de errores esta vacia"<<endl;
                            return;
                        } else {
                            toFix = errors->getNodeError();
                        }
                    } else {
                        cout<<"    >> La tarea contiene errores, verifique los datos, se ha actualizado la informacion del error"<<endl;
                        toFix->setInfoErr(msgUpdate);
                        toFix->setInfoErrConsole(msgUpdateC);
                        system("pause");
                    }
                }
            } else {
                //Operar segun el tipo Estudiantes - Tareas
                if (toFix->getType() == "ESTUDIANTE"){
                    fixStudent(toFix);
                } else {
                    fixTask(toFix);
                }
            }
        }
    }
}

void generateFile(){
    ofstream specialfile;
    specialfile.open("specialFile.txt");
    specialfile<<"¿Elements?\n";
    specialfile.close();
    //Call writter of list student
    students->writeSpecialFile();
    tasks->writeSpecialFile();
    specialfile.open("specialFile.txt", std::ios::app);
    specialfile<<"¿$Elements?";
    specialfile.close();
    cout<<"    >> Archivo specialFile.txt generado exitosamente"<<endl;
}