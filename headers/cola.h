#ifndef COLA_H
#define COLA_H

#include <iostream>
#include <string>
#include <fstream>
#include "nodo_cola.h"
#include "node_student.h"
#include "node_task.h"

using namespace std;

class Cola{
private:
    NodoCola *cabeza;
    int size;
    int countRegis;
    int generates;
public:
    Cola();

    bool estaVacia();
    int getSize();

    void queue(NodeStudent *errStudent_, string infoErr_);
    void queue(NodeTask *errTask_, string infoErr_);
    void dequeue();
    void graficar();
    void recorrer();
};


#endif