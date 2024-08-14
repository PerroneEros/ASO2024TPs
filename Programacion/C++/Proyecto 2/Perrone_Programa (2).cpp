//-------------------------PROYECTO-Nª2-----------------------------------------
//-------------------------PERRONE-EROS-----------------------------------------
#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;
//------------------------VARIABLES-GLOBALES------------------------------------
const int filas = 3, columnas = 3;
int matriz[filas][columnas];

bool matrizCargada = false;
bool matrizMostrada = false;
bool valorBuscado = false;
bool valorExtremoObtenido = false;

//-------------------------PROTOTIPOS-------------------------------------------
void cargarMatrizAleatoria(int matriz[filas][columnas]);
void cargarMatrizManual(int matriz[filas][columnas]);
void mostrarMatriz(int matriz[filas][columnas]);
bool buscarValor(int matriz[filas][columnas], int valor);
void obtenerValorExtremo(int matriz[filas][columnas], string tipo);
void ordenarMatrizInsercion(int matriz[filas][columnas], bool ascendente);
void ordenarMatrizIntercambio(int matriz[filas][columnas], bool ascendente);
void mostrarMenu();
//-----------------------PROGRAMA-PRINCIPAL-------------------------------------
int main() {
    srand(time(NULL)); // Inicializa la semilla para los números aleatorios
    mostrarMenu(); // Muestra el menú
    return 0;
}
//---------------------------FUNCIONES------------------------------------------
// Función para mostrar el menú
void mostrarMenu() {
    int opcion, valorBuscar;
    char forma;
    string extremo;

    do {
        // Muestra las opciones del menu
        cout << "Seleccione una opcion:" << endl;
        cout << "1. Cargar la matriz" << endl;
        cout << "2. Mostrar los valores de la matriz" << endl;
        cout << "3. Buscar un valor específico" << endl;
        cout << "4. Obtener el valor máximo o minimo de la matriz" << endl;
        cout << "5. Ordenar la matriz" << endl;
        cout << "6. Salir del programa" << endl;
        cin >> opcion;

        switch (opcion) {
            case 1:
                // Cargar la matriz de forma aleatoria o manual
                cout << "¿Quiere cargar la matriz de forma aleatoria o manual? (a/m): ";
                cin >> forma;
                if (forma == 'a' || forma == 'A') {
                    cargarMatrizAleatoria(matriz);
                } else if (forma == 'm' || forma == 'M') {
                    cargarMatrizManual(matriz);
                } else {
                    cout << "Opción no válida." << endl;
                }
                matrizCargada = true;
                cout << endl;
                break;
            case 2:
                // Mostrar la matriz
                if (!matrizCargada) {
                    cout << "Debe cargar la matriz primero (opción 1)." << endl;
                } else {
                    mostrarMatriz(matriz);
                    matrizMostrada = true;
                }
                cout << endl;
                break;
            case 3:
                // Buscar un valor en la matriz
                if (!matrizCargada || !matrizMostrada) {
                    cout << "Debe cargar la matriz y mostrarla primero (opciones 1 y 2)." << endl;
                } else {
                    cout << "Ingrese el número a buscar: ";
                    cin >> valorBuscar;
                    buscarValor(matriz, valorBuscar);
                    valorBuscado = true;
                }
                cout << endl;
                break;
            case 4:
                // Obtener el valor máximo o mínimo de la matriz
                if (!matrizCargada || !matrizMostrada || !valorBuscado) {
                    cout << "Debe cargar la matriz, mostrarla y buscar un valor primero (opciones 1, 2 y 3)." << endl;
                } else {
                    cout << "¿Qué valor quiere devolver? (max/min): ";
                    cin >> extremo;
                    obtenerValorExtremo(matriz, extremo);
                    valorExtremoObtenido = true;
                }
                cout << endl;
                break;
            case 5:
                // Ordenar la matriz usando inserción o intercambio
                if (!matrizCargada || !matrizMostrada || !valorBuscado || !valorExtremoObtenido) {
                    cout << "Debe cargar la matriz, mostrarla, buscar un valor y obtener el valor extremo primero (opciones 1, 2, 3 y 4)." << endl;
                } else {
                    cout << "¿Qué método de ordenamiento desea utilizar?" << endl;
                    cout << "1. Ordenar por método de inserción." << endl;
                    cout << "2. Ordenar por método de intercambio." << endl;
                    int metodo;
                    cin >> metodo;
                    bool ascendente;
                    cout << "¿Desea ordenar de forma ascendente o descendente? (a/d): ";
                    cin >> forma;
                    ascendente = (forma == 'a' || forma == 'A');

                    if (metodo == 1) {
                        ordenarMatrizInsercion(matriz, ascendente);
                    } else if (metodo == 2) {
                        ordenarMatrizIntercambio(matriz, ascendente);
                    } else {
                        cout << "Opción no válida." << endl;
                    }
                }
                cout << endl;
                break;
            case 6:
                // Salir del programa
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                // Manejar opciones no válidas
                cout << "Opción no válida. Intente nuevamente." << endl;
                break;
        }
    } while (opcion != 6);
}

// Función para cargar la matriz con valores aleatorios
void cargarMatrizAleatoria(int matriz[filas][columnas]) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matriz[i][j] = rand() % 100 + 1; // Carga la matriz con valores aleatorios del 1 al 100
        }
    }
    cout << "Matriz cargada aleatoriamente." << endl;
}

// Función para cargar la matriz con valores ingresados manualmente
void cargarMatrizManual(int matriz[filas][columnas]) {
    cout << "Ingrese los valores de la matriz:" << endl;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cin >> matriz[i][j]; // Carga la matriz con valores ingresados por el usuario
        }
    }
    cout << "Matriz cargada manualmente." << endl;
}

// Función para mostrar los valores de la matriz
void mostrarMatriz(int matriz[filas][columnas]) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cout << matriz[i][j] << "\t"; // Muestra los valores de la matriz
        }
        cout << endl;
    }
}

// Función para buscar un valor en la matriz
bool buscarValor(int matriz[filas][columnas], int valor) {
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            if (matriz[i][j] == valor) {
                cout << "Valor encontrado en fila " << i + 1 << ", columna " << j + 1 << endl;
                return true;
            }
        }
    }
    cout << "Valor no encontrado." << endl;
    return false;
}

// Función para obtener el valor máximo o mínimo de la matriz
void obtenerValorExtremo(int matriz[filas][columnas], string tipo) {
    int valor = matriz[0][0];
    if (tipo == "max") {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] > valor) {
                    valor = matriz[i][j]; // Encuentra el valor máximo en la matriz
                }
            }
        }
        cout << "El valor máximo es: " << valor << endl;
    } else if (tipo == "min") {
        for (int i = 0; i < filas; i++) {
            for (int j = 0; j < columnas; j++) {
                if (matriz[i][j] < valor) {
                    valor = matriz[i][j]; // Encuentra el valor mínimo en la matriz
                }
            }
        }
        cout << "El valor mínimo es: " << valor << endl;
    } else {
        cout << "Opción no válida." << endl;
    }
}

// Función para ordenar la matriz usando el método de inserción
void ordenarMatrizInsercion(int matriz[filas][columnas], bool ascendente) {
    int lineal[filas * columnas];
    int posicion = 0;

    // Copiar la matriz en un arreglo
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            lineal[posicion++] = matriz[i][j];
        }
    }

    // Aplicar el método de ordenación por inserción al arreglo
    int n = filas * columnas;
    for (int i = 1; i < n; i++) {
        int valoractual = lineal[i];
        int j = i - 1;

        // Orden ascendente
        if (ascendente) {
            while (j >= 0 && lineal[j] > valoractual) {
                lineal[j + 1] = lineal[j];
                j--;
            }
        }
        // Orden descendente
        else {
            while (j >= 0 && lineal[j] < valoractual) {
                lineal[j + 1] = lineal[j];
                j--;
            }
        }
        lineal[j + 1] = valoractual;
    }

    // Copiar el arreglo ordenado de nuevo a la matriz original
    posicion = 0;
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matriz[i][j] = lineal[posicion++];
        }
    }

    if (ascendente) {
        cout << "Matriz ordenada por método de inserción (ascendente)." << endl;
    } else {
        cout << "Matriz ordenada por método de inserción (descendente)." << endl;
    }
}

// Función para ordenar la matriz usando el método de intercambio (
void ordenarMatrizIntercambio(int matriz[filas][columnas], bool ascendente) {
    int n = filas * columnas;
    for (int k = 0; k < n - 1; k++) {
        for (int i = 0; i < n - k - 1; i++) {
            int fila1 = i / columnas;
            int col1 = i % columnas;
            int fila2 = (i + 1) / columnas;
            int col2 = (i + 1) % columnas;

            // Orden ascendente
            if (ascendente) {
                if (matriz[fila1][col1] > matriz[fila2][col2]) {
                    // Intercambiar elementos
                    int temp = matriz[fila1][col1];
                    matriz[fila1][col1] = matriz[fila2][col2];
                    matriz[fila2][col2] = temp;
                }
            }
            // Orden descendente
            else {
                if (matriz[fila1][col1] < matriz[fila2][col2]) {
                    // Intercambiar elementos
                    int temp = matriz[fila1][col1];
                    matriz[fila1][col1] = matriz[fila2][col2];
                    matriz[fila2][col2] = temp;
                }
            }
        }
    }

    if (ascendente) {
        cout << "Matriz ordenada por método de intercambio (ascendente)." << endl;
    } else {
        cout << "Matriz ordenada por método de intercambio (descendente)." << endl;
    }
}
