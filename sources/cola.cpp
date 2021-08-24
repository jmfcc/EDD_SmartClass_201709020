#include "../headers/cola.h"

Cola::Cola(){
    this->cabeza = NULL;
    this->size = 0;
    this->countRegis = 0;
    this->generates = 1;
}

bool Cola::estaVacia(){
    return this->cabeza == NULL;
}
int Cola::getSize(){
    return this->size;
}

void Cola::queue(NodeStudent *errStudent_, string infoErr_){
    this->countRegis++;
    NodoCola *newNode = new NodoCola(errStudent_, infoErr_, this->countRegis);
    if (estaVacia()){
        this->cabeza = newNode;
    }else{
        NodoCola *aux = this->cabeza;
        while (aux->getAnterior() != NULL){
            aux = aux->getAnterior();
        }
        aux->setAnterior(newNode);
    }
    this->size++;
}

void Cola::queue(NodeTask *errTask_, string infoErr_){
    this->countRegis++;
    NodoCola *newNode = new NodoCola(errTask_, infoErr_, this->countRegis);
    if (estaVacia()){
        this->cabeza = newNode;
    }else{
        NodoCola *aux = this->cabeza;
        while (aux->getAnterior() != NULL){
            aux = aux->getAnterior();
        }
        aux->setAnterior(newNode);
    }
    this->size++;
}

void Cola::dequeue(){
    if (estaVacia()){
        cout<<"\n     --- LA COLA ESTA VACIA ---"<<endl;
    } else {
        this->cabeza = this->cabeza->getAnterior();
        this->size--;
    }
}
void Cola::graficar(){
    int limit = this->size;
    string commandG = "dot -Tpdf errores.dot -o statusErrors"+to_string(this->generates)+".pdf";
    string commandO = "start statusErrors"+to_string(this->generates)+".pdf";
    if (estaVacia()){
        cout<<"\n     --- NO HAY REGISTROS EN COLA DE ERRORES PARA GRAFICAR ---"<<endl;
    }else{
        ofstream file;
        file.open("errores.dot");
        cout<<"\n    - Generando errores.dot -"<<endl;
        
        file<<"digraph D {\n";
        file<<"\trankdir=LR\n";
        file<<"\tgraph [dpi = 300];\n";
        file<<"\tnodo_inicio[shape=point];";

        NodoCola *aux = this->cabeza;
        int count = 0;

        while (aux != NULL){
            
            string formatInfo = "ID Error: " + to_string(aux->getIDErr()) + "\\nTipo de Error: " + aux->getType() + "\\nInfo. Error: " + aux->getInfoErr();
            
            file<<"\tnodo_"<<count<<"[shape=record,label=\"{<f0>";
            file<<formatInfo;
            file<<"|<f1>Anterior}\"];\n";
            
            aux = aux->getAnterior();
            count++;
        }
        file<<"\tnodo_null[shape=none,label=\"NULL\"]\n";
        file<<"\n";
        file<<"\tnodo_inicio->nodo_0[label=\"Primero\"]\n";
        if (limit == 1){
            file<<"\tnodo_0->nodo_null\n";
        }else{
            for (int i = 1; i < limit; i++){
                file<<"\tnodo_"<<i-1<<":f1";
                file<<"->";
                file<<"nodo_"<<i<<":f0\n";
            }
            file<<"\tnodo_"<<limit-1<<":f1";
            file<<"->nodo_null\n";
        }
        file<<"}\n";
        file.close();
        
        system(commandG.c_str());
        system(commandO.c_str());
        this->generates++;
    }
}

void Cola::recorrer(){
    NodoCola *aux = this->cabeza;
    cout<<"\n    -------- COLA --------"<<endl;
    if (estaVacia()){
        cout<<"\n     --- SIN REGISTROS ---"<<endl;
    }else{
        while (aux != NULL){
            aux->showInfo();
            aux = aux->getAnterior();
        }
    }
    
}