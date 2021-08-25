#include "../headers/list_student.h"

ListStudent::ListStudent(){
    this->head = NULL;
    this->refError = NULL;
    this->size = 0;
    this->generates = 1;
}

string ListStudent::getInputDPI(){
    string dpi_ = "";
    do {
        // dpi_= "";
        cout<<"   >> Ingresa el numero de DPI del estudiante: ";
        getline(cin, dpi_);
        if (dpi_ == ""){
            // cout<<"     --> Se ha anulado la operación"<<endl;
            return dpi_;
        }
    } while (!validaLongitud(dpi_, 13) || !validaNumero(dpi_));
    
    return dpi_;
}

void ListStudent::setColaRef(Cola *refError_){
    this->refError = refError_;
}

bool ListStudent::isEmpty(){
    return this->head == NULL;
}
int ListStudent::getSize(){
    return this->size;
}

void ListStudent::setSize(string type_){
    if (type_ == "increase"){
        this->size++;
    } else {
        this->size--;
    }
}

void ListStudent::insertStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_){
    NodeStudent *newNode = new NodeStudent(cardNumber_, dpi_, name_, career_, email_, password_, credits_, age_);
    
    if (isEmpty()){
        //Self-Reference
        newNode->setNext(newNode);
        newNode->setPrev(newNode);
        //Asign newNode as head pointer
        this->head = newNode;
    } else {
        NodeStudent *aux = this->head->getPrev();
        aux->setNext(newNode);
        newNode->setPrev(aux);
        newNode->setNext(this->head);
        this->head->setPrev(newNode);
    }
    setSize("increase");
    // this->size++;
}

void ListStudent::insertErrorStudent(int cardNumber_, string dpi_, string name_, string career_, string email_, string password_, int credits_, int age_, string infoErr_, string infoErr_console_){
    NodeStudent *newNode = new NodeStudent(cardNumber_, dpi_, name_, career_, email_, password_, credits_, age_);
    this->refError->queue(newNode, infoErr_, infoErr_console_);
}

void ListStudent::showListContent(){
    cout<<"--------------- LISTA DE ESTUDIANTES ----------------"<<endl;
    if (this->size > 0){
        int counter = 0;
        while (counter < this->size){
            counter++;
            this->head->showInfo();
            cout<<"-----------------------------------------------------"<<endl;
            this->head = this->head->getNext();
        }   
    } else {
        cout<<"              - SIN REGISTROS - "<< endl;
        cout<<endl;
    }
}

void ListStudent::deleteStudent(){
    string dpi_ = getInputDPI();
    if (dpi_ == ""){
        cout<<"    --> Se ha cancelado la operación"<<endl;
        return;
    }

    if (searchStudentByDPI(dpi_)){
        NodeStudent *aux = this->head;
        while (aux->getDPI() != dpi_){
            aux = aux->getNext();
        }
        string confirm = "";
        cout<<"    >> Aviso: Esta seguro que desea eliminar los registros de "<<aux->getCardNumber()<<" (Y/N)?: ";
        getline(cin, confirm);
        if (confirm == "Y" || confirm == "y"){
            if (aux == head){
                if (this->size == 1){
                    this->head = NULL;
                } else {
                    this->head = this->head->getNext();
                    this->head->setPrev(aux->getPrev());
                    aux = NULL;
                    aux = this->head->getPrev();
                    aux->setNext(this->head);
                }
            } else {
                aux = aux->getNext();
                aux->setPrev(aux->getPrev()->getPrev());
                aux->getPrev()->setNext(aux);
            }
            this->size--;
            cout<<"     --> Se ha completado la operacion"<<endl;
        } else {
            cout<<"     --> Se ha anulado la operacion"<<endl;
        }
    } else {
        cout<<"   >> Error: No hubo coincidencia del DPI ingresado"<<endl;
    }
}

bool ListStudent::searchStudentByDPI(string dpi_){
    if (this->size > 0){
        NodeStudent *aux = this->head;
        do {
            if (aux->getDPI() == dpi_){
                return true;
            }
            aux = aux->getNext();
        } while (aux != this->head);
    }
    return false;
}

bool ListStudent::searchStudentByCardNumber(int cardNumber_){
    if (this->size > 0){
        NodeStudent *aux = this->head;
        do {
            if (aux->getCardNumber() == cardNumber_){
                return true;
            }
            aux = aux->getNext();
        } while (aux != this->head);
        
    }
    return false;
}

void ListStudent::insertStudentByConsole(){
    cout<<"\n  ------ Agregar Estudiante -----------"<<endl;
    cout<<"  Nota: Para cancelar la operacion, deje un campo vacio y presione enter"<<endl;
    string data[8] = {"", "", "", "", "", "", "", ""};
    bool init = true;
    for (int i=0; i<8; i++){
        bool isOk = false;
        while (!isOk) {
            switch (i) {
                case 0:
                    cout<<"     >> Ingresa el numero de carnet: ";
                    break;
                case 1:
                    cout<<"     >> Ingresa el numero de DPI: ";
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
            }
            string input = "";
            // if (init){
            //     cin.ignore();
            //     init = false;
            // }
            getline(cin, input);
            if (input != ""){
                switch (i) {
                    case 0: //Carnet
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaLongitud(input, 9)){
                            cout<<"       --> Error: La longitud del carnet es distinta de la esperada"<<endl;
                        } else if (searchStudentByCardNumber(stoi(input))){
                            cout<<"       --> Error: El carnet ingresado ya esta registrado"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 1:  // DPI
                        if (!validaNumero(input)){
                            cout<<"       --> Error: La entrada contiene caracteres no numericos"<<endl;
                        } else if (!validaLongitud(input, 13)){
                            cout<<"       --> Error: La longitud del carnet es distinta de la esperada"<<endl;
                        } else if (searchStudentByDPI(input)){
                            cout<<"       --> Error: El numero de DPI ya esta registrado"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 4:  // Email
                        if (!validaCorreo(input)){
                            cout<<"       --> Error: Debe ingresar un correo valido"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 6:  // Credits
                        if (!validaNumero(input)){
                            cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    case 7: // Age
                        if (!validaNumero(input)){
                            cout<<"       --> Error: Debe ingresar un valor numerico"<<endl;
                        } else {
                            data[i] = input;
                            isOk = true;
                        }
                        break;
                    default:  // Name, Carrer, Password
                        data[i] = input;
                        isOk = true;
                        break;
                }
            }else{
                cout<<"     --> Se ha anulado la operacion"<<endl;
                return;
            }
        }
    }
    insertStudent(stoi(data[0]), data[1], data[2], data[3], data[4], data[5], stoi(data[6]), stoi(data[7]));
    cout<<"\n   >> Se ha guardado el registro"<<endl;
}

void ListStudent::editStudentData(){
    string dpi_ = getInputDPI();
    if (dpi_ == ""){
        cout<<"    --> Se ha cancelado la operacion"<<endl;
        return;
    }

    if (searchStudentByDPI(dpi_)){
        NodeStudent *aux = this->head;
        while (aux->getDPI() != dpi_){
            aux = aux->getNext();
        }
        bool edit = true;
        string option = "";
        while (edit) {
            cout<<"\n  --------- Editar Estudiante -----------"<<endl;
            cout<<"   Nota: Para cancelar una modificacion, deje el campo vacio y presione enter"<<endl;
            cout<<"\n   1 - Carnet (No editable): "<<aux->getCardNumber()<<endl;
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
                }else if (stoi(option) == 1){
                    cout<<"     --> Error: La opcion no es editable"<<endl;
                    option = " ";
                }else if (stoi(option) > 9 || stoi(option) < 0){
                    cout<<"     --> Error: Debe seleccionar una opción valida (2-8)"<<endl;
                    option += "error";
                }
            } while (!validaNumero(option));
            

            switch (stoi(option)-1) {
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
                cout<<"     --> Se ha anulado la operacion"<<endl;
                return;
            }
        }
        // cout<<"\n   >> Se han guardado los cambios"<<endl;
    } else {
        cout<<"   >> Error: No hubo coincidencia del DPI ingresado"<<endl;
    }

}

void ListStudent::graficar(){
    int limit = this->size;
    string commandG = "dot -Tpng students.dot -o statusStudents"+to_string(this->generates)+".png";
    string commandO = "start statusStudents"+to_string(this->generates)+".png";
    if (isEmpty()){
        cout<<"\n     --- NO HAY REGISTROS PARA GRAFICAR ---"<<endl;
    }else{
        ofstream file;
        file.open("students.dot");
        cout<<"\n    - Generando students.dot -"<<endl;
        
        file<<"digraph D {\n";
        file<<"\trankdir=LR\n";
        // file<<"\tgraph [dpi = 200];\n";
        file<<"\tnodo_inicio[shape=point];";
        
        NodeStudent *aux = this->head;
        int count = 0;

        do{
            string formatInfo = "DPI: " + aux->getDPI() 
            + "\\nCarnet: " + to_string(aux->getCardNumber())
            + "\\nNombre: " + aux->getName();
            
            file<<"\tnodo_"<<count<<"[shape=record,label=\"";
            file<<formatInfo;
            file<<"\"];\n";
            
            aux = aux->getNext();
            count++;
        } while (aux != head);

        file<<"\n";
        file<<"\tnodo_inicio->nodo_0[label=\"Primero\"]\n";

        if (limit == 1){
            file<<"\tnodo_0->nodo_0\n";
            file<<"\tnodo_0->nodo_0\n";
        }else{
            for (int i = 1; i < limit; i++){
                file<<"\tnodo_"<<i-1<<" ";
                file<<"-> ";
                file<<"nodo_"<<i<<";\n";

                file<<"\tnodo_"<<i<<" ";
                file<<"-> ";
                file<<"nodo_"<<i-1<<"\n";
            }
            file<<"\tnodo_"<<limit-1<<" ";
            file<<"-> nodo_0\n";

            file<<"\tnodo_0";
            file<<"->nodo_"<<limit-1<<"\n";
        }
        file<<"}\n";
        file.close();
        
        system(commandG.c_str());
        // system("pause");
        system(commandO.c_str());
        this->generates++;
    }
}

void ListStudent::writeSpecialFile(){
    ofstream specialfile_;
    specialfile_.open("specialFile.txt", std::ios::app);
    NodeStudent *aux = this->head;
    do{
        specialfile_<<"\t¿element type = \"user\"?\n";
        specialfile_<<"\t\t¿item Carnet = \""+to_string(aux->getCardNumber())+"\" $?\n";
        specialfile_<<"\t\t¿item DPI = \""+aux->getDPI()+"\" $?\n";
        specialfile_<<"\t\t¿item Nombre = \""+aux->getName()+"\" $?\n";
        specialfile_<<"\t\t¿item Carrera = \""+aux->getCareer()+"\" $?\n";
        specialfile_<<"\t\t¿item Email = \""+aux->getEmail()+"\" $?\n";
        specialfile_<<"\t\t¿item Password = \""+aux->getPassword()+"\" $?\n";
        specialfile_<<"\t\t¿item Creditos = \""+to_string(aux->getCredits())+"\" $?\n";
        specialfile_<<"\t\t¿item Edad = \""+to_string(aux->getAge())+"\" $?\n";
        specialfile_<<"\t¿$element?\n";
        aux = aux->getNext();
    } while (aux != this->head);
    specialfile_.close();
}