#include <iostream>
#include <windows.h>
#include <string>

#include "../headers/file_reader.h"
#include "../headers/list_student.h"
#include "../headers/list_task.h"
#include "../headers/cola.h"

using namespace std;

static Cola *errors = new Cola();
static ListTask *tasks = new ListTask();
static ListStudent *students = new ListStudent();

void menu();
void mySwitch(int);
int getIntegerInput();
string getExistFileURLInput();

int main(){
    students->setColaRef(errors);
    // SetConsoleOutputCP(CP_UTF8);
    
    // tasks->insertTask(201709020, "Tarea de matematica", "Primer tarea unidad 1", "Matematica Aplicada 1", "2021/08/11", "23", "Pendiente");

    // tasks->showListContent();

    // string inputUser;
    // // cin.ignore(); // 
    // getline(cin, inputUser);  // input de una cadena con espacios
    // // cin >> inputUser;      // Input de una cadena sin espacios
    // cout << inputUser << endl;

    // system("pause");

    menu();

    return 0;
}

void menu(){
    while (true){
        cout<<"\n-------------------------------------------------------"<<endl;
        cout<<"-------------- S M A R T - C L A S S ------------------"<<endl;
        cout<<"-------------------------------------------------------"<<endl<<endl;
        cout<<"  [1] Cargar masiva - Usuarios\n";
        cout<<"  [2] Cargar masiva - Tareas\n"; 
        cout<<"  [3] Operaciones Manuales (Usuarios)\n";
        cout<<"  [4] Operaciones Manuales (Tareas)\n";
        cout<<"  [5] Reportes\n  [6] Salir\n"<<endl;
        cout<<"   >> Elija una opcion: ";
        int opcion;
        opcion = getIntegerInput();
        if (opcion != -1){
            if (opcion > 0 && opcion < 6){
                cout<<endl;
                mySwitch(opcion);
                system("pause");
                system("cls");
            } else if (opcion == 6){
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
            break;
        case 3: // Ingreso Manual - Usuarios
            cout<<"     1 - Agregar un nuevo estudiante"<<endl;
            cout<<"     2 - Editar registro de estudiante"<<endl;
            cout<<"     3 - Eliminar registro de estudiante"<<endl;
            cout<<"     4 - Regresar al menu principal"<<endl;
            do {
                cout<<"     >> Ingresa una opcion: ";
                opt = getIntegerInput();
                if (opt < 1 && opt > 4){
                    cout<<"      --> Error: Debe elegir un numero de opcion correcta";
                }
            } while (opt < 1 && opt > 4);
            
            if (opt == 1){
                students->insertStudentByConsole();
            } else if (opt == 2){
                students->editStudentData();
            } else if (opt == 3){
                students->deleteStudent();
            }
            break;
        case 4: // Ingreso Manual - Tareas
            break;
        case 5:
            // students->showListContent();
            students->graficar();
            errors->graficar();
            break;
    }
}

int getIntegerInput(){
    int value = -1;
    string valueInput;
    try {
        // cin.ignore();
        getline(cin, valueInput);
        for (int i = 0; i < valueInput.length(); i++){
            if (!isdigit(valueInput[i])){
                return value;
            }
        }
        value = std::stoi(valueInput);        
    }
    catch(const std::exception& e) {
        std::cerr << e.what() << '\n';
    }
    return value;
}

bool fileExists( std::string const& name ) {
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
