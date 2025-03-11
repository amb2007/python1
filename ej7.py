print("hola, ingrese su nombre:")
nombre  =str(input())
print("cuantos años tienes " +nombre +" ?")
edad = int(input())
print("donde vives " +nombre +" ?")
home = str(input())
year= 2025 - edad
print(nombre+ " naciste en el " +  year)
if edad < 18:
    print("eres menor de edad")
else: 
    print("eres mayor de edad")
if edad % 5 == 0:
    print("su edad esmultiplo de 5")
else:
    print("su edad no es multiplo de 5")