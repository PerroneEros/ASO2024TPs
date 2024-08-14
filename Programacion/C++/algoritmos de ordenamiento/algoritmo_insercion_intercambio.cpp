#include <iostream>
using namespace std;

int main ()
{   int n = 5;
    int numeros [] = {5,3,1,2,4}; // ARREGLO DESORDENADO
    int pos;
    int tmp;
    //ALGORITMO DE ORDENAMIENTO POR INSERCION CON INTERCAMBIOS
    for (int i = 0; i < n; i++)
    {
       pos=i;
        while ((pos >0 ) && (numeros[pos-1] > numeros[pos]))
        {
            //INTERCAMBIAMOS CON LA VARIABLE TEMPORAL
            tmp = numeros[pos];
            numeros[pos] = numeros [pos - 1];
            numeros [pos - 1]=tmp;
            pos--;
        }
          
     }
}
    //IMPRIMO EN ORDEN ASCENDENTE ORDENADO !
    cout<<"Arreglo Ordenado : ";
    for (int j=0; j< n; j++)
    {
       cout<< numeros[j] <<" "; 
    }
