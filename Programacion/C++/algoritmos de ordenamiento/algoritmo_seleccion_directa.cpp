//Ordenacion por seleccion directa
#include<iostream>
using namespace std;
int main()
{
    int n = 3;
    int i,j,x,menor,a[n] = {3,1,2};
    for (i = 0; i < n-1; ++i){
        menor = a[i];
        x = i;
        for (j = i; j < n; ++j){
            if (a[j] > menor){
                menor = a[j];
                x = j;
            }
        }
        a[x] = a[i];
        a[i] = menor;
    }
    for (i = 0; i < n; ++i){
        cout<< a[i] << endl;
    }
    return 0;
}