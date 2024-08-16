a = int(input("ingrese un numero:"))
b = int(input("ingrese un numero:"))
x = int(input("ingrese un numero:"))

print(f"los multiplos de {x} son:")
for i in range(a,b+1,1):
    if ((x % i) == 0):
        print(i,end=", ") 
