#include<iostream>

using namespace std;

int main()

{

    int n,mitad,primero,ultimo,x, a[] = {0,1,2,3,4,5,6,7,8,9};

    primero = 0;

    ultimo = 9;

    x = 0;

    cout<< "ingresa el numero a buscar:" ;

    cin>> n;

    
    while (primero <= ultimo && x == 0)

    {

        mitad = (primero + ultimo) / 2;

        cout << mitad << "\t";

        if (n == a[mitad])

            x = 1;

        else if (n < a[mitad])

            ultimo = mitad -1;

        else if (n > a[mitad])

            primero = mitad + 1;

    }

    if (x == 1)

        cout<<" El numero se encuentra en el vector";

    else

        cout<< "El numero no se encuentra el vector";

    return 0;

}