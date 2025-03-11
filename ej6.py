print("ingrese un numero")
num =float(input())
print("elija la operacion: suma, resta, multiplicacion, division")
op =  str(input())
if op == "suma":
    print("elija cuanto sumar al anterior")
    aux= float(input())
    print(num + aux)
if op == "resta":
    print("elija cuanto restae al anterior")
    aux= float(input())
    print(num - aux)
if op == "multiplicacion":
    print("elija por cuanto multiplicae al anterior")
    aux= float(input())
    print(num * aux)
if op == "division":
    print("elija por cuanto dividir al anterior")
    aux= float(input())
    print(num / aux)
