//Proyecto 1 Perrone Eros
//librerias
#include <iostream>
#include <cmath>
#include <string>
using namespace std;

int main (){
//tipo de datos y variables que se van a usar 
 int dia, mes;
 string decision; 
 float invitados, total_de_invitados;

//ingreso de datos 
 cout << "ingrese el dia en el que nacio:" << endl;
 cin >> dia;
 cout << "ingrese el mes en el que nacio:" << endl;
 cin >> mes;
//te dice el signo dependiendo el mes y el dia de nacimiento 
 if ((mes >=1) && (mes <=12)){
    if (mes == 1){
        if ((dia >= 1) && (dia <= 20)){
            cout << "El sigo del zodiaco es: Capricornio" << endl;
         }
        else {
            if ((dia >= 21) && (dia <= 31)) {
            cout << "El signo del zodiaco es: Acuario" << endl;
        }
     }
    }else if (mes == 2){
        if ((dia >=1 ) && (dia <= 19)) {
            cout << "El signo del zodiaco es:Acuario" << endl;
         }
         else {
             if ((dia >= 20) && (dia <= 29)) {                         //lo pongo en 29 por si el año es bisiesto
                 cout << "El signo del zodiaco es: Piscis" << endl;
             }
         }
    }else if(mes == 3){ 
        if ((dia >= 1) && (dia <= 20)) {
            cout << "El signo del zodiaco es: Piscis" << endl;
         }
        else{
            if ((dia >= 21) && (dia <= 31)) {
                cout << "El signo del zodiaco es: Aries" << endl;
            }
        }
    }else if (mes == 4){
        if ((dia >= 1) && (dia <= 19)) {
            cout << "El signo del zodiaco es:Aries" << endl;
         }
         else {
             if ((dia >= 20) && (dia <=30)) {
                 cout << "El signo del zodiaco es: Tauro" << endl;
             }
         }
    }else if (mes == 5){
        if ((dia >= 1) && (dia <= 20)) {
            cout << "El signo del zodiaco es: Tauro" << endl;
         }
        else{
            if ((dia >= 21) && (dia <= 31)) {
                cout << "El signo del zodiaco es: Geminis" << endl;
            }
        }  
    }else if (mes == 6){
        if ((dia >= 1) && (dia <= 21)) {
           cout << "El signo del zodiaco es: Geminis" << endl; 
         }
        else{
         if ((dia >= 22) && (dia <= 30)) {
             cout << "El signo del zodiaco es: Cancer" << endl;
         }   
        }
    }else if (mes == 7){
        if ((dia >= 1) && (dia <=22)) {
            cout << "El signo del zodiaco es: Cancer" << endl;
         }
        else {
            if ((dia >= 23) && (dia <= 31)) {
                cout << "El signo del zodiaco es: Leo" << endl;
            }
        }  
    }else if (mes == 8){
        if ((dia >= 1) && (dia <= 23)) {
            cout << "El signo del zodiaco es: Leo" << endl;
         }
        else{
            if((dia >= 24) && (dia <= 31)) {
                cout << "El signo del zodiaco es: Virgo" << endl;
             }
            }
    }else if (mes == 9){
        if ((dia >= 1) && (dia <= 22)) {
            cout << "El signo del zodiaco es: Virgo" << endl;
         }
        else{
            if ((dia >= 23) && (dia <= 30)) {
                cout << "El signo del zodiaco es: Libra" << endl;
            }
        } 
    }else if (mes == 10){
        if ((dia >= 1) && (dia <= 22)) {
            cout << "El signo del zodiaco es: Libra" << endl;
         }
        else{
            if((dia >= 23) && (dia <=31)) {
                cout << "El signo del zodiaco es: Escorpio" << endl;
            }
        } 
    }else if (mes == 11){
        if ((dia >= 1) && (dia <= 22)) {
            cout << "El signo del zodiaco es: Escorpio" << endl;
         }
        else{
            if ((dia >= 23) && (dia <= 30)) {
                cout << "El signo del zodiaco es: Sagitario" << endl;
            }
        }
    }else if (mes == 12){
        if ((dia >= 1) && (dia <= 21)){
            cout << "El signo del zodiaco es: Sagitario" << endl;
         }
        else{
            if ((dia >= 22) && (dia <= 31)){
                cout << "El signo del zodiaco es: Capricornio" << endl;
            }
        } 
    }
 }
else {                                                        //por si se confunde de mes 
     cout << "Mes invalido porfavor ingrese devuelta" << endl;
   }

//punto 2
//ingreso de datos
 cout << "¿te gusta festejar tu cumpleaños?(Si:s No:n):" << endl;    
 cin >> decision;
 
 if (((decision == "si") || (decision == "SI")) || ((decision == "no") || (decision == "NO"))) {  //ve si entra o no 
  if ((decision == "SI") || (decision == "si")) {
     cout << "Que Bueno" << endl;
   }
  else {
      if(((decision == "NO") || (decision == "no"))){
       cout << "Que Lastima" << endl;
      }
   } 
 }
 else{                                                                                          //si no entra escribe el mensaje 
   cout << "Vuelva a intentar, Solo esta permitido--->el ingreso de 'si' o 'no' " << endl;  
 }

 //punto 3
 //ingreso de datos
 cout << "¿cuantos invitados van a asistir a su cumpleaños?:" << endl;
 cin >> invitados;
 
 invitados = abs(invitados);                             //por si el usuario pone un numero negativo 
 total_de_invitados = round(sqrt(pow(invitados,4)));    //tambien se puede hacaer con un invitados*invitados*invitados*invitados
 
 cout << "tus invitados ^ 4,raiz cuadrada y redondeado el valor son:" << total_de_invitados << endl;

return 0;
}