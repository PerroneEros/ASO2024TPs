
largo =int(input("ingrese el largo del rectangulo:"))
ancho =int(input("ingrese el ancho del rectangulo:"))

while not (((largo <= 40) and (largo > 0)) and ((ancho > 0) and (ancho < largo))):
    
    if ((largo > 40) or (largo < 0)):
        largo =int(input("ingrese el largo del rectangulo"))

    if ((ancho < 0) or (ancho > largo)):
        ancho =int(input("ingrese el ancho del rectangulo")) 

for i in range(1,largo+1,1):
   
    for j in range (1,ancho+1,1):
        print('*',end=" ")
    print()
