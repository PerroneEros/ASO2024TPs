#include <iostream>
using namespace std;

int main ()
{   int n = 5;
    int numeros [] = {5,3,1,2,4}; // ARREGLO DESORDENADO
    int pos;
    int aux;

    //ALGORITMO DE ORDENAMIENTO POR INSERCION
    for (int i=0; i< n; i++) // es para recorrer el arreglo
    {
        pos=i;
        aux= numeros[i];  // almacena el valor al que ingresa en el arreglo

        while ((pos>0) && (numeros[pos-1]< aux)) // segunda vuelta cuando el for esta en i=1 pos=1 pos=i, 5 > 3 
        {
            numeros[pos] = numeros [pos - 1]; // es lo mismo que estar en pos = 1 del arrglo asigna el valor 5 y en la pos =0 
            pos--;
        }
        //yo estaba en pos = 1 voy a pos =0 ;
        numeros[pos] = aux;       
    }

    //IMPRIMO EN ORDE ASCENDENTE ORDENADO !
    cout <<"Arreglo Ordenado : ";
    for (int j=0; j< n; j++)
    {
       cout<< numeros[j] <<" "; 
    }


}