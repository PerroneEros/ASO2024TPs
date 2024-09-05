'''2. Escriba una función llamada EsBisiesto que permita ingresar un número de año y 
devuelva verdadero en caso que el año sea bisiesto, o falso cuando no lo es. Un año 
es bisiesto si: es divisible entre cuatro y (no es divisible entre 100 o es divisible entre 
400). Utilizarlo en un programa que permita ingresar dia, mes y año y muestre por 
pantalla si la fecha es válida o no. '''

def Esbisiesto(anio):
    if anio % 4 == 0:
        if anio % 100 == 0:
            if anio % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    return False

def ValidarFecha(dia,mes,anio):
    if mes < 1 or mes > 12:
        print("El mes es incorrecto")
        return False
    elif mes in (4, 6, 9, 11):
        if dia < 1 or dia > 30:
            print("El día es incorrecto para el mes")
            return False
    elif mes in (1,3,5,7,8,10,12):
       if dia < 1 or dia > 31: 
            print("El día es incorrecto para el mes")
            return False
    elif mes == 2:
        if Esbisiesto(anio):
            if dia < 1 or dia > 29:
                print("El día es incorrecto para el mes")
                return False
        else:
            if dia < 1 or dia > 28:
                print("El día es incorrecto para el mes")
                return False
    return True

dia = int(input("ingrese un dia:"))
mes = int(input("ingrese un mes:"))
anio = int(input("ingrese un año:"))

if ValidarFecha(dia,mes,anio):
    print("la fecha es valida")
else:
    print("la fecha es invalida")    