//Ordenacion de vectores
//Metodo de la burbuja
#include<iostream>
using namespace std;

void burbuja();


int main()
{
    burbuja();
    return 0;
}

void burbuja()
{
 int n = 7;
    int i,j,temp,a[n] = {2,3,1,4,7,8,3};
    for (i = 0; i < n-1; ++i){
        for (j = 0; j < n-1; ++j){
            if (a[j] > a[j+1]){
                temp = a[j];
                a[j] = a[j+1];
                a[j+1] = temp;
            }
        }
    }
    for (i = 0; i < n; ++i){
        cout<< a[i] <<endl;
    }

   } 